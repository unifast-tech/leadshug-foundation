import hashlib
import io
import tempfile
import unittest
from contextlib import redirect_stdout
import os
import subprocess
import sys
from pathlib import Path

from foundation_lifecycle.parser import validate_root
from validate_foundation_lifecycle import main

def write_tree(root: Path):
    (root/"backlog").mkdir(); (root/"decisions").mkdir(); (root/"modules").mkdir(); (root/"todos/completed").mkdir(parents=True)
    (root/"modules/core.md").write_text("x"); (root/"todos/completed/done.md").write_text("x")
    (root/"evolution_lifecycle.md").write_text("""## Immutable identifiers
`BLG-<slug>` `CAP-<slug>` `DEC-<slug>`
## Authority matrix
| Field / truth | Canonical owner | Other surfaces |
| --- | --- | --- |
## State machines
### Candidates
**Schema:** immutable ID; title; state; source/evidence link; value/risk; dependencies; disposition owner; next gate.
**Enum:** `Proposed|Under-Review|Selected-for-Planning|Deferred|Rejected`
| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
### Capabilities
**Schema:** immutable ID; module owner; state; evidence; dependency links; intended outcome; retirement rationale when applicable.
**Enum:** `Not-Assessed|Discovery|Planned|In-Progress|Delivered|Retired`
| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
### Tactical TODOs
**Schema:** immutable TODO path/identity; objective; scope; state; approval evidence; owner; validation/evidence; delivery disposition.
**Enum:** `Draft|Review|Approved|In-Progress|Completed|Cancelled`
| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
### Decisions
**Schema:** immutable ID; question; alternatives; rationale; provenance/evidence; state; named canonical targets; target-consolidation evidence; supersession link when applicable.
**Enum:** `Proposed|Accepted|Superseded|Rejected`
| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
### Contract verification
**Schema:** contract reference; responsible module; state; evidence link; verification scope; deprecation successor when applicable.
**Enum:** `Not-Assessed|Documented|Verified|Deprecated`
| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |""")
    (root/"backlog/README.md").write_text("## Candidates\n| Immutable ID | Title | State | Source / evidence | Value / risk | Dependencies | Disposition owner | Next gate |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n| BLG-x | x | Proposed | [x](../evolution_lifecycle.md) | x | x | x | x |")
    (root/"decisions/README.md").write_text("## Records\n- [x](x.md)")
    (root/"decisions/x.md").write_text("**Provenance:** x\n| Immutable ID | State | Question and accepted direction | Alternatives considered / rationale | Named canonical targets | Target-consolidation evidence |\n| --- | --- | --- | --- | --- | --- |\n| DEC-x | Accepted | x | x | `evolution_lifecycle.md` | `evolution_lifecycle.md` x |")
    (root/"system_roadmap.md").write_text("# LeadsHug — System Roadmap\n| Phase / theme | Horizon | Gate status | Dependencies | Expected outcome | Exit gate |\n| --- | --- | --- | --- | --- | --- |\n| x | Now | Exit-Gate-Met | x | x | [m](modules/core.md); [t](todos/completed/done.md) |")


def manifest(root: Path):
    return {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(root.rglob("*")) if path.is_file()}


class ValidatorCliTests(unittest.TestCase):
    def test_returns_zero_and_never_writes_successful_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_tree(root)
            before = manifest(root)
            with redirect_stdout(io.StringIO()):
                self.assertEqual(0, main(["--root", str(root)]))
            self.assertEqual(before, manifest(root))

    def test_caps_diagnostics_and_reports_omitted_count(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_tree(root)
            path = root / "backlog" / "README.md"
            row = "| bad | SENSITIVE_UNIQUE_CELL | wrong | [source](https://invalid) | value | none | owner | next |\n"
            path.write_text(path.read_text(encoding="utf-8") + row * 120, encoding="utf-8")
            findings = validate_root(root)
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(1, main(["--root", str(root)]))
            lines = output.getvalue().splitlines()
            self.assertEqual(101, len(lines))
            self.assertEqual(f"<root>:summary: FINDINGS_OMITTED_{len(findings) - 100}", lines[-1])
            self.assertNotIn("SENSITIVE_UNIQUE_CELL", output.getvalue())
            self.assertNotIn(str(root), output.getvalue())

    def test_cli_rejects_external_link_anywhere_in_decision_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_tree(root)
            path = root / "decisions" / "README.md"
            path.write_text("[external](https://example.invalid)\n" + path.read_text(encoding="utf-8"), encoding="utf-8")
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(1, main(["--root", str(root)]))
            self.assertIn("LINK_DESTINATION", output.getvalue())

    def test_cli_rejects_unindexed_external_decision_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "root"
            root.mkdir()
            write_tree(root)
            outside = Path(directory) / "outside.md"
            outside.write_text("outside", encoding="utf-8")
            (root / "decisions" / "rogue.md").symlink_to(outside)
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(1, main(["--root", str(root)]))
            self.assertIn("DECISION_MEMBERSHIP", output.getvalue())
            self.assertIn("LINK_CONFINEMENT", output.getvalue())

    def test_cli_redacts_control_characters_from_discovered_paths(self):
        cases = (
            ("newline", "rogue\nINJECTED.md", "INJECTED", None),
            ("ansi", "rogue\x1b[31m.md", "\x1b", None),
            ("raw-byte", None, os.fsdecode(b"\xff"), b"rogue-\xff.md"),
        )
        for label, name, forbidden, raw_name in cases:
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory) / "root"
                root.mkdir()
                write_tree(root)
                outside = Path(directory) / "outside.md"
                outside.write_text("outside", encoding="utf-8")
                if raw_name is None:
                    (root / "decisions" / name).symlink_to(outside)
                else:
                    os.symlink(os.fsencode(outside), os.fsencode(root / "decisions") + b"/" + raw_name)
                output = io.StringIO()
                with redirect_stdout(output):
                    self.assertEqual(1, main(["--root", str(root)]))
                rendered = output.getvalue()
                self.assertIn("<unsafe-path>", rendered)
                self.assertNotIn(forbidden, rendered)
                self.assertLessEqual(len(rendered.splitlines()), 101)

    def test_cli_rejects_bare_records_entry(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_tree(root)
            path = root / "decisions" / "README.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nexample.md\n", encoding="utf-8")
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(1, main(["--root", str(root)]))
            self.assertIn("DECISION_MEMBERSHIP", output.getvalue())

    def test_real_repository_acceptance(self):
        root = Path(__file__).resolve().parents[2]
        with redirect_stdout(io.StringIO()):
            self.assertEqual(0, main(["--root", str(root)]))

    def test_entrypoint_creates_no_bytecode(self):
        root = Path(__file__).resolve().parents[2]
        env = dict(os.environ, PYTHONPATH=str(root / "deterministic"), PYTHONDONTWRITEBYTECODE="")
        result = subprocess.run([sys.executable, str(root / "deterministic" / "validate_foundation_lifecycle.py"), "--root", str(root)], env=env, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)
        self.assertEqual([], list((root / "deterministic").rglob("*.pyc")))

    def test_returns_nonzero_and_never_writes_invalid_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_tree(root)
            path = root / "system_roadmap.md"
            path.write_text(path.read_text(encoding="utf-8").replace("modules/core.md", "../escape.md"), encoding="utf-8")
            before = manifest(root)
            with redirect_stdout(io.StringIO()):
                self.assertEqual(1, main(["--root", str(root)]))
            self.assertEqual(before, manifest(root))
