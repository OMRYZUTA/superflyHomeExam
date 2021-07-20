import unittest
from solution import get_hour_hand_value, get_minute_hand_value, get_angle, get_fixed_hour_hand_value, solution


class Test(unittest.TestCase):
    def test_get_hour_hand_value(self):
        self.assertEqual(get_hour_hand_value("01"), 30)
        self.assertEqual(get_hour_hand_value("13"), 30)
        self.assertEqual(get_hour_hand_value("00"), 0)
        self.assertEqual(get_hour_hand_value("12"), 0)
        self.assertEqual(get_hour_hand_value("18"), 180)
        self.assertEqual(get_hour_hand_value("09"), 270)
        self.assertEqual(get_hour_hand_value("23"), 330)

    def test_get_minute_hand_value(self):
        self.assertEqual(get_minute_hand_value("30"), 180)
        self.assertEqual(get_minute_hand_value("45"), 270)
        self.assertEqual(get_minute_hand_value("00"), 0)

    def test_get_fixed_hour_hand_value(self):
        self.assertEqual(get_fixed_hour_hand_value(0, 30), 15)

    def test_get_angle(self):
        self.assertEqual(get_angle(270, 0), 90)
        self.assertEqual(get_angle(30, 102), 63.5)

    def test_solution(self):
        self.assertEqual(solution("09:00"), 90)
        self.assertEqual(solution("13:17"), 63.5)


if __name__ == '__main__':
    unittest.main()
