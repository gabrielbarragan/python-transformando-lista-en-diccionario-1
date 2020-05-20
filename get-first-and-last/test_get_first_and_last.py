import unittest
from get_first_and_last import *


class GetFirstAndLastTests(unittest.TestCase):
    
	def test_list_with_five_strings(self):
		input_array = ["Lapiz", "goma", "regla", "pluma", "azul"]
		expected_dict = {'Lapiz': 'azul'}
		self.assertEqual(get_first_and_last(input_array), expected_dict)

	def test_list_with_three_strings(self):
		input_array = ["oro", "arroz", "molido"]
		expected_dict = {'oro': 'molido'}
		self.assertEqual(get_first_and_last(input_array), expected_dict)

if __name__=="__main__":
    unittest.main()