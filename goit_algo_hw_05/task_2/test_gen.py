import unittest
from main import sum_profit, generator_numbers
import test_data as td

class TestSumNumbers(unittest.TestCase):

    def test_text1(self):
        result = sum_profit(td.text_1, generator_numbers)
        self.assertAlmostEqual(result, 1351.46)

    def test_text2(self):
        result = sum_profit(td.text_2, generator_numbers)
        self.assertAlmostEqual(result, 1368.78)

    def test_text3(self):
        result = sum_profit(td.text_3, generator_numbers)
        self.assertAlmostEqual(result, 390.95)

    def test_text4(self):
        result = sum_profit(td.text_4, generator_numbers)
        self.assertEqual(result, 10000)

    def test_empty_string(self):
        text = ""
        result = sum_profit(text, generator_numbers)
        self.assertEqual(result, 0)

    def test_no_numbers(self):
        text = "Це просто тест без чисел."
        result = sum_profit(text, generator_numbers)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
