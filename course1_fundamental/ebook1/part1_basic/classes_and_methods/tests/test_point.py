import unittest

from ..point import Point

class PointTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        first_point = Point(3, 5)
        second_point = Point(3, 5)
        cls.new_point = first_point + second_point
    
    def test_add_two_points(self):
        self.assertEqual(self.new_point.x, 6)
        self.assertEqual(self.new_point.y, 10)
        
    def test_add_point_and_tuple_return_a_new_point(self):
        self.assertIsInstance(self.new_point, Point)
        
    def test_add_point_and_tuple(self):
        self.assertEqual(self.new_point.x, 6)
        self.assertEqual(self.new_point.y, 10)
        