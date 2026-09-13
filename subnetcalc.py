"""Command-line subnet calculator, stdlib only (built on `ipaddress`).

Given an IPv4 address and CIDR prefix, prints the network address,
broadcast address, usable host range, subnet mask, and usable host count
-- the numbers you'd otherwise work out by hand for CCNA subnetting
practice.
"""

from __future__ import annotations

import argparse
import ipaddress
import sys


def describe_subnet(cidr: str) -> str:
    network = ipaddress.ip_network(cidr, strict=False)

    if network.num_addresses >= 4:
        usable_first = network.network_address + 1
        usable_last = network.broadcast_address - 1
        usable_range = f"{usable_first} - {usable_last}"
        usable_count = network.num_addresses - 2
    else:
        # /31 (point-to-point, no network/broadcast per RFC 3021) and /32
        # (single host) have no distinct "usable range" in the normal sense.
        usable_range = f"{network.network_address} - {network.broadcast_address}"
        usable_count = network.num_addresses

    lines = [
        f"Address:            {network.network_address.exploded} (input: {cidr})",
        f"Network address:    {network.network_address}",
        f"Broadcast address:  {network.broadcast_address}",
        f"Subnet mask:        {network.netmask}",
        f"Wildcard mask:      {network.hostmask}",
        f"CIDR prefix:        /{network.prefixlen}",
        f"Usable host range:  {usable_range}",
        f"Usable hosts:       {usable_count}",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="subnetcalc",
        description="Subnet calculator: network/broadcast/usable range/mask for an IP+CIDR.",
    )
    parser.add_argument("cidr", help="e.g. 192.168.1.0/24")
    args = parser.parse_args(argv)

    try:
        print(describe_subnet(args.cidr))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
