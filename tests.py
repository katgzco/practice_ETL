import unittest
from extraction import create_days_range


class TestSum(unittest.TestCase):
    def test_create_days_range(self):
        range_tested = [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
        ]
        result = create_days_range(2022, 4)
        self.assertEqual(result, range_tested)
