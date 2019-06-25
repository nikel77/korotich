import unittest

from my_sum import array_checker


class TestArrayChecker(unittest.TestCase):
    def test_int_than_str(self):
        data = ['1', 'e', '5', 'd']
        result = array_checker(data)
        self.assertEqual(result, True)

    def test_str(self):
        data = ['a', 'v', 's']
        result = array_checker(data)
        self.assertEqual(result, False)

    def test_int(self):
        data = ['1', '2', '3']
        result = array_checker(data)
        self.assertEqual(result, True)

    def test_str_than_int(self):
        data = ['a', 'b', '1']
        result = array_checker(data)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
