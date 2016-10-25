
import unittest

import env

from router.network import load_network, Network, NetworkError
from router.router import RouteCalculator, JourneyError

class TestRouteCalculator(unittest.TestCase):
    def setUp(self):
        network = load_network('./data/network.txt')
        self._route_calc = RouteCalculator(network)


    def test_journey_validation(self):
        self.assertFalse(self._route_calc.validate_journey(['New York', 'Cape Town']))
        self.assertFalse(self._route_calc.validate_journey(['Buenos Aires', 'New York', 'Cape Town']))

        self.assertTrue(self._route_calc.validate_journey(['New York', 'Liverpool']))
        self.assertTrue(self._route_calc.validate_journey(['Buenos Aires', 'New York', 'Liverpool']))


    def test_journey_time(self):
        with self.assertRaises(JourneyError):
            self._route_calc.calculate_journey_time(['New York', 'Cape Town'])

        self.assertEqual(self._route_calc.calculate_journey_time(['New York', 'Liverpool']), 4)
        self.assertEqual(self._route_calc.calculate_journey_time(['Buenos Aires', 'New York', 'Liverpool']), 10)


    def test_shortest_path(self):
        with self.assertRaises(JourneyError):
            self._route_calc.calculate_shortest_path('New York', 'MadeUp Town')

        with self.assertRaises(JourneyError):
            self._route_calc.calculate_shortest_path('New York', 'New York')

        shortest_path = self._route_calc.calculate_shortest_path('New York', 'Liverpool')
        self.assertEqual(len(shortest_path) - 1, 1)
        cost = self._route_calc.calculate_journey_time(shortest_path)
        self.assertEqual(cost, 4)

        shortest_path = self._route_calc.calculate_shortest_path('Buenos Aires', 'Liverpool')
        self.assertEqual(len(shortest_path) - 1, 2)
        cost = self._route_calc.calculate_journey_time(shortest_path)
        self.assertEqual(cost, 8)


    def test_get_all_routes(self):
        with self.assertRaises(JourneyError):
            self._route_calc.get_all_routes('New York', 'MadeUp Town')

        with self.assertRaises(JourneyError):
            self._route_calc.get_all_routes('New York', 'New York')

        shortest_paths = self._route_calc.get_all_routes('Buenos Aires', 'Liverpool')
        self.assertEqual(len(shortest_paths), 2)
        cost = self._route_calc.calculate_journey_time(shortest_paths[0])
        self.assertEqual(cost, 8)
        cost = self._route_calc.calculate_journey_time(shortest_paths[1])
        self.assertEqual(cost, 8)


if __name__ == '__main__':
    unittest.main()