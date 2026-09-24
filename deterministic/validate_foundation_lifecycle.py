#!/usr/bin/env python3
"""Validate the bounded live Foundation lifecycle graph without modifying it."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
sys.dont_write_bytecode = True

from foundation_lifecycle.parser import validate_root


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only Foundation lifecycle structural validation.")
    parser.add_argument("--root", required=True, help="Foundation root to validate")
    args = parser.parse_args(argv)
    findings = validate_root(Path(args.root))
    for finding in findings[:100]:
        print(finding.render())
    if len(findings) > 100:
        print(f"<root>:summary: FINDINGS_OMITTED_{len(findings) - 100}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
