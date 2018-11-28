import unittest
from GeneticAlgorithm.StringGen import StringGen
from GeneticAlgorithm.StringChromosome import StringChromosome
from GeneticAlgorithm.StringPopulation import StringPopulation


class StringPopulationTest(unittest.TestCase):

	def setUp(self):
		string_a = "a"
		string_b = "b"
		string_c = "c"
		string_a = StringGen(string_a)
		string_b = StringGen(string_b)
		self.chromosome_a = StringChromosome([string_a, string_b, string_a])  # aba
		self.chromosome_b = StringChromosome([string_a, string_a, string_b])  # aab
		self.population = StringPopulation([self.chromosome_a, self.chromosome_a, self.chromosome_b, self.chromosome_b], 10, "bab")
		
	def test_evaluate_fitness(self):
		"""
		Evalua que se encuentre el optimo para el bit dado
		"""
		test = StringPopulation([self.chromosome_a, self.chromosome_a, self.chromosome_a, self.chromosome_a], 1, "aaaa")
		test.evaluate_fitness()
		self.assertEqual(test.optimal, True)
		self.population.evaluate_fitness()
		self.assertEqual(self.population.optimal, False)
		
	def test_tournament_selection(self):
		"""
		Comprueba que se retorne una instancia de BitChromosome con la seleccion de torneo
		"""
		k = 5
		best = self.population.tournament_selection(k)
		self.assertIsInstance(best, StringChromosome)
		
	def test_selection(self):
		"""
		Comprueba que la seleccion sea del tamaño deseado
		"""
		selection = self.population.selection()
		self.assertEqual(len(selection), 2 * self.population.size)

	def test_reproduction(self):
		"""
		Prueba que la nueva generacion tenga la misma cantidad de individuos que la pasada
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
		chromosomes = self.population.population
		self.population.evolution()
		self.assertNotEqual(self.population.population, chromosomes)
		self.assertEqual(self.population.generation, 2)


if __name__ == '__main__':
	unittest.main()
