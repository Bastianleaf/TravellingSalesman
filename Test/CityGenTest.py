import unittest
from GeneticAlgorithm.CityGen import CityGen


class CityGenTest(unittest.TestCase):
	
	def setUp(self):
		# diccionario de ciudades
		city_0_dict = {0: 0, 1: 10, 2: 20, 3: 30}
		city_1_dict = {0: 10, 1: 0, 2: 12, 3: 8}
		city_2_dict = {0: 20, 1: 12, 2: 0, 3: 12}
		city_3_dict = {0: 30, 1: 8, 2: 12, 3: 0}
		
		# ciudades
		self.city_0 = CityGen(0, city_0_dict)
		self.city_1 = CityGen(1, city_1_dict)
		self.city_2 = CityGen(2, city_2_dict)
		self.city_3 = CityGen(3, city_3_dict)
	
	def test_evaluate_distance(self):
		self.assertEqual(self.city_0.evaluate_distance(self.city_0), 0)
		self.assertEqual(self.city_0.evaluate_distance(self.city_1), 10)
		self.assertEqual(self.city_0.evaluate_distance(self.city_2), 20)
		self.assertEqual(self.city_0.evaluate_distance(self.city_3), 30)


if __name__ == '__main__':
	unittest.main()
