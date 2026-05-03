#!/usr/bin/env python3
"""
Evaluate brainstorm options using weighted scoring matrix.

Usage:
    python3 evaluate_options.py --options "Option A" "Option B" "Option C" \
        --criteria feasibility impact effort risk \
        --weights 3 3 2 2 \
        --scores "9,8,7,6" "7,9,6,8" "6,7,9,7"

Or interactive mode:
    python3 evaluate_options.py --interactive
"""

import argparse
import sys
from typing import List


def parse_score_string(s: str) -> List[int]:
    """Parse '9,8,7,6' into [9,8,7,6]"""
    return [int(x.strip()) for x in s.split(",")]


def print_matrix(options: List[str], criteria: List[str], weights: List[int],
                 scores: List[List[int]], totals: List[float]):
    """Print a nice scoring matrix."""
    col_width = max(max(len(o) for o in options), 12) + 2
    crit_width = 12

    print("\n" + "=" * 70)
    print("WEIGHTED SCORING MATRIX")
    print("=" * 70)

    # Criteria row
    header = f"{'Option':<{col_width}}"
    for c, w in zip(criteria, weights):
        header += f"{c}({w})".rjust(crit_width)
    header += f"{'TOTAL':>{crit_width}}"
    print(header)
    print("-" * 70)

    # Data rows
    for i, opt in enumerate(options):
        row = f"{opt:<{col_width}}"
        for s in scores[i]:
            row += f"{s}".rjust(crit_width)
        row += f"{totals[i]:.2f}".rjust(crit_width)
        print(row)

    print("=" * 70)

    # Winner
    max_idx = totals.index(max(totals))
    print(f"\n🏆 WINNER: {options[max_idx]} (score: {totals[max_idx]:.2f})")

    # Rankings
    ranked = sorted(enumerate(totals), key=lambda x: x[1], reverse=True)
    print("\n📊 Rankings:")
    for rank, (idx, score) in enumerate(ranked, 1):
        print(f"   {rank}. {options[idx]} — {score:.2f}")


def interactive_mode():
    """Run in interactive mode, asking user for input."""
    print("=" * 50)
    print("BRAINSTORM OPTION EVALUATOR (Interactive)")
    print("=" * 50)

    n_options = int(input("\nHow many options? "))
    options = []
    for i in range(n_options):
        options.append(input(f"  Option {i+1} name: "))

    n_criteria = int(input("\nHow many criteria? "))
    criteria = []
    weights = []
    for i in range(n_criteria):
        c = input(f"  Criteria {i+1} name: ")
        w = int(input(f"  Weight for '{c}' (1-5): "))
        criteria.append(c)
        weights.append(w)

    print(f"\nEnter scores (1-10) for each option on each criteria:")
    scores = []
    for opt in options:
        print(f"\n  {opt}:")
        opt_scores = []
        for crit in criteria:
            s = int(input(f"    {crit}: "))
            opt_scores.append(s)
        scores.append(opt_scores)

    total_weight = sum(weights)
    totals = []
    for opt_scores in scores:
        total = sum(s * w for s, w in zip(opt_scores, weights)) / total_weight
        totals.append(total)

    print_matrix(options, criteria, weights, scores, totals)


def main():
    parser = argparse.ArgumentParser(description="Evaluate brainstorm options")
    parser.add_argument("--options", nargs="+", help="Option names")
    parser.add_argument("--criteria", nargs="+", help="Criteria names")
    parser.add_argument("--weights", nargs="+", type=int, help="Criteria weights")
    parser.add_argument("--scores", nargs="+", help="Scores per option, comma-separated")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if not all([args.options, args.criteria, args.weights, args.scores]):
        print("Error: Need --options, --criteria, --weights, --scores (or use --interactive)")
        print("\nExample:")
        print('  python3 evaluate_options.py --options "Cache" "CDN" "Optimize DB"')
        print('    --criteria feasibility impact effort risk')
        print('    --weights 3 3 2 2')
        print('    --scores "9,8,7,6" "7,9,6,8" "6,7,9,7"')
        sys.exit(1)

    options = args.options
    criteria = args.criteria
    weights = args.weights
    scores = [parse_score_string(s) for s in args.scores]

    if len(options) != len(scores):
        print(f"Error: {len(options)} options but {len(scores)} score sets")
        sys.exit(1)

    if len(criteria) != len(weights):
        print(f"Error: {len(criteria)} criteria but {len(weights)} weights")
        sys.exit(1)

    for i, s in enumerate(scores):
        if len(s) != len(criteria):
            print(f"Error: Option '{options[i]}' has {len(s)} scores, expected {len(criteria)}")
            sys.exit(1)

    total_weight = sum(weights)
    totals = []
    for opt_scores in scores:
        total = sum(s * w for s, w in zip(opt_scores, weights)) / total_weight
        totals.append(total)

    print_matrix(options, criteria, weights, scores, totals)


if __name__ == "__main__":
    main()
