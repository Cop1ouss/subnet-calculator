import unittest

from subnetcalc import describe_subnet


class DescribeSubnetTests(unittest.TestCase):
    def test_standard_slash_24(self):
        out = describe_subnet("192.168.1.0/24")
        self.assertIn("Network address:    192.168.1.0", out)
        self.assertIn("Broadcast address:  192.168.1.255", out)
        self.assertIn("Subnet mask:        255.255.255.0", out)
        self.assertIn("Usable host range:  192.168.1.1 - 192.168.1.254", out)
        self.assertIn("Usable hosts:       254", out)

    def test_host_bits_set_is_normalized_to_the_network_address(self):
        # strict=False: a host address like 192.168.1.5/24 is treated as
        # "what subnet is this host in", the common real-world question,
        # rather than rejected outright.
        out = describe_subnet("192.168.1.5/24")
        self.assertIn("Network address:    192.168.1.0", out)

    def test_slash_30_point_to_point(self):
        out = describe_subnet("10.0.0.0/30")
        self.assertIn("Usable host range:  10.0.0.1 - 10.0.0.2", out)
        self.assertIn("Usable hosts:       2", out)

    def test_slash_31_has_no_network_broadcast_distinction(self):
        out = describe_subnet("10.0.0.0/31")
        self.assertIn("Usable host range:  10.0.0.0 - 10.0.0.1", out)
        self.assertIn("Usable hosts:       2", out)

    def test_slash_32_single_host(self):
        out = describe_subnet("10.0.0.5/32")
        self.assertIn("Usable host range:  10.0.0.5 - 10.0.0.5", out)
        self.assertIn("Usable hosts:       1", out)

    def test_invalid_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            describe_subnet("not-an-ip/24")


if __name__ == "__main__":
    unittest.main()
