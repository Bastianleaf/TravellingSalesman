import unittest
from GeneticAlgorithm.CityGen import CityGen
from GeneticAlgorithm.CityChromosome import CityChromosome


class CityGenTest(unittest.TestCase):

	def setUp(self):
		# diccionario de ciudades
		city_0_dict = {0: 0, 1: 10, 2: 20, 3: 30}
		city_1_dict = {0: 10, 1: 0, 2: 12, 3: 8}
		city_2_dict = {0: 20, 1: 12, 2: 0, 3: 12}
		city_3_dict = {0: 30, 1: 8, 2: 12, 3: 0}
		
		# ciudades
		city_0 = CityGen(0, "ciudad_0", city_0_dict)
		city_1 = CityGen(1, "ciudad_1", city_1_dict)
		city_2 = CityGen(2, "ciudad_2", city_2_dict)
		city_3 = CityGen(3, "ciudad_3", city_3_dict)
		
		# cromosomas
		self.chrom_0 = CityChromosome([city_0, city_1, city_2, city_3])  #distancia 34, a reproducir
		self.chrom_1 = CityChromosome([city_2, city_3, city_0, city_1])  #distancia 52, a reproducir
		self.chrom_2 = CityChromosome([city_2, city_1, city_0, city_3])  #distancia 52, a mutar
		self.chrom_3 = CityChromosome([city_1, city_3, city_2, city_0])  #distancia 40
		
	def test_evaluate_fitness(self):
		"""
		Prueba si calcula correctamente el puntaje asociado a cada cromosoma
		"""
		self.assertEqual(self.chrom_0.score, 34)
		self.assertEqual(self.chrom_1.score, 52)
		self.assertEqual(self.chrom_2.score, 52)
		self.assertEqual(self.chrom_3.score, 40)
		
	def test_mutation(self):
		"""
		Prueba si funciona correctamente la mutacion
		"""
		self.chrom_3.set_mutation_rate(1.0)
		cities_index_before = list(map(lambda x: x.value, self.chrom_3.cities))
		self.chrom_3.mutation() # se muta
		cities_index_after = list(map(lambda x: x.value, self.chrom_3.cities))
		self.assertNotEqual(cities_index_before, cities_index_after)
		
	def test_reproduction(self):
		"""
		Prueba si la reproduccion funciona correctamente de dos formas:
			-Los hijos y padres poseen la misma cantidad de genes (ciudades)
			-Los hijos no tienen genes (ciudades) repetidos.
		"""
		self.chrom_child = self.chrom_0.reproduction(self.chrom_1)
		self.assertEqual(len(self.chrom_0.cities), len(self.chrom_child.cities))
		child_index_cities = list(map(lambda x: x.value, self.chrom_child.cities))
		self.assertTrue(len(child_index_cities) == len(set(child_index_cities)))

	
if __name__ == '__main__':
	unittest.main()
