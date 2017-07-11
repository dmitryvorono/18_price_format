# TODO place your tests here
import unittest

class TestFormatPrice(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(format_price(''), '')


    def test_none(self):
        self.assertEqual(format_price(None), '')


    def test_zero_fractional_part(self):
        self.assertEqual(format_price('245.000000'), '245')
    

    def test_round_zero_fractional_part(self):
        self.assertEqual(format_price('245.001000'), '245')


    def test_numeric_digit(self):
        self.assertEqual(format_price('123456789'), '123 456 789')


    def test_usial_string(self):
        self.assertEqual(format_price('3245.010001', '3 245.01'))

    
if __name__ == '__init__':
    unittest.main()
