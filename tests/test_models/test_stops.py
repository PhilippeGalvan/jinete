import unittest
from copy import deepcopy

import jinete as jit

from tests.utils import (
    generate_one_vehicle,
    generate_one_position,
    generate_one_route,
)


class TestStop(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.vehicle = generate_one_vehicle()
        cls.route = jit.Route(cls.vehicle)

        cls.position = generate_one_position()

    def setUp(self) -> None:
        stop0 = jit.Stop(self.route, self.position, None)

        stop1 = jit.Stop(self.route, generate_one_position(), stop0)
        stop0.following = stop1

        stop2 = jit.Stop(self.route, generate_one_position(), stop1)
        stop1.following = stop2

        stop3 = jit.Stop(self.route, generate_one_position(), stop2)
        stop2.following = stop3

        stop4 = jit.Stop(self.route, generate_one_position(), stop3)
        stop3.following = stop4

        stops = [stop0, stop1, stop2, stop3, stop4]
        self.stops = stops
        self.route.stops = stops

    def test_creation(self):
        stop = jit.Stop(self.route, self.position, None)

        self.assertIsNone(stop._down_time)
        self.assertIsNone(stop._load_time)
        self.assertIsNone(stop._earliest)
        self.assertIsNone(stop._arrival_time)

        self.assertEqual(stop.route, self.route)
        self.assertEqual(stop.position, self.position)
        self.assertEqual(stop.previous, None)
        self.assertEqual(stop.previous_position, self.vehicle.initial)
        self.assertEqual(stop.previous_departure_time, self.vehicle.earliest)
        self.assertEqual(
            stop.navigation_time,
            stop.position.time_to(self.vehicle.initial, stop.previous_departure_time),
        )
        self.assertEqual(stop.waiting_time, 0.0)
        self.assertEqual(stop.down_time, 0.0)
        self.assertEqual(stop.load_time, 0.0)

    def test_creation_with_previous(self):
        previous_position = generate_one_position()
        previous_stop = jit.Stop(self.route, previous_position, None)

        stop = jit.Stop(self.route, self.position, previous_stop)
        previous_stop.following = stop

        self.assertEqual(previous_stop.following, stop)

        self.assertEqual(stop.route, self.route)
        self.assertEqual(stop.position, self.position)
        self.assertEqual(stop.previous, previous_stop)
        self.assertEqual(stop.distance, stop.position.distance_to(previous_stop.position))
        self.assertEqual(stop.previous_position, previous_stop.position)
        self.assertEqual(stop.previous_departure_time, previous_stop.departure_time)
        self.assertEqual(
            stop.navigation_time,
            stop.position.time_to(previous_stop.position, stop.previous_departure_time),
        )

    def test_stops(self):
        route = generate_one_route()
        stop = route.stops[0]
        self.assertEqual(route.stops, stop.stops)

    def test_flush(self):
        stop = jit.Stop(self.route, self.position, None)

        self.assertIsNone(stop._down_time)
        self.assertIsNone(stop._load_time)
        self.assertIsNone(stop._earliest)
        self.assertIsNone(stop._arrival_time)

        self.assertIsInstance(stop.departure_time, float)

        self.assertIsNotNone(stop._down_time)
        self.assertIsNotNone(stop._load_time)
        self.assertIsNotNone(stop._earliest)
        self.assertIsNotNone(stop._arrival_time)

        stop.flush()

        self.assertIsNone(stop._down_time)
        self.assertIsNone(stop._load_time)
        self.assertIsNone(stop._earliest)
        self.assertIsNone(stop._arrival_time)

    def test_cache(self):
        self.assertIsInstance(self.stops[-1].departure_time, float)
        for stop in self.stops:
            self.assertIsNotNone(stop._down_time)
            self.assertIsNotNone(stop._load_time)
            self.assertIsNotNone(stop._earliest)
            self.assertIsNotNone(stop._arrival_time)

    def test_all_following(self):
        self.assertIsInstance(self.stops[-1].departure_time, float)
        self.stops[2].flush_all_following()

        for stop in self.stops[:2]:
            self.assertIsNotNone(stop._down_time)
            self.assertIsNotNone(stop._load_time)
            self.assertIsNotNone(stop._earliest)
            self.assertIsNotNone(stop._arrival_time)
        for stop in self.stops[2:]:
            self.assertIsNone(stop._down_time)
            self.assertIsNone(stop._load_time)
            self.assertIsNone(stop._earliest)
            self.assertIsNone(stop._arrival_time)

    def test_all_previous(self):
        self.assertIsInstance(self.stops[-1].departure_time, float)

        self.stops[2].flush_all_previous()

        for stop in self.stops[:3]:
            self.assertIsNone(stop._down_time)
            self.assertIsNone(stop._load_time)
            self.assertIsNone(stop._earliest)
            self.assertIsNone(stop._arrival_time)

        for stop in self.stops[3:]:
            self.assertIsNotNone(stop._down_time)
            self.assertIsNotNone(stop._load_time)
            self.assertIsNotNone(stop._earliest)
            self.assertIsNotNone(stop._arrival_time)

    def test_flip(self):
        route = deepcopy(self.route)
        stops = route.stops
        stops[1].flip(stops[2])

        self.assertEqual(stops[0].position, self.route.stops[0].position)
        self.assertEqual(stops[1].position, self.route.stops[2].position)
        self.assertEqual(stops[2].position, self.route.stops[1].position)
        self.assertEqual(stops[3].position, self.route.stops[3].position)

        for first, second in zip(stops[:-1], stops[1:]):
            self.assertEqual(first.following, second)
            self.assertEqual(second.previous, first)


if __name__ == '__main__':
    unittest.main()
