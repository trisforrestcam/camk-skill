#!/usr/bin/env python3
"""
Infrastructure resource estimator.

Given peak RPS and storage needs, estimate servers, DBs, and cache.

Usage:
    python3 estimate_resources.py --peak-rps 10000 --storage-tb 10
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Infrastructure estimator")
    parser.add_argument("--peak-rps", type=float, required=True, help="Peak requests per second")
    parser.add_argument("--storage-tb", type=float, default=1.0, help="Total storage in TB")
    parser.add_argument("--write-ratio", type=float, default=0.1, help="Write ratio (0.0-1.0)")

    args = parser.parse_args()

    peak_rps = args.peak_rps
    storage_tb = args.storage_tb
    write_ratio = args.write_ratio

    # Assumptions per instance
    WEB_RPS = 5000
    DB_QPS = 2000
    CACHE_QPS = 100_000

    web_servers = max(2, int(peak_rps / WEB_RPS) + 1)
    db_servers = max(2, int(peak_rps / DB_QPS) + 1)
    cache_servers = max(2, int((peak_rps * 0.8) / CACHE_QPS) + 1)

    # Storage: assume each DB node handles ~2TB
    db_nodes_for_storage = max(2, int(storage_tb / 2) + 1)
    total_db_nodes = max(db_servers, db_nodes_for_storage)

    print("=" * 50)
    print("INFRASTRUCTURE ESTIMATE")
    print("=" * 50)
    print(f"  Peak RPS:        {peak_rps:,.0f}")
    print(f"  Storage:         {storage_tb:.1f} TB")
    print(f"  Write Ratio:     {write_ratio:.0%}")
    print()
    print(f"  Web Servers:     {web_servers}")
    print(f"  Database Nodes:  {total_db_nodes}")
    print(f"  Cache Nodes:     {cache_servers}")
    print(f"  Load Balancers:  2 (HA pair)")
    print()
    print("  Assumptions:")
    print(f"    - Web server handles ~{WEB_RPS:,} RPS")
    print(f"    - DB node handles ~{DB_QPS:,} QPS")
    print(f"    - Cache node handles ~{CACHE_QPS:,} QPS")
    print("=" * 50)


if __name__ == "__main__":
    main()
