import shutil
import tempfile
import unittest
from pathlib import Path

from foundation_lifecycle.parser import validate_root


def write_tree(root: Path, *, backlog_id="BLG-example", decision_id="DEC-example"):
    (root / "backlog").mkdir(parents=True)
    (root / "decisions").mkdir()
    (root / "modules").mkdir()
    (root / "todos" / "completed").mkdir(parents=True)
    (root / "modules" / "core.md").write_text("# Core\n", encoding="utf-8")
    (root / "todos" / "completed" / "done.md").write_text("# Done\n", encoding="utf-8")
    (root / "evolution_lifecycle.md").write_text("""# Lifecycle

## Immutable identifiers

`BLG-<slug>`, `CAP-<slug>` and `DEC-<slug>`.

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
| --- | --- | --- | --- |
""", encoding="utf-8")
    (root / "backlog" / "README.md").write_text(f"""# Backlog

## Candidates

| Immutable ID | Title | State | Source / evidence | Value / risk | Dependencies | Disposition owner | Next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {backlog_id} | Example | Proposed | [source](../evolution_lifecycle.md) | value | none | owner | next |
""", encoding="utf-8")
    (root / "decisions" / "README.md").write_text("""# Decisions

## Records

- [Example](example.md)
""", encoding="utf-8")
    (root / "decisions" / "example.md").write_text(f"""# Example

**Provenance:** fixture

| Immutable ID | State | Question and accepted direction | Alternatives considered / rationale | Named canonical targets | Target-consolidation evidence |
| --- | --- | --- | --- | --- | --- |
| {decision_id} | Accepted | direction | rationale | `evolution_lifecycle.md` | `evolution_lifecycle.md` evidence |
""", encoding="utf-8")
    (root / "system_roadmap.md").write_text("""# LeadsHug — System Roadmap

| Phase / theme | Horizon | Gate status | Dependencies | Expected outcome | Exit gate |
| --- | --- | --- | --- | --- | --- |
| Phase | Now | Exit-Gate-Met | none | outcome | [module](modules/core.md); [todo](todos/completed/done.md) |
""", encoding="utf-8")


class FoundationParserTests(unittest.TestCase):
    def fixture(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        write_tree(root)
        return temp, root

    def test_accepts_independent_valid_fixture(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        self.assertEqual([], validate_root(root))

    def test_rejects_duplicate_backlog_id(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        original = path.read_text(encoding="utf-8")
        row = "| BLG-example | Example | Proposed | [source](../evolution_lifecycle.md) | value | none | owner | next |\n"
        path.write_text(original + row, encoding="utf-8")
        self.assertTrue(any(f.rule == "ID_DUPLICATE" for f in validate_root(root)))

    def test_rejects_escaped_link_target(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("../evolution_lifecycle.md", "https://example.invalid"), encoding="utf-8")
        self.assertTrue(any(f.rule == "LINK_DESTINATION" for f in validate_root(root)))

    def test_rejects_missing_heading_and_table_schema(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        lifecycle = root / "evolution_lifecycle.md"
        lifecycle.write_text(lifecycle.read_text(encoding="utf-8").replace("## State machines", "## States"), encoding="utf-8")
        backlog = root / "backlog" / "README.md"
        backlog.write_text(backlog.read_text(encoding="utf-8").replace("| Title |", "| Name |"), encoding="utf-8")
        rules = {finding.rule for finding in validate_root(root)}
        self.assertIn("HEADING_REQUIRED", rules)
        self.assertIn("TABLE_REQUIRED", rules)

    def test_rejects_table_row_cardinality_change(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| owner | next |", "| owner | next | extra |"), encoding="utf-8")
        self.assertIn("TABLE_ROW", {finding.rule for finding in validate_root(root)})

    def test_canonical_tables_reject_outerless_gfm_data_rows(self):
        cases = (
            (
                "backlog/README.md",
                "| BLG-example | Example | Proposed | [source](../evolution_lifecycle.md) | value | none | owner | next |",
                "INVALID-ID | Example | Invalid-State | [source](../evolution_lifecycle.md) | value | none | owner | next",
            ),
            (
                "decisions/example.md",
                "| DEC-example | Accepted | direction | rationale | `evolution_lifecycle.md` | `evolution_lifecycle.md` evidence |",
                "DEC-example | Invalid-State | direction | rationale | `evolution_lifecycle.md` | `evolution_lifecycle.md` evidence",
            ),
            (
                "system_roadmap.md",
                "| Phase | Now | Exit-Gate-Met | none | outcome | [module](modules/core.md); [todo](todos/completed/done.md) |",
                "Phase | Now | Exit-Gate-Met | none | outcome | no evidence",
            ),
        )
        for relative, canonical, outerless in cases:
            with self.subTest(relative=relative), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / relative
                path.write_text(path.read_text(encoding="utf-8").replace(canonical, outerless), encoding="utf-8")
                self.assertIn("TABLE_ROW", {finding.rule for finding in validate_root(root)})

    def test_outerless_duplicate_canonical_table_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\nImmutable ID | Title | State | Source / evidence | Value / risk | Dependencies | Disposition owner | Next gate\n"
            + "--- | --- | --- | --- | --- | --- | --- | ---\n"
            + "BLG-second | Second | Proposed | [source](../evolution_lifecycle.md) | value | none | owner | next\n",
            encoding="utf-8",
        )
        self.assertIn("TABLE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_escaped_backticks_cannot_hide_extra_table_cell(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("| owner | next |", r"| owner \` | \` next | extra |"),
            encoding="utf-8",
        )
        self.assertIn("TABLE_ROW", {finding.rule for finding in validate_root(root)})

    def test_raw_pipe_inside_inline_code_is_still_a_table_delimiter(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| Example |", "| `foo|bar` |"), encoding="utf-8")
        self.assertIn("TABLE_ROW", {finding.rule for finding in validate_root(root)})

    def test_escaped_pipe_inside_inline_code_remains_one_cell(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| Example |", r"| `foo\|bar` |"), encoding="utf-8")
        self.assertEqual([], validate_root(root))

    def test_inline_code_cannot_span_table_cells_and_hide_external_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        valid_row = "| BLG-example | Example | Proposed | [source](../evolution_lifecycle.md) | value | none | owner | next |"
        exploit = "| BLG-example | `open | Proposed | [source](https://example.invalid) | close` | none | owner | next |"
        path.write_text(path.read_text(encoding="utf-8").replace(valid_row, exploit), encoding="utf-8")
        self.assertIn("TABLE_ROW", {finding.rule for finding in validate_root(root)})

    def test_cross_cell_code_span_in_extra_table_cannot_hide_external_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\n| a | b | c |\n| --- | --- | --- |\n| `open | [external](https://example.invalid) | close` |\n",
            encoding="utf-8",
        )
        self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_cross_cell_code_span_in_extra_table_without_outer_pipes_cannot_hide_external_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\na | b | c\n--- | --- | ---\n`open | [external](https://example.invalid) | close`\n",
            encoding="utf-8",
        )
        self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_balanced_inline_code_within_one_table_cell_is_valid(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| Example |", "| `Example` |"), encoding="utf-8")
        self.assertEqual([], validate_root(root))

    def test_rejects_invalid_ids_and_duplicate_decision_id(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        backlog = root / "backlog" / "README.md"
        backlog.write_text(backlog.read_text(encoding="utf-8").replace("BLG-example", "BLG-Invalid"), encoding="utf-8")
        decision = root / "decisions" / "example.md"
        row = "| DEC-example | Accepted | direction | rationale | `evolution_lifecycle.md` | `evolution_lifecycle.md` evidence |\n"
        decision.write_text(decision.read_text(encoding="utf-8") + row, encoding="utf-8")
        rules = {finding.rule for finding in validate_root(root)}
        self.assertIn("ID_INVALID", rules)
        self.assertIn("ID_DUPLICATE", rules)

    def test_rejects_stale_and_orphan_decision_membership(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        (root / "decisions" / "orphan.md").write_text("# orphan\n", encoding="utf-8")
        index = root / "decisions" / "README.md"
        index.write_text(index.read_text(encoding="utf-8").replace("example.md", "missing.md"), encoding="utf-8")
        rules = {finding.rule for finding in validate_root(root)}
        self.assertIn("DECISION_MEMBERSHIP", rules)
        self.assertIn("LINK_MISSING", rules)

    def test_rejects_duplicate_decision_index_entry(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "README.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n- [Duplicate](example.md)\n", encoding="utf-8")
        self.assertIn("DECISION_MEMBERSHIP", {finding.rule for finding in validate_root(root)})

    def test_rejects_invalid_state_and_hidden_unicode(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| Proposed |", "| proposed\u200b |"), encoding="utf-8")
        self.assertTrue(any(f.rule == "STATE_INVALID" for f in validate_root(root)))

    def test_decision_and_roadmap_state_rules_have_independent_mutations(self):
        cases = (
            ("decision", "| DEC-example | Accepted |", "| DEC-example | Unknown |"),
            ("roadmap", "| Phase | Now | Exit-Gate-Met |", "| Phase | Now | Unknown |"),
        )
        for owner, needle, replacement in cases:
            with self.subTest(owner=owner), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / ("decisions/example.md" if owner == "decision" else "system_roadmap.md")
                path.write_text(path.read_text(encoding="utf-8").replace(needle, replacement), encoding="utf-8")
                self.assertIn("STATE_INVALID", {finding.rule for finding in validate_root(root)})

    def test_open_roadmap_state_is_a_positive_control(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "system_roadmap.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace("| Phase | Now | Exit-Gate-Met |", "| Phase | Now | Open |")
        text = text.replace("[module](modules/core.md); [todo](todos/completed/done.md)", "not gated")
        path.write_text(text, encoding="utf-8")
        self.assertEqual([], validate_root(root))

    def test_proposed_decision_requires_pending_evidence(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| DEC-example | Accepted |", "| DEC-example | Proposed |"), encoding="utf-8")
        self.assertIn("EVIDENCE_SHAPE", {finding.rule for finding in validate_root(root)})

    def test_proposed_decision_with_pending_evidence_is_valid(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace("| DEC-example | Accepted |", "| DEC-example | Proposed |")
        text = text.replace("`evolution_lifecycle.md` evidence", "PENDING")
        path.write_text(text, encoding="utf-8")
        self.assertEqual([], validate_root(root))

    def test_rejected_decision_concrete_evidence_must_name_its_target(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace("| DEC-example | Accepted |", "| DEC-example | Rejected |")
        text = text.replace("`evolution_lifecycle.md` evidence", "unbound evidence")
        path.write_text(text, encoding="utf-8")
        self.assertIn("EVIDENCE_SHAPE", {finding.rule for finding in validate_root(root)})

    def test_terminal_decision_states_accept_supported_evidence_forms(self):
        cases = (
            ("Accepted", "PENDING"),
            ("Rejected", "PENDING"),
            ("Rejected", "`evolution_lifecycle.md` rejection evidence"),
            ("Superseded", "PENDING"),
            ("Superseded", "`evolution_lifecycle.md` supersession evidence"),
        )
        for state, evidence in cases:
            with self.subTest(state=state, evidence=evidence), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "decisions" / "example.md"
                text = path.read_text(encoding="utf-8")
                text = text.replace("| DEC-example | Accepted |", f"| DEC-example | {state} |")
                text = text.replace("`evolution_lifecycle.md` evidence", evidence)
                path.write_text(text, encoding="utf-8")
                self.assertEqual([], validate_root(root))

    def test_rejects_unsafe_link_forms_and_escape(self):
        for target in ("/tmp/x", "x%20y", "x\\y", "../../escape.md", "file:///tmp/x", "evolution_lifecycle.md#Bad_Fragment"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "backlog" / "README.md"
                path.write_text(path.read_text(encoding="utf-8").replace("../evolution_lifecycle.md", target), encoding="utf-8")
                self.assertTrue(any(f.rule in {"LINK_DESTINATION", "LINK_CONFINEMENT"} for f in validate_root(root)))

    def test_rejects_symlink_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "foundation"
            root.mkdir()
            write_tree(root)
            outside = Path(directory) / "outside.md"
            outside.write_text("outside", encoding="utf-8")
            (root / "backlog" / "escape.md").symlink_to(outside)
            path = root / "backlog" / "README.md"
            path.write_text(path.read_text(encoding="utf-8").replace("../evolution_lifecycle.md", "escape.md"), encoding="utf-8")
            self.assertIn("LINK_CONFINEMENT", {finding.rule for finding in validate_root(root)})

    def test_paths_cannot_leave_lexical_root_and_reenter_through_symlink(self):
        cases = (
            (
                "backlog/README.md",
                "../evolution_lifecycle.md",
                "../../reentry/evolution_lifecycle.md",
                "reentry",
                ".",
            ),
            (
                "decisions/README.md",
                "example.md",
                "../../reentry/decisions/example.md",
                "reentry",
                ".",
            ),
            (
                "system_roadmap.md",
                "modules/core.md",
                "../module-reentry/core.md",
                "module-reentry",
                "modules",
            ),
        )
        for relative, needle, destination, symlink_name, symlink_target in cases:
            with self.subTest(relative=relative), tempfile.TemporaryDirectory() as directory:
                root = Path(directory) / "root"
                root.mkdir()
                write_tree(root)
                (Path(directory) / symlink_name).symlink_to(root / symlink_target, target_is_directory=True)
                path = root / relative
                path.write_text(path.read_text(encoding="utf-8").replace(needle, destination, 1), encoding="utf-8")
                self.assertIn("LINK_CONFINEMENT", {finding.rule for finding in validate_root(root)})

    def test_rejects_symlink_loop_as_confined_finding(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "foundation"
            root.mkdir()
            write_tree(root)
            loop = root / "backlog" / "loop.md"
            loop.symlink_to(loop)
            path = root / "backlog" / "README.md"
            path.write_text(path.read_text(encoding="utf-8").replace("../evolution_lifecycle.md", "loop.md"), encoding="utf-8")
            self.assertIn("LINK_CONFINEMENT", {finding.rule for finding in validate_root(root)})

    def test_rejects_evidence_shape_and_roadmap_target_classes(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        decision = root / "decisions" / "example.md"
        decision.write_text(decision.read_text(encoding="utf-8").replace("`evolution_lifecycle.md` evidence", "PENDING; PENDING"), encoding="utf-8")
        roadmap = root / "system_roadmap.md"
        roadmap.write_text(roadmap.read_text(encoding="utf-8").replace("[todo](todos/completed/done.md)", "[wrong](evolution_lifecycle.md)"), encoding="utf-8")
        rules = {finding.rule for finding in validate_root(root)}
        self.assertIn("EVIDENCE_SHAPE", rules)
        self.assertIn("ROADMAP_EVIDENCE", rules)

    def test_rejects_missing_or_duplicate_provenance(self):
        for replacement in ("", "**Provenance:** fixture\n**Provenance:** second\n"):
            with self.subTest(replacement=replacement), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "decisions" / "example.md"
                path.write_text(path.read_text(encoding="utf-8").replace("**Provenance:** fixture\n", replacement), encoding="utf-8")
                self.assertTrue(any(f.rule == "PROVENANCE_SCHEMA" for f in validate_root(root)))

    def test_bootstrap_owner_schema_and_enum_mutations_fail(self):
        for mutation in ("owner", "schema", "enum"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                if mutation == "owner":
                    (root / "system_roadmap.md").unlink()
                else:
                    path = root / "evolution_lifecycle.md"
                    needle = "immutable ID; title; state" if mutation == "schema" else "Proposed|Under-Review|Selected-for-Planning|Deferred|Rejected"
                    path.write_text(path.read_text(encoding="utf-8").replace(needle, "removed"), encoding="utf-8")
                expected = "OWNER_MISSING" if mutation == "owner" else "BOOTSTRAP_REQUIRED"
                self.assertIn(expected, {finding.rule for finding in validate_root(root)})

    def test_bootstrap_schema_and_enum_labels_are_required(self):
        for label in ("**Schema:**", "**Enum:**"):
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8").replace(label, "", 1), encoding="utf-8")
                self.assertIn("BOOTSTRAP_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_bootstrap_fields_must_belong_to_their_sections(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        text = path.read_text(encoding="utf-8")
        candidate = "**Schema:** immutable ID; title; state; source/evidence link; value/risk; dependencies; disposition owner; next gate."
        decision = "**Schema:** immutable ID; question; alternatives; rationale; provenance/evidence; state; named canonical targets; target-consolidation evidence; supersession link when applicable."
        path.write_text(text.replace(candidate, "SWAP", 1).replace(decision, candidate, 1).replace("SWAP", decision, 1), encoding="utf-8")
        self.assertIn("BOOTSTRAP_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_identifier_grammar_must_belong_to_immutable_section(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        text = path.read_text(encoding="utf-8")
        declaration = "`BLG-<slug>`, `CAP-<slug>` and `DEC-<slug>`."
        path.write_text(text.replace(declaration, "Identifiers are declared below.", 1) + "\n" + declaration + "\n", encoding="utf-8")
        self.assertIn("BOOTSTRAP_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_all_lifecycle_state_machine_contracts_are_bootstrapped(self):
        mutations = (
            "### Capabilities",
            "**Enum:** `Not-Assessed|Discovery|Planned|In-Progress|Delivered|Retired`",
            "### Tactical TODOs",
            "**Enum:** `Draft|Review|Approved|In-Progress|Completed|Cancelled`",
            "### Contract verification",
            "**Enum:** `Not-Assessed|Documented|Verified|Deprecated`",
        )
        for value in mutations:
            with self.subTest(value=value), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8").replace(value, "removed", 1), encoding="utf-8")
                rules = {finding.rule for finding in validate_root(root)}
                expected = "HEADING_REQUIRED" if value.startswith("###") else "BOOTSTRAP_REQUIRED"
                self.assertIn(expected, rules)

    def test_authority_and_transition_table_schemas_are_required(self):
        for header in ("| Field / truth | Canonical owner | Other surfaces |", "| From | Actor / evidence | To | Rule |"):
            with self.subTest(header=header), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8").replace(header, header.replace("Rule", "Wrong").replace("Other surfaces", "Wrong"), 1), encoding="utf-8")
                self.assertIn("TABLE_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_fenced_bootstrap_contract_is_not_admitted(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text("```md\n" + path.read_text(encoding="utf-8") + "```\n", encoding="utf-8")
        rules = {finding.rule for finding in validate_root(root)}
        self.assertIn("HEADING_REQUIRED", rules)
        self.assertIn("BOOTSTRAP_REQUIRED", rules)

    def test_fenced_backlog_table_is_not_admitted(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        text = path.read_text(encoding="utf-8")
        table = text[text.index("|"):]
        path.write_text(text[:text.index("|")] + "```md\n" + table + "```\n", encoding="utf-8")
        self.assertIn("TABLE_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_html_commented_backlog_table_is_not_admitted(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        text = path.read_text(encoding="utf-8")
        table = text[text.index("|"):]
        path.write_text(text[:text.index("|")] + "<!--\n" + table + "-->\n", encoding="utf-8")
        self.assertIn("TABLE_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_raw_html_block_around_table_fails_closed(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        text = path.read_text(encoding="utf-8")
        table = text[text.index("|"):]
        path.write_text(text[:text.index("|")] + "<pre>\n" + table + "</pre>\n", encoding="utf-8")
        self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_unsupported_raw_angle_syntax_fails_closed(self):
        for syntax in (
            "<?validation",
            "<![CDATA[",
            "<!VALIDATION",
            "<div",
            "<person@example.invalid>",
            '<a href="https://example.invalid">external</a>',
        ):
            with self.subTest(syntax=syntax), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8") + "\n" + syntax + "\n", encoding="utf-8")
                self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_unclosed_html_comment_fails_closed(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n<!-- unclosed\n", encoding="utf-8")
        self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_comment_marker_in_code_cannot_hide_duplicate_table(self):
        for marker in ("    <!--", "`<!--`"):
            with self.subTest(marker=marker), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "backlog" / "README.md"
                text = path.read_text(encoding="utf-8")
                table = text[text.index("|"):]
                path.write_text(text + f"\n{marker}\n" + table + "-->\n", encoding="utf-8")
                rules = {finding.rule for finding in validate_root(root)}
                self.assertIn("MARKDOWN_AMBIGUOUS", rules)
                self.assertIn("TABLE_SCHEMA", rules)

    def test_same_line_comment_cannot_hide_adjacent_links(self):
        for line in (
            "[external](https://example.invalid) <!-- note -->",
            "<!-- note --> [external](https://example.invalid)",
        ):
            with self.subTest(line=line), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8") + "\n" + line + "\n", encoding="utf-8")
                self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_shorter_fence_does_not_close_longer_fence(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        text = path.read_text(encoding="utf-8")
        table = text[text.index("|"):]
        path.write_text(text[:text.index("|")] + "````md\n```\n" + table + "````\n", encoding="utf-8")
        self.assertIn("TABLE_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_backtick_in_fence_info_fails_closed(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\n```bad`info\n[external](https://example.invalid)\n```\n",
            encoding="utf-8",
        )
        rules = {finding.rule for finding in validate_root(root)}
        self.assertIn("MARKDOWN_AMBIGUOUS", rules)
        self.assertIn("LINK_DESTINATION", rules)

    def test_indented_roadmap_table_is_not_admitted(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "system_roadmap.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(("    " + line) if line.startswith("|") else line for line in lines) + "\n", encoding="utf-8")
        self.assertIn("TABLE_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_mixed_space_tab_indented_table_is_not_admitted(self):
        for prefix in (" \t", "  \t", "   \t"):
            with self.subTest(prefix=repr(prefix)), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "backlog" / "README.md"
                lines = path.read_text(encoding="utf-8").splitlines()
                path.write_text("\n".join((prefix + line) if line.startswith("|") else line for line in lines) + "\n", encoding="utf-8")
                self.assertIn("TABLE_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_indented_decision_table_is_not_admitted(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(("    " + line) if line.startswith("|") else line for line in lines) + "\n", encoding="utf-8")
        self.assertIn("TABLE_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_superseded_and_accepted_evidence_require_real_suffix(self):
        for state, evidence in (("Superseded", "anything"), ("Accepted", "`evolution_lifecycle.md`")):
            with self.subTest(state=state), tempfile.TemporaryDirectory() as directory:
                root = Path(directory); write_tree(root)
                path = root / "decisions" / "example.md"
                text = path.read_text(encoding="utf-8").replace("Accepted", state, 1).replace("`evolution_lifecycle.md` evidence", evidence)
                path.write_text(text, encoding="utf-8")
                self.assertTrue(any(item.rule == "EVIDENCE_SHAPE" for item in validate_root(root)))

    def test_rejects_canonical_scheme_and_invalid_live_owner(self):
        temp, root = self.fixture(); self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("`evolution_lifecycle.md`", "`https:evil`", 1), encoding="utf-8")
        (root / "backlog" / "README.md").write_bytes(b"\xff")
        rules = {item.rule for item in validate_root(root)}
        self.assertIn("LINK_DESTINATION", rules)
        self.assertIn("UTF8_INVALID", rules)

    def test_history_is_not_an_owner(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        (root / "todos" / "completed" / "history.md").write_bytes(b"\xff")
        self.assertEqual([], validate_root(root))

    def test_diagnostics_are_sorted_and_redacted(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        (root / "backlog" / "README.md").write_text("# Backlog\n", encoding="utf-8")
        findings = validate_root(root)
        rendered = [finding.render() for finding in findings]
        self.assertEqual(rendered, sorted(rendered))
        self.assertNotIn("Backlog", "\n".join(rendered))

    def test_cross_file_duplicate_dec_is_global_when_both_indexed(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        second = root / "decisions" / "second.md"
        second.write_text((root / "decisions" / "example.md").read_text(encoding="utf-8"), encoding="utf-8")
        (root / "decisions" / "README.md").write_text(
            "# Decisions\n\n## Records\n\n- [one](example.md)\n- [two](second.md)\n",
            encoding="utf-8",
        )
        self.assertIn("ID_DUPLICATE", {finding.rule for finding in validate_root(root)})

    def test_malformed_decision_divider_is_rejected_in_isolation(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "| --- | --- | --- | --- | --- | --- |",
                "| invalid | --- | --- | --- | --- | --- |",
            ),
            encoding="utf-8",
        )
        self.assertIn("TABLE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_duplicate_decision_table_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text + text[text.index("|"):], encoding="utf-8")
        self.assertIn("TABLE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_duplicate_backlog_table_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text + text[text.index("|"):], encoding="utf-8")
        self.assertIn("TABLE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_duplicate_roadmap_table_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "system_roadmap.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text + text[text.index("|"):], encoding="utf-8")
        self.assertIn("TABLE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_backlog_source_requires_exactly_one_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "[source](../evolution_lifecycle.md)",
                "[a](../evolution_lifecycle.md) [b](../evolution_lifecycle.md)",
            ),
            encoding="utf-8",
        )
        self.assertIn("LINK_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_unicode_u2066_in_state_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| Proposed |", "| Proposed\u2066 |"), encoding="utf-8")
        self.assertIn("STATE_INVALID", {finding.rule for finding in validate_root(root)})

    def test_records_section_rejects_non_decision_owner_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "README.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n- [bad](../todos/completed/done.md)\n", encoding="utf-8")
        self.assertIn("DECISION_MEMBERSHIP", {finding.rule for finding in validate_root(root)})

    def test_query_link_destination_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("../evolution_lifecycle.md", "../evolution_lifecycle.md?q=1"), encoding="utf-8")
        self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_unbalanced_inline_code_cannot_hide_external_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n`broken [external](https://example.invalid)\n", encoding="utf-8")
        self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_escaped_backticks_cannot_hide_external_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n\\` [external](https://example.invalid) \\`\n", encoding="utf-8")
        self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_mismatched_inline_code_runs_cannot_hide_external_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n` [external](https://example.invalid) ```\n", encoding="utf-8")
        rules = {finding.rule for finding in validate_root(root)}
        self.assertIn("MARKDOWN_AMBIGUOUS", rules)
        self.assertIn("LINK_DESTINATION", rules)

    def test_reference_style_link_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[external][ref]\n[ref]: https://example.invalid\n", encoding="utf-8")
        self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_reference_definitions_inside_list_containers_are_rejected(self):
        for definition in (
            "- [foo]: ../../outside.md",
            "1. [foo]: ../../outside.md",
            "- 1. [foo]: ../../outside.md",
            "- [foo]:\n    ../../outside.md",
        ):
            with self.subTest(definition=definition), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(
                    path.read_text(encoding="utf-8") + f"\n[foo]\n\n{definition}\n",
                    encoding="utf-8",
                )
                self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_external_autolinks_are_rejected(self):
        for autolink in ("<https://example.invalid>", "<mailto:test@example.invalid>"):
            with self.subTest(autolink=autolink), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8") + f"\n{autolink}\n", encoding="utf-8")
                self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_gfm_extended_autolinks_are_rejected_with_punctuation_boundaries(self):
        for autolink in (
            "See https://example.invalid/path.",
            "See (www.example.invalid/path).",
            "Contact test.user+tag@example.invalid, now.",
        ):
            with self.subTest(autolink=autolink), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8") + f"\n{autolink}\n", encoding="utf-8")
                self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_gfm_extended_autolink_text_inside_code_is_not_a_link(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\n`https://example.invalid/path` `www.example.invalid` `test@example.invalid`\n",
            encoding="utf-8",
        )
        self.assertEqual([], validate_root(root))

    def test_external_image_destinations_are_rejected(self):
        for image in ("![x](https://example.invalid/image.png)", "\\![x](https://example.invalid/image.png)"):
            with self.subTest(image=image), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8") + f"\n{image}\n", encoding="utf-8")
                self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_unsupported_inline_link_labels_fail_closed(self):
        for link in ("[nested [label]](https://example.invalid)", r"[escaped \] label](https://example.invalid)"):
            with self.subTest(link=link), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8") + f"\n{link}\n", encoding="utf-8")
                self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_unsupported_destination_whitespace_parentheses_and_titles_are_rejected(self):
        for destination in ("space target.md", "target(foo.md", 'target.md "title"'):
            with self.subTest(destination=destination), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8") + f"\n[local]({destination})\n", encoding="utf-8")
                self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_character_references_cannot_encode_forbidden_destinations(self):
        for destination in (
            "..&sol;..&sol;outside.md",
            "https&colon;//example.invalid",
            "target.md&quest;x=1",
            "target&percnt;20name.md",
        ):
            with self.subTest(destination=destination), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "backlog" / "README.md"
                path.write_text(path.read_text(encoding="utf-8").replace("../evolution_lifecycle.md", destination), encoding="utf-8")
                self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_multiline_links_and_images_are_rejected(self):
        for markup in (
            "[escape](\n../../outside.md)",
            "[escape](\n/etc/passwd)",
            "[escape](\n//example.invalid/path)",
            "![escape](\n../../outside.png)",
            "[escape\nlabel](../../outside.md)",
        ):
            with self.subTest(markup=markup), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "evolution_lifecycle.md"
                path.write_text(path.read_text(encoding="utf-8") + f"\n{markup}\n", encoding="utf-8")
                self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_multiline_code_span_is_rejected_as_ambiguous(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\n`[example](\n../../outside.md)`\n",
            encoding="utf-8",
        )
        self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_non_commonmark_line_separators_are_rejected(self):
        for separator in ("\x0b", "\x0c", "\x1c", "\x1d", "\x1e", "\x85", "\u2028", "\u2029"):
            with self.subTest(separator=repr(separator)), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "backlog" / "README.md"
                path.write_text(path.read_text(encoding="utf-8").replace("\n", separator), encoding="utf-8")
                self.assertIn("MARKDOWN_AMBIGUOUS", {finding.rule for finding in validate_root(root)})

    def test_cap_identifier_grammar_is_required_from_live_lifecycle(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "evolution_lifecycle.md"
        path.write_text(path.read_text(encoding="utf-8").replace("`CAP-<slug>`", "`removed`"), encoding="utf-8")
        self.assertIn("BOOTSTRAP_REQUIRED", {finding.rule for finding in validate_root(root)})

    def test_canonical_target_aliases_are_rejected(self):
        for alias in ("./evolution_lifecycle.md", "decisions/../evolution_lifecycle.md"):
            with self.subTest(alias=alias), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_tree(root)
                path = root / "decisions" / "example.md"
                text = path.read_text(encoding="utf-8")
                path.write_text(
                    text.replace(
                        "`evolution_lifecycle.md` | `evolution_lifecycle.md` evidence",
                        f"`evolution_lifecycle.md`; `{alias}` | `evolution_lifecycle.md` evidence; `{alias}` evidence",
                    ),
                    encoding="utf-8",
                )
                rules = {finding.rule for finding in validate_root(root)}
                self.assertTrue({"LINK_DESTINATION", "EVIDENCE_SHAPE"} & rules)

    def test_character_reference_cannot_desynchronize_decision_targets_and_evidence(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        (root / "..&sol").write_text("decoy", encoding="utf-8")
        (root / "outside.md").write_text("decoy", encoding="utf-8")
        path = root / "decisions" / "example.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "`evolution_lifecycle.md` | `evolution_lifecycle.md` evidence",
                "..&sol;outside.md | `..&sol` evidence; `outside.md` evidence",
            ),
            encoding="utf-8",
        )
        self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_angle_link_destination_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "backlog" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("../evolution_lifecycle.md", "<../evolution_lifecycle.md>"), encoding="utf-8")
        self.assertIn("LINK_DESTINATION", {finding.rule for finding in validate_root(root)})

    def test_root_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            real_root = Path(directory) / "real"
            real_root.mkdir()
            write_tree(real_root)
            linked_root = Path(directory) / "linked"
            linked_root.symlink_to(real_root, target_is_directory=True)
            self.assertIn("ROOT_INVALID", {finding.rule for finding in validate_root(linked_root)})

    def test_owner_directory_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "root"
            root.mkdir()
            write_tree(root)
            outside = Path(directory) / "outside"
            shutil.copytree(root / "backlog", outside)
            shutil.rmtree(root / "backlog")
            (root / "backlog").symlink_to(outside, target_is_directory=True)
            self.assertIn("OWNER_CONFINEMENT", {finding.rule for finding in validate_root(root)})

    def test_roadmap_exit_gate_requires_existing_module(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "system_roadmap.md"
        path.write_text(path.read_text(encoding="utf-8").replace("modules/core.md", "modules/missing.md"), encoding="utf-8")
        rules = {finding.rule for finding in validate_root(root)}
        self.assertIn("LINK_MISSING", rules)
        self.assertIn("ROADMAP_EVIDENCE", rules)

    def test_roadmap_rejects_inline_code_pseudo_links(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "system_roadmap.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "[module](modules/core.md); [todo](todos/completed/done.md)",
                "`[module](modules/core.md)`; `[todo](todos/completed/done.md)`",
            ),
            encoding="utf-8",
        )
        self.assertIn("ROADMAP_EVIDENCE", {finding.rule for finding in validate_root(root)})

    def test_roadmap_rejects_images_as_evidence_links(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "system_roadmap.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            .replace("[module](modules/core.md)", "![module](modules/core.md)")
            .replace("[todo](todos/completed/done.md)", "![todo](todos/completed/done.md)"),
            encoding="utf-8",
        )
        self.assertIn("ROADMAP_EVIDENCE", {finding.rule for finding in validate_root(root)})

    def test_roadmap_evidence_target_classes_require_markdown_records(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        (root / "modules" / "not-a-record.bin").write_bytes(b"module")
        (root / "todos" / "completed" / "not-a-todo.bin").write_bytes(b"todo")
        path = root / "system_roadmap.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            .replace("modules/core.md", "modules/not-a-record.bin")
            .replace("todos/completed/done.md", "todos/completed/not-a-todo.bin"),
            encoding="utf-8",
        )
        self.assertIn("ROADMAP_EVIDENCE", {finding.rule for finding in validate_root(root)})

    def test_one_character_provenance_is_valid(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("fixture", "x"), encoding="utf-8")
        self.assertEqual([], validate_root(root))

    def test_empty_provenance_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("**Provenance:** fixture", "**Provenance:**"), encoding="utf-8")
        self.assertIn("PROVENANCE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_provenance_below_table_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        text = path.read_text(encoding="utf-8").replace("**Provenance:** fixture\n", "")
        path.write_text(text + "\n**Provenance:** fixture\n", encoding="utf-8")
        self.assertIn("PROVENANCE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_row_level_provenance_override_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("direction", "**Provenance:** override"), encoding="utf-8")
        self.assertIn("PROVENANCE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_duplicate_provenance_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("fixture", "fixture\n**Provenance:** second"), encoding="utf-8")
        self.assertIn("PROVENANCE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_duplicate_provenance_on_one_line_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("fixture", "fixture **Provenance:** second"), encoding="utf-8")
        self.assertIn("PROVENANCE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_fenced_code_provenance_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("**Provenance:** fixture", "```md\n**Provenance:** fixture\n```") ,
            encoding="utf-8",
        )
        self.assertIn("PROVENANCE_SCHEMA", {finding.rule for finding in validate_root(root)})

    def test_empty_indexed_decision_table_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
        self.assertIn("TABLE_ROW", {finding.rule for finding in validate_root(root)})

    def test_indented_records_entry_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("- [Example]", "    - [Example]"), encoding="utf-8")
        self.assertIn("DECISION_MEMBERSHIP", {finding.rule for finding in validate_root(root)})

    def test_fenced_records_entry_does_not_satisfy_membership(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "README.md"
        path.write_text(
            "# Decisions\n\n## Records\n\n```md\n## Records\n- [Example](example.md)\n## Stop\n```\n",
            encoding="utf-8",
        )
        self.assertIn("DECISION_MEMBERSHIP", {finding.rule for finding in validate_root(root)})

    def test_trailing_empty_target_segment_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("`evolution_lifecycle.md` |", "`evolution_lifecycle.md`; |", 1), encoding="utf-8")
        self.assertIn("EVIDENCE_SHAPE", {finding.rule for finding in validate_root(root)})

    def test_trailing_empty_evidence_segment_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(path.read_text(encoding="utf-8").replace("`evolution_lifecycle.md` evidence |", "`evolution_lifecycle.md` evidence; |"), encoding="utf-8")
        self.assertIn("EVIDENCE_SHAPE", {finding.rule for finding in validate_root(root)})

    def test_duplicate_canonical_target_is_rejected(self):
        temp, root = self.fixture()
        self.addCleanup(temp.cleanup)
        path = root / "decisions" / "example.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "`evolution_lifecycle.md` | `evolution_lifecycle.md` evidence |",
                "`evolution_lifecycle.md`; `evolution_lifecycle.md` | `evolution_lifecycle.md` evidence; `evolution_lifecycle.md` evidence |",
            ),
            encoding="utf-8",
        )
        self.assertIn("EVIDENCE_SHAPE", {finding.rule for finding in validate_root(root)})

    def test_controlled_live_tree_copy_detects_mutation(self):
        live_root = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as directory:
            copied_root = Path(directory) / "foundation"
            shutil.copytree(live_root, copied_root, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
            self.assertEqual([], validate_root(copied_root))
            path = copied_root / "evolution_lifecycle.md"
            path.write_text(path.read_text(encoding="utf-8").replace("## State machines", "## State machine removed", 1), encoding="utf-8")
            self.assertIn("HEADING_REQUIRED", {finding.rule for finding in validate_root(copied_root)})
