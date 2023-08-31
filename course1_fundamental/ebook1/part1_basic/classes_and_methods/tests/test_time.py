import unittest

from ..time import Time

class TimeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        time = Time()
        time.hour = 11
        time.minute = 35
        time.second = 59
        cls.time = time
        cls.time_to_int = (time.hour * 60 + time.minute) * 60 + time.second
        
    def convert_time_to_int(self, time):
        """
            Convert the time from time object to the total seconds of the time with int type
        """
        return (time.hour * 60 + time.minute) * 60 + time.second
    
    def test_time_to_int_return_number_with_int_type(self):
        self.assertIsInstance(self.time_to_int, int)
    
    def test_convert_time_to_int(self):
        self.assertEqual(self.time_to_int, 41759)
        
    def test_convert_time_to_int_and_increment_seconds(self):
        seconds = self.time_to_int + 500
        self.assertEqual(seconds, 42259)
        
    def test_increment_seconds_to_time_object_return_a_time_object(self):
        new_time = self.time.increment(500)
        self.assertIsInstance(new_time, Time)
        
    def test_current_time_is_after_other_time(self):
        other_time = self.time.increment(-500)
        self.assertTrue(self.time_to_int > self.convert_time_to_int(other_time))
        
    def test_current_time_is_not_after_other_time(self):
        other_time = self.time.increment(500)
        self.assertFalse(self.time_to_int > self.convert_time_to_int(other_time))

    