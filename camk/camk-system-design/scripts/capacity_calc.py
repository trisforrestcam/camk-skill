#!/usr/bin/env python3
"""
Capacity calculator for system design.

Usage:
    python3 capacity_calc.py --dau 1000000 --requests-per-user 10 \
        --payload-bytes 1024 --read-ratio 0.9
"""

import argparse


def format_number(n: float) -> str:
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.2f}B"
    if n >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    if n >= 1_000:
        return f"{n/1_000:.2f}K"
    return f"{n:.2f}"


def format_bytes(b: float) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if b < 1024:
            return f"{b:.2f} {unit}"
        b /= 1024
    return f"{b:.2f} EB"


def main():
    parser = argparse.ArgumentParser(description="System design capacity calculator")
    parser.add_argument("--dau", type=int, required=True, help="Daily active users")
    parser.add_argument("--requests-per-user", type=int, default=10, help="Requests per user per day")
    parser.add_argument("--payload-bytes", type=int, default=1024, help="Average payload size in bytes")
    parser.add_argument("--read-ratio", type=float, default=0.9, help="Read request ratio (0.0-1.0)")
    parser.add_argument("--replication", type=int, default=3, help="Data replication factor")
    parser.add_argument("--peak-multiplier", type=float, default=3.0, help="Peak traffic multiplier")

    args = parser.parse_args()

    dau = args.dau
    rpu = args.requests_per_user
    payload = args.payload_bytes
    read_ratio = args.read_ratio
    replication = args.replication
    peak = args.peak_multiplier

    total_requests = dau * rpu
    avg_rps = total_requests / 86_400
    peak_rps = avg_rps * peak

    read_rps = peak_rps * read_ratio
    write_rps = peak_rps * (1 - read_ratio)

    daily_data = total_requests * payload
    yearly_data = daily_data * 365 * replication

    ingress = write_rps * payload
    egress = read_rps * payload

    print("=" * 50)
    print("CAPACITY ESTIMATION RESULTS")
    print("=" * 50)
    print(f"  Daily Active Users (DAU): {format_number(dau)}")
    print(f"  Total Requests/Day:       {format_number(total_requests)}")
    print(f"  Average RPS:              {format_number(avg_rps)}")
    print(f"  Peak RPS (x{peak}):         {format_number(peak_rps)}")
    print(f"    - Read RPS:             {format_number(read_rps)}")
    print(f"    - Write RPS:            {format_number(write_rps)}")
    print()
    print(f"  Daily Data:               {format_bytes(daily_data)}")
    print(f"  Yearly Data (x{replication} repl):   {format_bytes(yearly_data)}")
    print()
    print(f"  Ingress Bandwidth:        {format_bytes(ingress)}/s")
    print(f"  Egress Bandwidth:         {format_bytes(egress)}/s")
    print("=" * 50)


if __name__ == "__main__":
    main()
