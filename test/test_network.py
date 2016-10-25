import unittest

import env

from router.network import load_network, Network, NetworkError

class TestNetwork(unittest.TestCase):
    def setUp(self):
        pass


    def test_load(self):
        network = load_network('./data/network.txt')
        self.assertEqual(network.size(), 9)
        reachable_from_Buenos_Aires = network.reachable_from("Buenos Aires")
        self.assertCountEqual(reachable_from_Buenos_Aires,
                              ["Cape Town", "Casablanca", "New York"])


    def test_add_link(self):
        network = Network()
        network.add_link("A", "B", 5)
        network.add_link("C", "B", 6)
        network.add_link("A", "C", 5)

        reachable_from_A = network.reachable_from("A")
        self.assertEqual(len(reachable_from_A), 2)
        self.assertCountEqual(reachable_from_A, ["B", "C"])


    def test_add_circular_link(self):
        network = Network()
        with self.assertRaises(NetworkError):
            network.add_link("B", "B", 5)


    def test_add_nonnumeric_link(self):
        network = Network()
        with self.assertRaises(ValueError):
            network.add_link("B", "C", 'c')


    def test_cost(self):
        network = Network()
        network.add_link("A", "B", 5)
        self.assertEqual(network.link_cost("A", "B"), 5)


if __name__ == '__main__':
    unittest.main()