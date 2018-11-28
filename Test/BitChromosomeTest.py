import unittest
from GeneticAlgorithm.BitGen import BitGen
from GeneticAlgorithm.BitChromosome import BitChromosome


class BitChromosomeTest(unittest.TestCase):
	
	def setUp(self):
		bit_a = BitGen("0")
		bit_b = BitGen("1")
		self.chromosome = BitChromosome([bit_a, bit_b, bit_a, bit_a]) #0100
		self.chromosome_test = BitChromosome([bit_b, bit_b, bit_a, bit_a]) #1100
		
	def test_evaluate_fitness(self):
		"""
		Comprueba que el score sea el correcto para el valor dado
		"""
		self.chromosome.evaluate_fitness("0100")
		self.assertEqual(4, self.chromosome.score)
	
	def test_mutation(self):
		"""
		Comprueba que la mutacion retorne un nuevo bit
		"""
		self.chromosome.set_mutation_rate(1.0)
		bits_values = list(map(lambda x: x.value, self.chromosome.value))
		self.chromosome.mutation()
		new_bits_values =  list(map(lambda x: x.value, self.chromosome.value))
		self.assertNotEqual(bits_values, new_bits_values)
		
	def test_reproduction(self):
		"""
		Comprueba que la reproduccion genere la cantidad correcta de hijos.
		"""
		child = self.chromosome.reproduction(self.chromosome_test)
		self.assertNotEqual(child, self.chromosome)
		self.assertNotEqual(child, self.chromosome_test)
		self.assertEqual(len(child.value), len(self.chromosome.value))
	
	
	


if __name__ == '__main__':
	unittest.main()
