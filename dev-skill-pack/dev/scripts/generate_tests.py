#!/usr/bin/env python3
"""
Generate test scaffolding for a Python module.

Usage:
    echo '{"module_path": "src/myapp/services.py"}' | python3 generate_tests.py

Output: JSON with suggested test cases
"""

import json
import sys
import re
from pathlib import Path


def extract_functions(source: str) -> list[dict]:
    """Extract function/class info from Python source."""
    items = []
    
    # Find classes
    for match in re.finditer(r'^class\s+(\w+)\s*[\(:]', source, re.MULTILINE):
        items.append({"type": "class", "name": match.group(1)})
    
    # Find functions
    for match in re.finditer(r'^def\s+(\w+)\s*\(', source, re.MULTILINE):
        name = match.group(1)
        if not name.startswith("_"):
            items.append({"type": "function", "name": name})
    
    return items


def generate_test_cases(items: list[dict]) -> list[dict]:
    """Generate test case templates."""
    tests = []
    
    for item in items:
        if item["type"] == "class":
            tests.append({
                "target": item["name"],
                "cases": [
                    f"test_{item['name'].lower()}_initialization",
                    f"test_{item['name'].lower()}_valid_input",
                    f"test_{item['name'].lower()}_invalid_input",
                    f"test_{item['name'].lower()}_edge_cases",
                ]
            })
        else:
            tests.append({
                "target": item["name"],
                "cases": [
                    f"test_{item['name']}_success",
                    f"test_{item['name']}_error_handling",
                    f"test_{item['name']}_edge_cases",
                ]
            })
    
    return tests


def main():
    params = json.load(sys.stdin)
    module_path = params.get("module_path", "")
    
    if not module_path or not Path(module_path).exists():
        print(json.dumps({"error": f"Module not found: {module_path}"}))
        return
    
    source = Path(module_path).read_text()
    items = extract_functions(source)
    tests = generate_test_cases(items)
    
    result = {
        "module": module_path,
        "suggested_tests": tests,
        "note": "Review and customize these templates before implementing"
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
