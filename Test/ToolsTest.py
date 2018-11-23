import unittest
from Main.Tools import *


class ToolTest(unittest.TestCase):
	def setUp(self):
		# diccionario de ciudades
		city_0_dict = {0: 0, 1: 10, 2: 20, 3: 30}
		city_1_dict = {0: 10, 1: 0, 2: 12, 3: 8}
		city_2_dict = {0: 20, 1: 12, 2: 0, 3: 12}
		city_3_dict = {0: 30, 1: 8, 2: 12, 3: 0}
		
		# ciudades
		city_0 = CityGen(0, city_0_dict)
		city_1 = CityGen(1, city_1_dict)
		city_2 = CityGen(2, city_2_dict)
		city_3 = CityGen(3, city_3_dict)
		
		self.cities = [city_0, city_1, city_2, city_3]
		
	def test_generate_random_route(self):
		population = generate_random_route(8, self.cities)
		self.assertIsInstance(population, CityPopulation)
		self.assertIsInstance(population.population[0], CityChromosome)
		self.assertEqual(len(population.population), 8)


if __name__ == '__main__':
	unittest.main()
