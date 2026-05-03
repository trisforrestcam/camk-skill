#!/usr/bin/env python3
"""
Premortem analysis: Imagine the project failed, then work backwards to find why.

Usage:
    python3 premortem.py --project "Migrate to microservices" \
        --timeline "6 months" \
        --team-size 5

Or interactive mode:
    python3 premortem.py --interactive
"""

import argparse
import random


PREMORTEM_PROMPTS = [
    "What was the first sign that things were going wrong?",
    "Which assumption turned out to be completely false?",
    "What did we underestimate by 10x?",
    "Which stakeholder was most surprised by the failure?",
    "What was the 'we should have known' moment?",
    "Which dependency failed us?",
    "What did we ignore because it was 'not our problem'?",
    "Which risk did we dismiss as 'unlikely'?",
    "What was the breaking point?",
    "If we could go back 1 month, what would we change?",
]

RISK_CATEGORIES = [
    ("Technical", "Architecture, tech debt, scalability, integration"),
    ("People", "Team skills, bandwidth, turnover, communication"),
    ("Process", "Planning, estimation, decision-making, reviews"),
    ("External", "Dependencies, vendors, regulations, market"),
    ("Resource", "Budget, time, tools, infrastructure"),
]


def interactive_mode():
    print("=" * 60)
    print("PREMORTEM ANALYSIS")
    print("=" * 60)
    print("\nImagine: It's 6 months from now. The project has FAILED.")
    print("Let's work backwards to find out why.\n")

    project = input("Project name: ")
    timeline = input("Timeline: ")

    print(f"\n{'='*60}")
    print(f"PREMORTEM: {project}")
    print(f"Timeline: {timeline}")
    print(f"{'='*60}")

    # Scenario
    print("\n📋 SCENARIO:")
    print(f"   It's {timeline} from now. {project} has failed.")
    print("   The post-mortem meeting is happening. What went wrong?")

    # Prompts
    print("\n🎯 REFLECTION PROMPTS:")
    selected = random.sample(PREMORTEM_PROMPTS, min(5, len(PREMORTEM_PROMPTS)))
    for i, prompt in enumerate(selected, 1):
        print(f"   {i}. {prompt}")

    # Risk categories
    print("\n⚠️  RISK CATEGORIES TO CONSIDER:")
    for cat, desc in RISK_CATEGORIES:
        print(f"   • {cat}: {desc}")

    # Output template
    print("\n" + "=" * 60)
    print("FILL IN THE BLANKS:")
    print("=" * 60)
    print("""
Most likely failure mode:
  ___________________________________________________

Root cause:
  ___________________________________________________

Early warning sign we missed:
  ___________________________________________________

What we should have done differently:
  ___________________________________________________

Mitigation for next time:
  ___________________________________________________
""")


def quick_mode(project: str, timeline: str, team_size: int = None):
    print("=" * 60)
    print(f"PREMORTEM: {project}")
    print(f"Timeline: {timeline}")
    if team_size:
        print(f"Team size: {team_size}")
    print("=" * 60)

    print("\n📋 SCENARIO:")
    print(f"   It's {timeline} from now. '{project}' has failed.")

    print("\n🎯 TOP 5 QUESTIONS:")
    selected = random.sample(PREMORTEM_PROMPTS, 5)
    for i, prompt in enumerate(selected, 1):
        print(f"   {i}. {prompt}")

    print("\n⚠️  RISK CATEGORIES:")
    for cat, desc in RISK_CATEGORIES:
        print(f"   • {cat}: {desc}")

    print("\n💡 OUTPUT TEMPLATE:")
    print("-" * 40)
    print("Failure mode: [describe how it failed]")
    print("Root cause:   [the underlying reason]")
    print("Early sign:   [what we should have noticed]")
    print("Mitigation:   [how to prevent it]")
    print("-" * 40)


def main():
    parser = argparse.ArgumentParser(description="Premortem analysis")
    parser.add_argument("--project", help="Project name")
    parser.add_argument("--timeline", default="6 months", help="Project timeline")
    parser.add_argument("--team-size", type=int, help="Team size")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.project:
        quick_mode(args.project, args.timeline, args.team_size)
    else:
        print("Usage:")
        print("  python3 premortem.py --interactive")
        print("  python3 premortem.py --project 'Migrate to microservices' --timeline '3 months'")


if __name__ == "__main__":
    main()
