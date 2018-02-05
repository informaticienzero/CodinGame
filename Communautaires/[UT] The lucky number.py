import unittest
from LuckyNumbers import count
from typing import Dict, List


class TestLuckyNumbers(unittest.TestCase):
    """
    All the unit tests of the lucky numbers program.
    """

    def test_count_0(self):
        """
        Tests the simplest case, with 0.
        """
        self.assertEqual(count(0), 0, 'Between 0 and 0, there is 0 lucky numbers.')

    def test_count_5(self):
        """
        Test the fast method with 5.
        """
        value: int = 5
        result: int = 0
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_9(self):
        """
        Test the fast method with 9.
        """
        value: int = 9
        result: int = 2
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_10(self):
        """
        Test the fast method with 10.
        """
        value: int = 10
        result: int = 2
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_20(self):
        """
        Test the fast method with 20.
        """
        value: int = 20
        result: int = 4
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_35(self):
        """
        Test the fast method with 35.
        """
        value: int = 35
        result: int = 6
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_66(self):
        """
        Test the fast method with 66.
        """
        value: int = 66
        result: int = 18
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_72(self):
        """
        Test the fast method with 72.
        """
        value: int = 72
        result: int = 21
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_173(self):
        """
        Test the fast method with 173.
        """
        value: int = 173
        result: int = 55
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_459(self):
        """
        Test the fast method with 459.
        """
        value: int = 459
        result: int = 148
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_666(self):
        """
        Test the fast method with 666.
        """
        value: int = 666
        result: int = 264
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_770(self):
        """
        Test the fast method with 770.
        """
        value: int = 770
        result: int = 306
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_1719(self):
        """
        Test the fast method with 2645.
        """
        value: int = 2645
        result: int = 1113
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_2645(self):
        """
        Test the fast method with 1719.
        """
        value: int = 1719
        result: int = 723
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_7000(self):
        """
        Test the fast method with 700.
        """
        value: int = 7000
        result: int = 3333
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_361_000(self):
        """
        Test the fast method with 361000.
        """
        value: int = 361_000
        result: int = 187_995
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_361_070(self):
        """
        Test the fast method with 361070.
        """
        value: int = 361_070
        result: int = 188_058
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_361_077(self):
        """
        Test the fast method with 361077.
        """
        value: int = 361_077
        result: int = 188_065
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_361_080(self):
        """
        Test the fast method with 361080.
        """
        value: int = 361_080
        result: int = 188_067
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_361_087(self):
        """
        Test the fast method with 361087.
        """
        value: int = 361_087
        result: int = 188_067
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_700_000(self):
        """
        Test the fast method with 700000.
        """
        value: int = 700_000
        result: int = 374_421
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_770_000(self):
        """
        Test the fast method with 770000.
        """
        value: int = 770_000
        result: int = 410_562
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_773_000(self):
        """
        Test the fast method with 773000.
        """
        value: int = 773_000
        result: int = 411_864
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_773_904(self):
        """
        Test the fast method with 773904.
        """
        value: int = 773_904
        result: int = 412_264
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_800_000(self):
        """
        Test the fast method with 800000.
        """
        value: int = 800_000
        result: int = 426_983
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_880_000(self):
        """
        Test the fast method with 880000.
        """
        value: int = 880_000
        result: int = 472_910
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_883_904(self):
        """
        Test the fast method with 883904.
        """
        value: int = 883_904
        result: int = 475_749
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_6_645_243(self):
        """
        Test the fast method with 6645243.
        """
        value: int = 6_645_243
        result: int = 3_615_948
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')

    def test_count_1_000_000_000_000_000_000(self):
        """
        Test the fast method with 1000000000000000000.
        """
        value: int = 1_000_000_000_000_000_000
        result: int = 264160473575034274
        self.assertEqual(count(value), result, f'Between 0 and {value}, there are {result} lucky numbers.')


if __name__ == '__main__':
    unittest.main()
