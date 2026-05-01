#!/usr/bin/env python3
"""
Check code complexity metrics for Python files.

Usage:
    echo '{"path": "src/"}' | python3 check_complexity.py

Output: JSON with complexity report
"""

import json
import sys
import ast
from pathlib import Path


def calculate_cyclomatic(source: str) -> dict:
    """Calculate basic cyclomatic complexity."""
    tree = ast.parse(source)
    
    results = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            complexity = 1  # Base path
            
            for child in ast.walk(node):
                if isinstance(child, (ast.If, ast.While, ast.For,
                                    ast.ExceptHandler, ast.With,
                                    ast.Assert, ast.comprehension)):
                    complexity += 1
                elif isinstance(child, ast.BoolOp):
                    complexity += len(child.values) - 1
            
            results.append({
                "function": node.name,
                "line": node.lineno,
                "complexity": complexity,
                "risk": "high" if complexity > 10 else "medium" if complexity > 5 else "low"
            })
    
    return results


def check_file(filepath: Path) -> dict:
    """Check a single file."""
    try:
        source = filepath.read_text()
        functions = calculate_cyclomatic(source)
        
        high_complexity = [f for f in functions if f["risk"] == "high"]
        
        return {
            "file": str(filepath),
            "functions": functions,
            "summary": {
                "total_functions": len(functions),
                "high_complexity": len(high_complexity),
                "max_complexity": max((f["complexity"] for f in functions), default=0)
            },
            "needs_attention": high_complexity
        }
    except SyntaxError as e:
        return {
            "file": str(filepath),
            "error": f"Syntax error: {e}"
        }


def main():
    params = json.load(sys.stdin)
    path = Path(params.get("path", "."))
    
    if path.is_file():
        files = [path]
    else:
        files = list(path.rglob("*.py"))
    
    results = [check_file(f) for f in files if not f.name.startswith("test_")]
    
    report = {
        "files_checked": len(results),
        "files_with_issues": sum(1 for r in results if r.get("needs_attention")),
        "details": results
    }
    
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
