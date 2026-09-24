"""Structural parsing for the admitted Foundation lifecycle owners only."""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path, PurePosixPath
import re
import unicodedata


ID_RE = re.compile(r"^(?:BLG|DEC)-[a-z0-9]+(?:-[a-z0-9]+)*$")
FRAGMENT_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
RECORD_ENTRY_RE = re.compile(r"^-\s+\[[^\]\r\n]+\]\(([^)\r\n]+)\)(?:\s+—\s+\S.*)?\s*$")
REFERENCE_DEFINITION_RE = re.compile(
    r"^\s*(?:(?:[-+*]|\d+[.)])[ \t]+)*\[[^\]\r\n]+\]:"
)
CONTROL_RE = re.compile(r"[\x00-\x1f\x7f-\x9f\u200b-\u200f\u202a-\u202e\u2060\ufeff]")
NON_COMMONMARK_LINE_SEPARATOR_RE = re.compile(r"[\x0b\x0c\x1c-\x1e\x85\u2028\u2029]")
GFM_AUTOLINK_RE = re.compile(
    r"(?<![A-Za-z0-9_])(?:"
    r"(?:https?://|ftp://|www\.)[^\s<>]+"
    r"|[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z]{2,}"
    r")",
    re.IGNORECASE,
)
BACKLOG_COLUMNS = ["Immutable ID", "Title", "State", "Source / evidence", "Value / risk", "Dependencies", "Disposition owner", "Next gate"]
DECISION_COLUMNS = ["Immutable ID", "State", "Question and accepted direction", "Alternatives considered / rationale", "Named canonical targets", "Target-consolidation evidence"]
ROADMAP_COLUMNS = ["Phase / theme", "Horizon", "Gate status", "Dependencies", "Expected outcome", "Exit gate"]
AUTHORITY_COLUMNS = ["Field / truth", "Canonical owner", "Other surfaces"]
TRANSITION_COLUMNS = ["From", "Actor / evidence", "To", "Rule"]


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    coordinate: str
    rule: str

    def render(self) -> str:
        return f"{self.path}:{self.coordinate}: {self.rule}"


class Validator:
    def __init__(self, root: Path):
        self.root = root
        self.findings: list[Finding] = []

    def add(self, path: Path, coordinate: str, rule: str) -> None:
        try:
            relative = path.relative_to(self.root).as_posix()
        except ValueError:
            relative = "<root>"
        if unsafe(relative):
            relative = "<unsafe-path>"
        self.findings.append(Finding(relative, coordinate, rule))

    def read(self, relative: str) -> str | None:
        path = self.root / relative
        try:
            path.resolve(strict=False).relative_to(self.root.resolve(strict=True))
        except (OSError, RuntimeError, ValueError):
            self.add(path, "file", "OWNER_CONFINEMENT")
            return None
        if not path.is_file() or path.is_symlink():
            self.add(path, "file", "OWNER_MISSING")
            return None
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            self.add(path, "file", "UTF8_INVALID")
            return None
        except OSError:
            self.add(path, "file", "OWNER_UNREADABLE")
            return None

    def require_heading(self, path: Path, text: str, heading: str) -> None:
        visible = "\n".join(line for _, line in visible_markdown_lines(text))
        if len(re.findall(rf"(?m)^{re.escape(heading)}\s*$", visible)) != 1:
            self.add(path, "heading", "HEADING_REQUIRED")

    def require_literal_in_section(self, path: Path, text: str, heading: str, value: str) -> None:
        visible = "\n".join(line for _, line in visible_markdown_lines(text))
        level = len(heading.split()[0])
        section = re.search(rf"(?ms)^{re.escape(heading)}\s*$\n(.*?)(?=^#{{1,{level}}}\s|\Z)", visible)
        if not section or section.group(1).count(value) != 1:
            self.add(path, "schema", "BOOTSTRAP_REQUIRED")

    def require_exact_line_in_section(self, path: Path, text: str, heading: str, value: str) -> None:
        visible = "\n".join(line for _, line in visible_markdown_lines(text))
        section = re.search(rf"(?ms)^{re.escape(heading)}\s*$\n(.*?)(?=^#{{1,3}}\s|\Z)", visible)
        if not section or sum(line == value for line in section.group(1).splitlines()) != 1:
            self.add(path, "schema", "BOOTSTRAP_REQUIRED")

    def table_after(self, path: Path, text: str, heading: str, columns: list[str]) -> list[tuple[int, list[str]]]:
        visible = "\n".join(line for _, line in visible_markdown_lines(text))
        marker = re.search(rf"(?m)^{re.escape(heading)}\s*$", visible)
        if not marker:
            return []
        section = visible[marker.end():]
        section = re.split(r"(?m)^#{1,%d}\s" % len(heading.split()[0]), section, maxsplit=1)[0]
        lines = section.splitlines()
        gfm_starts = [index for index, line in enumerate(lines) if split_gfm_row(line) == columns]
        starts = [index for index in gfm_starts if split_row(lines[index]) == columns]
        if len(gfm_starts) != 1 or len(starts) != 1:
            self.add(path, "table", "TABLE_REQUIRED" if not gfm_starts else "TABLE_SCHEMA")
            return []
        start = starts[0]
        if start is None or start + 1 >= len(lines):
            self.add(path, "table", "TABLE_REQUIRED")
            return []
        header = split_row(lines[start])
        divider = split_row(lines[start + 1])
        if header is None or divider is None or header != columns or len(divider) != len(columns) or any(not re.fullmatch(r":?-{3,}:?", cell) for cell in divider):
            self.add(path, "table", "TABLE_SCHEMA")
            return []
        rows: list[tuple[int, list[str]]] = []
        for offset, line in enumerate(lines[start + 2:], start + 3):
            if not line.strip():
                break
            gfm_row = split_gfm_row(line)
            if gfm_row is None:
                if line.lstrip().startswith("|"):
                    self.add(path, f"row-{offset}", "TABLE_ROW")
                    continue
                break
            row = split_row(line)
            if row is None or len(row) != len(columns):
                self.add(path, f"row-{offset}", "TABLE_ROW")
            else:
                rows.append((offset, row))
        return rows

    def check_link(self, source: Path, destination: str, coordinate: str) -> Path | None:
        if (unsafe(destination) or any(char.isspace() for char in destination)
                or any(char in destination for char in ("\\", "<", ">", "?", "%", "&", "(", ")", '"', "'"))
                or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", destination)):
            self.add(source, coordinate, "LINK_DESTINATION")
            return None
        target_text, separator, fragment = destination.partition("#")
        if destination.count("#") > 1 or (separator and not FRAGMENT_RE.fullmatch(fragment)) or not target_text:
            self.add(source, coordinate, "LINK_DESTINATION")
            return None
        candidate = PurePosixPath(target_text)
        if candidate.is_absolute() or str(candidate) in {".", ""}:
            self.add(source, coordinate, "LINK_DESTINATION")
            return None
        target = source.parent.joinpath(*candidate.parts)
        try:
            lexical_target = Path(os.path.normpath(target))
            lexical_target.relative_to(self.root)
            resolved = target.resolve(strict=False)
            resolved.relative_to(self.root.resolve(strict=True))
        except (OSError, RuntimeError, ValueError):
            self.add(source, coordinate, "LINK_CONFINEMENT")
            return None
        if not target.exists() or not resolved.is_file():
            self.add(source, coordinate, "LINK_MISSING")
            return None
        return resolved

    def check_canonical_target(self, source: Path, destination: str, coordinate: str) -> Path | None:
        """Validate a root-relative canonical target stored in a decision cell."""
        if (unsafe(destination) or any(char.isspace() for char in destination)
                or any(char in destination for char in ("\\", "<", ">", "?", "%", "&", "#", ":", "(", ")", '"', "'"))):
            self.add(source, coordinate, "LINK_DESTINATION")
            return None
        candidate = PurePosixPath(destination)
        if (candidate.is_absolute() or str(candidate) in {".", ""}
                or destination != candidate.as_posix() or any(part in {".", ".."} for part in candidate.parts)):
            self.add(source, coordinate, "LINK_DESTINATION")
            return None
        target = self.root.joinpath(*candidate.parts)
        try:
            resolved = target.resolve(strict=False)
            resolved.relative_to(self.root.resolve(strict=True))
        except (OSError, RuntimeError, ValueError):
            self.add(source, coordinate, "LINK_CONFINEMENT")
            return None
        if not target.exists() or not resolved.is_file():
            self.add(source, coordinate, "LINK_MISSING")
            return None
        return resolved

    def check_links(self, path: Path, text: str) -> None:
        if not markdown_block_context_balanced(text):
            self.add(path, "file", "MARKDOWN_AMBIGUOUS")
        visible = visible_markdown_lines(text)
        visible_text = "\n".join(content for _, content in visible)
        if NON_COMMONMARK_LINE_SEPARATOR_RE.search(text):
            self.add(path, "file", "MARKDOWN_AMBIGUOUS")
        if multiline_inline_link_syntax(visible_text):
            self.add(path, "file", "LINK_DESTINATION")
        table_lines = gfm_table_line_numbers(visible)
        for line, content in visible:
            fragments = [content]
            if line in table_lines:
                row = split_gfm_row(content)
                if row is None:
                    self.add(path, f"line-{line}", "MARKDOWN_AMBIGUOUS")
                    continue
                fragments = row
            for fragment in fragments:
                matches, balanced = links_outside_code(fragment)
                if not balanced:
                    self.add(path, f"line-{line}", "MARKDOWN_AMBIGUOUS")
                masked, _ = mask_inline_code(fragment)
                if re.search(r"\[[^\]]+\]\[[^\]]*\]", masked) or REFERENCE_DEFINITION_RE.search(masked):
                    self.add(path, f"line-{line}", "LINK_DESTINATION")
                if GFM_AUTOLINK_RE.search(masked):
                    self.add(path, f"line-{line}", "LINK_DESTINATION")
                if "<" in masked or ">" in masked:
                    self.add(path, f"line-{line}", "MARKDOWN_AMBIGUOUS")
                if re.search(r"<(?:[A-Za-z][A-Za-z0-9+.-]*:|//)[^>\s]*>", masked):
                    self.add(path, f"line-{line}", "LINK_DESTINATION")
                for match in matches:
                    self.check_link(path, match.group(1), f"line-{line}")
                image_matches = list(IMAGE_RE.finditer(masked))
                for match in image_matches:
                    self.check_link(path, match.group(1), f"line-{line}")
                recognized = [*matches, *image_matches]
                for residual in re.finditer(r"\]\([^)]*\)", masked):
                    if not any(match.start() <= residual.start() and residual.end() <= match.end() for match in recognized):
                        self.add(path, f"line-{line}", "LINK_DESTINATION")

    def validate(self) -> list[Finding]:
        if not self.root.is_dir() or any(Path(*self.root.parts[:index]).is_symlink() for index in range(1, len(self.root.parts) + 1)):
            self.add(self.root, "root", "ROOT_INVALID")
            return sorted(set(self.findings))
        lifecycle = self.read("evolution_lifecycle.md")
        if lifecycle is not None:
            path = self.root / "evolution_lifecycle.md"
            state_headings = ("### Candidates", "### Capabilities", "### Tactical TODOs", "### Decisions", "### Contract verification")
            for heading in ("## Immutable identifiers", "## Authority matrix", "## State machines", *state_headings):
                self.require_heading(path, lifecycle, heading)
            for literal in ("BLG-<slug>", "CAP-<slug>", "DEC-<slug>"):
                self.require_literal_in_section(path, lifecycle, "## Immutable identifiers", literal)
            section_fields = {
                "### Candidates": (
                    "**Schema:** immutable ID; title; state; source/evidence link; value/risk; dependencies; disposition owner; next gate.",
                    "**Enum:** `Proposed|Under-Review|Selected-for-Planning|Deferred|Rejected`",
                ),
                "### Capabilities": (
                    "**Schema:** immutable ID; module owner; state; evidence; dependency links; intended outcome; retirement rationale when applicable.",
                    "**Enum:** `Not-Assessed|Discovery|Planned|In-Progress|Delivered|Retired`",
                ),
                "### Tactical TODOs": (
                    "**Schema:** immutable TODO path/identity; objective; scope; state; approval evidence; owner; validation/evidence; delivery disposition.",
                    "**Enum:** `Draft|Review|Approved|In-Progress|Completed|Cancelled`",
                ),
                "### Decisions": (
                    "**Schema:** immutable ID; question; alternatives; rationale; provenance/evidence; state; named canonical targets; target-consolidation evidence; supersession link when applicable.",
                    "**Enum:** `Proposed|Accepted|Superseded|Rejected`",
                ),
                "### Contract verification": (
                    "**Schema:** contract reference; responsible module; state; evidence link; verification scope; deprecation successor when applicable.",
                    "**Enum:** `Not-Assessed|Documented|Verified|Deprecated`",
                ),
            }
            for heading, fields in section_fields.items():
                for field in fields:
                    self.require_exact_line_in_section(path, lifecycle, heading, field)
            self.table_after(path, lifecycle, "## Authority matrix", AUTHORITY_COLUMNS)
            for heading in state_headings:
                self.table_after(path, lifecycle, heading, TRANSITION_COLUMNS)
            self.check_links(path, lifecycle)
        self.validate_backlog()
        self.validate_decisions()
        self.validate_roadmap()
        return sorted(set(self.findings))

    def validate_backlog(self) -> None:
        text = self.read("backlog/README.md")
        if text is None:
            return
        path = self.root / "backlog/README.md"
        self.require_heading(path, text, "## Candidates")
        ids: set[str] = set()
        for line, row in self.table_after(path, text, "## Candidates", BACKLOG_COLUMNS):
            identifier, state = row[0], row[2]
            if not ID_RE.fullmatch(identifier) or not identifier.startswith("BLG-") or CONTROL_RE.search(identifier):
                self.add(path, f"row-{line}", "ID_INVALID")
            elif identifier in ids:
                self.add(path, f"row-{line}", "ID_DUPLICATE")
            ids.add(identifier)
            if state not in {"Proposed", "Under-Review", "Selected-for-Planning", "Deferred", "Rejected"} or CONTROL_RE.search(state):
                self.add(path, f"row-{line}", "STATE_INVALID")
            links = list(LINK_RE.finditer(row[3]))
            if len(links) != 1 or row[3].strip() != links[0].group(0):
                self.add(path, f"row-{line}", "LINK_REQUIRED")
        self.check_links(path, text)

    def validate_decisions(self) -> None:
        index = self.read("decisions/README.md")
        if index is None:
            return
        index_path = self.root / "decisions/README.md"
        self.require_heading(index_path, index, "## Records")
        visible_index = "\n".join(line for _, line in visible_markdown_lines(index))
        records = re.search(r"(?ms)^## Records\s*$\n?(.*?)(?=^##\s|\Z)", visible_index)
        if not records:
            self.add(index_path, "heading", "HEADING_REQUIRED")
            return
        self.check_links(index_path, index)
        indexed: list[Path] = []
        for line, content in enumerate(records.group(1).splitlines(), index[:records.start(1)].count("\n") + 1):
            if not content.strip():
                continue
            entry = RECORD_ENTRY_RE.fullmatch(content)
            if not entry:
                self.add(index_path, f"line-{line}", "DECISION_MEMBERSHIP")
                continue
            target = self.check_link(index_path, entry.group(1), f"line-{line}")
            if target and target.parent == self.root / "decisions" and target.name != "README.md" and target.suffix == ".md":
                indexed.append(target)
            else:
                self.add(index_path, f"line-{line}", "DECISION_MEMBERSHIP")
        actual: set[Path] = set()
        for path in (self.root / "decisions").glob("*.md"):
            if path.name == "README.md":
                continue
            if path.is_symlink():
                self.add(path, "membership", "DECISION_MEMBERSHIP")
                try:
                    path.resolve(strict=False).relative_to(self.root.resolve(strict=True))
                except (OSError, RuntimeError, ValueError):
                    self.add(path, "membership", "LINK_CONFINEMENT")
                continue
            actual.add(path.resolve())
        if set(indexed) != actual or len(indexed) != len(set(indexed)):
            self.add(index_path, "membership", "DECISION_MEMBERSHIP")
        global_ids: set[str] = set()
        for path in sorted(set(indexed)):
            text = self.read(path.relative_to(self.root).as_posix())
            if text is None:
                continue
            lines = [line for _, line in visible_markdown_lines(text)]
            provenance_lines = [number for number, value in enumerate(lines, 1) if "**Provenance:**" in value]
            provenance_occurrences = sum(value.count("**Provenance:**") for value in lines)
            headers = [number for number, value in enumerate(lines, 1) if split_row(value) == DECISION_COLUMNS]
            valid_provenance = (provenance_occurrences == 1 and len(provenance_lines) == 1 and len(headers) == 1 and provenance_lines[0] < headers[0]
                                and bool(re.fullmatch(r"\*\*Provenance:\*\*\s*\S(?:.*\S)?\s*", lines[provenance_lines[0] - 1])))
            if not valid_provenance:
                self.add(path, "provenance", "PROVENANCE_SCHEMA")
            for line, row in self.table_with_columns(path, text, DECISION_COLUMNS):
                self.validate_decision_row(path, line, row, global_ids)
            self.check_links(path, text)

    def validate_decision_row(self, path: Path, line: int, row: list[str], ids: set[str]) -> None:
        identifier, state, targets, evidence = row[0], row[1], row[4], row[5]
        if not ID_RE.fullmatch(identifier) or not identifier.startswith("DEC-") or CONTROL_RE.search(identifier):
            self.add(path, f"row-{line}", "ID_INVALID")
        elif identifier in ids:
            self.add(path, f"row-{line}", "ID_DUPLICATE")
        ids.add(identifier)
        if state not in {"Proposed", "Accepted", "Superseded", "Rejected"} or CONTROL_RE.search(state):
            self.add(path, f"row-{line}", "STATE_INVALID")
        target_paths = [item.strip().strip("`") for item in targets.split(";")]
        evidence_parts = [item.strip() for item in evidence.split(";")]
        if (not target_paths or any(not item for item in target_paths) or any(not item for item in evidence_parts)
                or len(target_paths) != len(evidence_parts) or len(set(target_paths)) != len(target_paths)):
            self.add(path, f"row-{line}", "EVIDENCE_SHAPE")
            return
        resolved_targets: list[Path] = []
        for target, item in zip(target_paths, evidence_parts):
            resolved = self.check_canonical_target(path, target, f"row-{line}")
            if resolved is not None:
                resolved_targets.append(resolved)
            if state == "Proposed" and item != "PENDING":
                self.add(path, f"row-{line}", "EVIDENCE_SHAPE")
            if state in {"Accepted", "Rejected", "Superseded"} and item != "PENDING" and (not item.startswith(f"`{target}`") or not item[len(target) + 2:].strip()):
                self.add(path, f"row-{line}", "EVIDENCE_SHAPE")
        if len(resolved_targets) != len(set(resolved_targets)):
            self.add(path, f"row-{line}", "EVIDENCE_SHAPE")

    def validate_roadmap(self) -> None:
        text = self.read("system_roadmap.md")
        if text is None:
            return
        path = self.root / "system_roadmap.md"
        self.require_heading(path, text, "# LeadsHug — System Roadmap")
        for line, row in self.table_after(path, text, "# LeadsHug — System Roadmap", ROADMAP_COLUMNS):
            status, gate = row[2], row[5]
            if status not in {"Open", "Exit-Gate-Met"} or CONTROL_RE.search(status):
                self.add(path, f"row-{line}", "STATE_INVALID")
            if status == "Exit-Gate-Met":
                gate_links, balanced = links_outside_code(gate)
                if not balanced:
                    self.add(path, f"row-{line}", "MARKDOWN_AMBIGUOUS")
                targets = [self.check_link(path, match.group(1), f"row-{line}") for match in gate_links]
                names = {target.relative_to(self.root).as_posix() for target in targets if target}
                if (not any(name.startswith("modules/") and name.endswith(".md") for name in names)
                        or not any(name.startswith("todos/completed/") and name.endswith(".md") for name in names)):
                    self.add(path, f"row-{line}", "ROADMAP_EVIDENCE")
        self.check_links(path, text)

    def table_with_columns(self, path: Path, text: str, columns: list[str]) -> list[tuple[int, list[str]]]:
        lines = [line for _, line in visible_markdown_lines(text)]
        matches = []
        gfm_matches = []
        for index, line in enumerate(lines):
            if split_gfm_row(line) != columns:
                continue
            gfm_matches.append(index)
            if split_row(line) != columns:
                continue
            if index + 1 >= len(lines) or split_row(lines[index + 1]) is None:
                self.add(path, "table", "TABLE_SCHEMA")
                return []
            divider = split_row(lines[index + 1])
            if len(divider) != len(columns) or any(not re.fullmatch(r":?-{3,}:?", cell) for cell in divider):
                self.add(path, "table", "TABLE_SCHEMA")
                return []
            matches.append(index)
        if len(gfm_matches) != 1 or len(matches) != 1:
            self.add(path, "table", "TABLE_REQUIRED" if not gfm_matches else "TABLE_SCHEMA")
            return []
        index = matches[0]
        for index, line in [(index, lines[index])]:
            rows = []
            for number, candidate in enumerate(lines[index + 2:], index + 3):
                if not candidate.strip():
                    break
                gfm_row = split_gfm_row(candidate)
                if gfm_row is None:
                    if candidate.lstrip().startswith("|"):
                        self.add(path, f"row-{number}", "TABLE_ROW")
                        continue
                    break
                row = split_row(candidate)
                if row is None or len(row) != len(columns):
                    self.add(path, f"row-{number}", "TABLE_ROW")
                else:
                    rows.append((number, row))
            if not rows:
                self.add(path, "table", "TABLE_ROW")
            return rows
        return []


def split_row(line: str) -> list[str] | None:
    """Split the validator's canonical table form, which requires outer pipes."""
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return split_gfm_row(line)


def split_gfm_row(line: str) -> list[str] | None:
    """Split a GFM table row, including the allowed omission of outer pipes."""
    _, balanced = mask_inline_code(line)
    if not balanced:
        return None
    left = len(line) - len(line.lstrip())
    right = len(line.rstrip())
    source = line[left:right]
    leading_pipe = source.startswith("|")
    trailing_pipe = source.endswith("|") and not escaped_at(source, len(source) - 1)
    start = 1 if leading_pipe else 0
    end = len(source) - 1 if trailing_pipe else len(source)
    if not any(char == "|" and not escaped_at(source, index) for index, char in enumerate(source[start:end], start)):
        return None
    cells, current = [], []
    for index, char in enumerate(source[start:end], start):
        if char == "|" and not escaped_at(source, index):
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    cells.append("".join(current).strip())
    if any(not mask_inline_code(cell)[1] for cell in cells):
        return None
    return cells


def escaped_at(text: str, index: int) -> bool:
    preceding_slashes = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        preceding_slashes += 1
        cursor -= 1
    return preceding_slashes % 2 == 1


def gfm_table_line_numbers(lines: list[tuple[int, str]]) -> set[int]:
    """Return lines belonging to visible GFM table blocks."""
    table_lines: set[int] = set()
    for index, (_, content) in enumerate(lines):
        divider = split_gfm_row(content)
        if (divider is None or not divider
                or any(not re.fullmatch(r":?-{3,}:?", cell) for cell in divider)
                or index == 0):
            continue
        header = split_gfm_row(lines[index - 1][1])
        if header is None or len(header) != len(divider):
            continue
        table_lines.update((lines[index - 1][0], lines[index][0]))
        for number, row_text in lines[index + 1:]:
            if not row_text.strip():
                break
            if "|" not in row_text:
                break
            table_lines.add(number)
    return table_lines


def validate_root(root: Path | str) -> list[Finding]:
    return Validator(Path(root).absolute()).validate()


def unsafe(value: str) -> bool:
    return bool(CONTROL_RE.search(value) or any(not char.isprintable() or unicodedata.category(char) in {"Cf", "Cs"} for char in value))


def visible_markdown_lines(text: str) -> list[tuple[int, str]]:
    """Return source lines with fenced-code content blanked while preserving line numbers."""
    return scan_markdown_lines(text)[0]


def scan_markdown_lines(text: str) -> tuple[list[tuple[int, str]], bool, bool]:
    visible: list[tuple[int, str]] = []
    fence: tuple[str, int] | None = None
    comment = False
    ambiguous = False
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    for number, line in enumerate(normalized.split("\n"), 1):
        if comment:
            if "-->" in line:
                if line.split("-->", 1)[1].strip():
                    ambiguous = True
                comment = False
            visible.append((number, ""))
            continue
        if fence is not None:
            closing = re.fullmatch(r" {0,3}([`~]+)[ \t]*", line)
            if closing and closing.group(1)[0] == fence[0] and len(closing.group(1)) >= fence[1]:
                fence = None
            visible.append((number, ""))
            continue
        indented_code = markdown_indent_width(line) >= 4
        if indented_code:
            if "<!--" in line:
                ambiguous = True
            visible.append((number, ""))
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if opening:
            marker = opening.group(1)
            if marker[0] == "`" and "`" in line[opening.end():]:
                ambiguous = True
                visible.append((number, line))
                continue
            fence = (marker[0], len(marker))
            visible.append((number, ""))
            continue
        masked, _ = mask_inline_code(line)
        if "<!--" in line and "<!--" not in masked:
            ambiguous = True
        if re.fullmatch(r" {0,3}</?[A-Za-z][A-Za-z0-9-]*(?:\s[^>]*)?>\s*", masked):
            ambiguous = True
        if "<!--" in masked:
            prefix, remainder = masked.split("<!--", 1)
            if prefix.strip():
                ambiguous = True
            if "-->" in remainder:
                if remainder.split("-->", 1)[1].strip():
                    ambiguous = True
                comment = False
            else:
                comment = True
            visible.append((number, ""))
            continue
        visible.append((number, line))
    return visible, fence is None and not comment, ambiguous


def markdown_block_context_balanced(text: str) -> bool:
    _, balanced, ambiguous = scan_markdown_lines(text)
    return balanced and not ambiguous


def markdown_indent_width(line: str) -> int:
    width = 0
    for character in line:
        if character == " ":
            width += 1
        elif character == "\t":
            width += 4 - (width % 4)
        else:
            break
    return width


def links_outside_code(text: str) -> tuple[list[re.Match[str]], bool]:
    """Find Markdown links outside inline code spans."""
    masked, balanced = mask_inline_code(text)
    return list(LINK_RE.finditer(masked)), balanced


def multiline_inline_link_syntax(text: str) -> bool:
    """Fail closed when an inline link or image crosses a physical line."""
    masked, _ = mask_inline_code(text)
    return bool(
        re.search(r"!?\[[^\]]*\n[^\]]*\]\s*\(", masked)
        or re.search(r"!?\[[^\]]*\]\([^)]*\n[^)]*\)", masked)
    )


def mask_inline_code(text: str) -> tuple[str, bool]:
    masked: list[str] = []
    delimiter: int | None = None
    index = 0
    while index < len(text):
        character = text[index]
        if character == "`":
            end = index
            while end < len(text) and text[end] == "`":
                end += 1
            run_length = end - index
            preceding_slashes = 0
            cursor = index - 1
            while cursor >= 0 and text[cursor] == "\\":
                preceding_slashes += 1
                cursor -= 1
            if preceding_slashes % 2:
                masked.extend(" " * run_length if delimiter is not None else "`" * run_length)
                index = end
                continue
            if delimiter is None:
                delimiter = run_length
            elif delimiter == run_length:
                delimiter = None
            else:
                return text, False
            masked.extend(" " * run_length)
            index = end
        else:
            masked.append(" " if delimiter is not None else character)
            index += 1
    if delimiter is not None:
        return text, False
    return "".join(masked), True
