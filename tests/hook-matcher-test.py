#!/usr/bin/env python3
"""
TDD tests for rust-skills hook matcher
Run: python3 tests/hook-matcher-test.py
"""

import re
import json
import sys
from pathlib import Path

# Load matcher from hooks.json
hooks_path = Path(__file__).parent.parent / "hooks" / "hooks.json"
with open(hooks_path) as f:
    hooks_config = json.load(f)

MATCHER = hooks_config["hooks"]["UserPromptSubmit"][0]["matcher"]

print(f"=== Hook Matcher TDD Tests ===")
print(f"Matcher loaded from: {hooks_path}\n")

# Test cases: (input, should_match, expected_match_word)
test_cases = [
    # Rust - 
    ("how to use tokio", True, "how to"),
    ("value moved error", True, "value moved"),


]

passed = 0
failed = 0

for text, should_match, expected_word in test_cases:
    match = re.search(MATCHER, text)
    matched = match is not None

    if matched == should_match:
        passed += 1
        if matched:
            print(f"✅ PASS: '{text}' -> matched '{match.group()}'")
        else:
            print(f"✅ PASS: '{text}' -> no match (expected)")
    else:
        failed += 1
        if matched:
            print(f"❌ FAIL: '{text}' -> matched '{match.group()}' (should NOT match)")
        else:
            print(f"❌ FAIL: '{text}' -> no match (should match '{expected_word}')")

print(f"\n=== Summary ===")
print(f"Passed: {passed}/{len(test_cases)}")
print(f"Failed: {failed}/{len(test_cases)}")

if failed > 0:
    sys.exit(1)
