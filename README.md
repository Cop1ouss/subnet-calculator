# Subnet Calculator

![category](https://img.shields.io/badge/category-Networking%20%26%20Certs-0ea5e9)
![status](https://img.shields.io/badge/status-active-34d399)
![stdlib only](https://img.shields.io/badge/dependencies-stdlib%20only-a78bfa)

A command-line subnet calculator, built while studying for CCNA. Given an
IPv4 address and CIDR (e.g. `192.168.1.0/24`), it prints:

- Network address
- Broadcast address
- Subnet mask + wildcard mask
- Usable host range
- Number of usable hosts

Correctly handles the edge cases too: a host address like `192.168.1.5/24`
is normalized to its network (`192.168.1.0/24` — "what subnet is this host
in" is the usual real question); `/31` point-to-point links (RFC 3021, no
distinct network/broadcast address) and `/32` single hosts are both
reported without a fabricated 2-address deduction.

## Usage

```bash
python3 subnetcalc.py 192.168.1.0/24
```

```
Address:            192.168.1.0 (input: 192.168.1.0/24)
Network address:    192.168.1.0
Broadcast address:  192.168.1.255
Subnet mask:        255.255.255.0
Wildcard mask:      0.0.0.255
CIDR prefix:        /24
Usable host range:  192.168.1.1 - 192.168.1.254
Usable hosts:       254
```

## Tests

```bash
python3 -m unittest test_subnetcalc -v
```

No dependencies beyond the standard library (`ipaddress`, `argparse`).

## Related

Part of the same CCNA study track as [`ccna-tracker`](https://github.com/Cop1ouss/ccna-tracker)
(`scripts/subnet_drill.py` there is a timed quiz generator over the same
kind of problem) and [`cisco-track`](https://github.com/Cop1ouss/cisco-track).
