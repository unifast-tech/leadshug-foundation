# Foundation deterministic validation

`validate_foundation_lifecycle.py` is a read-only Python-standard-library check for the admitted live Foundation lifecycle graph:

- `evolution_lifecycle.md` supplies the bootstrap headings, schemas, and enums.
- `backlog/README.md` supplies current candidate rows.
- `decisions/README.md` and its indexed root decision records supply current decision structure.
- `system_roadmap.md` supplies roadmap gate structure.

It intentionally does not scan history, artifacts, completed documents, or product modules as live authorities. Those files can be valid link targets without becoming inputs. The command validates only objective structure: identifiers, exact table schemas, allowed states, index membership, root-confined references, positional target/evidence shape, and roadmap evidence target classes. It does not assess product decisions, evidence sufficiency, approval authority, or architectural quality.

Run from the project root:

```bash
python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=foundation_documentation/deterministic python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'
```

Exit `0` means no structural finding. Exit `1` means at least one finding. Diagnostics contain only a stable rule code, Foundation-relative owner path, and structural coordinate; they are sorted and capped at 100 findings with a final omitted-count summary. The validator neither writes inputs nor launches subprocesses, network requests, CI jobs, runners, attestations, registries, or provenance subsystems.
