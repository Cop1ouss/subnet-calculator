import argparse
import ipaddress


def describe_subnet(cidr: str) -> str:
    network = ipaddress.ip_network(cidr, strict=False)
    hosts = list(network.hosts())

    lines = [
        f"Network address:   {network.network_address}",
        f"Broadcast address: {network.broadcast_address}",
        f"Subnet mask:       {network.netmask}",
        f"Usable host range: {hosts[0]} - {hosts[-1]}" if hosts else "Usable host range: none",
        f"Usable hosts:      {len(hosts)}",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate subnet details from an IP/CIDR.")
    parser.add_argument("cidr", help="IP address with CIDR, e.g. 192.168.1.0/24")
    args = parser.parse_args()

    print(describe_subnet(args.cidr))


if __name__ == "__main__":
    main()
