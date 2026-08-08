#!/usr/bin/env python3
"""Runs every GLEAN test module in one shot. Exit code 0 = all passed."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
TESTS = ["test_inference.py", "test_db.py", "test_addon.py"]

def main():
    failures = []
    for t in TESTS:
        print(f"\n{'='*60}\n{t}\n{'='*60}")
        r = subprocess.run([sys.executable, str(HERE / t)])
        if r.returncode != 0:
            failures.append(t)
    print("\n" + "=" * 60)
    if failures:
        print(f"FAILED: {failures}")
        sys.exit(1)
    print("ALL TEST MODULES PASSED")

if __name__ == "__main__":
    main()
