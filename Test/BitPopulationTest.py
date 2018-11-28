import unittest
from GeneticAlgorithm.BitGen import BitGen
from GeneticAlgorithm.BitChromosome import BitChromosome
from GeneticAlgorithm.BitPopulation import BitPopulation

class BitPopulationTest(unittest.TestCase):

	def setUp(self):
		bit_a = BitGen("0")
		bit_b = BitGen("1")
		self.chromosome_a = BitChromosome([bit_a, bit_b, bit_a, bit_a])  # 0100
		self.chromosome_b = BitChromosome([bit_b, bit_b, bit_a, bit_a])  # 1100
		self.chromosome_c = BitChromosome([bit_b, bit_b, bit_a, bit_b])  # 1101
		self.chromosome_d = BitChromosome([bit_b, bit_a, bit_a, bit_b])  # 1001
		self.population = BitPopulation([self.chromosome_a, self.chromosome_b, self.chromosome_c, self.chromosome_d], 3,  "1001")

	def test_evaluate_fitness(self):
		test = BitPopulation([self.chromosome_a, self.chromosome_a, self.chromosome_a, self.chromosome_a], 1, "0100")
		test.evaluate_fitness()
		self.assertEqual(test.optimal, True)
		self.population.evaluate_fitness()
		self.assertEqual(self.population.optimal, False)
		
	def test_tournament_selection(self):
		k = 5
		best = self.population.tournament_selection(k)
		self.assertIsInstance(best, BitChromosome)
		
	def test_selection(self):
		selection = self.population.selection()
		self.assertEqual(len(selection), 2 * self.population.size)

	def test_reproduction(self):
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
