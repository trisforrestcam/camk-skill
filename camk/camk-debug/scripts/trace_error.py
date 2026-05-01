#!/usr/bin/env python3
"""
Analyze a Python traceback and suggest investigation steps.

Usage:
    echo '{"traceback": "..."}' | python3 trace_error.py

Output: JSON with analysis and suggested fixes
"""

import json
import sys
import re


def analyze_traceback(tb: str) -> dict:
    """Analyze a Python traceback."""
    lines = tb.strip().split("\n")
    
    # Extract error type and message
    error_match = re.search(r'(\w+Error):\s*(.+)', tb)
    error_type = error_match.group(1) if error_match else "Unknown"
    error_msg = error_match.group(2) if error_match else "No message"
    
    # Extract file and line from last frame
    frame_pattern = r'File "([^"]+)", line (\d+), in (\w+)'
    frames = re.findall(frame_pattern, tb)
    
    analysis = {
        "error_type": error_type,
        "error_message": error_msg,
        "frames": [
            {"file": f[0], "line": int(f[1]), "function": f[2]}
            for f in frames
        ],
        "suggestions": []
    }
    
    # Type-specific suggestions
    if "AttributeError" in error_type:
        analysis["suggestions"].extend([
            "Check if object is None before accessing attribute",
            "Verify the object has the expected type",
            "Check for typos in attribute names"
        ])
    elif "KeyError" in error_type:
        analysis["suggestions"].extend([
            "Use .get() with default value instead of direct access",
            "Check if key exists before accessing",
            "Verify the dictionary contains expected keys"
        ])
    elif "IndexError" in error_type:
        analysis["suggestions"].extend([
            "Check list length before indexing",
            "Consider using negative indices or slicing",
            "Verify data source returns expected structure"
        ])
    elif "TypeError" in error_type:
        analysis["suggestions"].extend([
            "Check argument types match function signature",
            "Verify None values are handled",
            "Check for missing required arguments"
        ])
    elif "ValueError" in error_type:
        analysis["suggestions"].extend([
            "Validate input before processing",
            "Check data format matches expected pattern",
            "Verify numeric ranges and constraints"
        ])
    else:
        analysis["suggestions"].extend([
            "Read the error message carefully",
            "Check the last frame in the traceback",
            "Add logging around the failing area",
            "Consider adding input validation"
        ])
    
    return analysis


def main():
    params = json.load(sys.stdin)
    traceback = params.get("traceback", "")
    
    if not traceback:
        print(json.dumps({"error": "No traceback provided"}))
        return
    
    result = analyze_traceback(traceback)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
