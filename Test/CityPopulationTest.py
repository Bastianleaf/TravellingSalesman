import unittest
from GeneticAlgorithm.CityGen import CityGen
from GeneticAlgorithm.CityChromosome import CityChromosome
from GeneticAlgorithm.CityPopulation import CityPopulation


class CityPopulationTest(unittest.TestCase):
	
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
		
		self.chrom_0 = CityChromosome([city_0, city_1, city_2, city_3])  # distancia 34
		self.chrom_1 = CityChromosome([city_2, city_3, city_0, city_1])  # distancia 52
		self.chrom_2 = CityChromosome([city_2, city_1, city_0, city_3])  # distancia 52
		self.chrom_3 = CityChromosome([city_1, city_3, city_2, city_0])  # distancia 40
		
		# poblacion genetica
		self.population = CityPopulation([self.chrom_0, self.chrom_1, self.chrom_2, self.chrom_3])
		self.equal_population = CityPopulation([self.chrom_0, self.chrom_0, self.chrom_0, self.chrom_0])
		self.population_test = CityPopulation([self.chrom_0, self.chrom_1, self.chrom_2, self.chrom_3])
	def test_fitness_evaluation(self):
		"""
		Prueba se la evaluacion funciona correctamente de dos formas:
			-Verifica que aumente el contador de generacion homogenea cuando una generacion es identica
			-Verifica que al tercer ciclo de generaciones homogeneas lo considere como optimo
		"""
		self.equal_population.evaluate_fitness()
		self.assertEqual(self.equal_population.homogeneous_counter, 1)
		self.equal_population.evaluate_fitness()
		self.equal_population.evaluate_fitness()
		self.assertTrue(self.equal_population.optimal)

	def test_tournament_selection(self):
		"""
		Verifica que retorne un cromosoma de la poblacion
		"""
		k = 5
		selected = self.population.tournament_selection(k)
		self.assertIsInstance(selected, CityChromosome)

	def test_selection(self):
		"""
		Prueba la seleccion de la poblacion verificando que esta sea el doble
		del tamaño de los cromosomas originales
		"""
		selection = self.population.selection()
		self.assertEqual(len(selection), 2 * self.population.size)
		
	def test_reproduction(self):
		"""
		Prueba que la reproduccion sea exitosa verificando que
		el tamaño de la poblacion sea igual al de la generacion anterior
		"""
		selection = self.population.selection()
		self.population.reproduction(selection)
		self.assertEqual(len(selection) / 2, self.population.size)
		
	def test_evolution(self):
		"""
		Prueba el funcionaiento correcto de evolution:
			-Prueba que la poblacion nueva sea distinta
			-Prueba que haya aumentado la generacion
		"""
		chromosomes = self.population_test.population
		self.population_test.evolution()
		self.assertNotEqual(self.population_test.population, chromosomes)
		self.assertEqual(self.population_test.generation, 2)
		
		
		
if __name__ == '__main__':
	unittest.main()
