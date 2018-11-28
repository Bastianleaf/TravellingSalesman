import unittest
from GeneticAlgorithm.StringGen import StringGen
from GeneticAlgorithm.StringChromosome import StringChromosome


class StringChromosomeTest(unittest.TestCase):
	
	def setUp(self):
		string_a = "a"
		string_b = "b"
		string_c = "c"
		string_a = StringGen(string_a)
		string_b = StringGen(string_b)
		self.chromosome_a = StringChromosome([string_a, string_b, string_a]) #aba
		self.chromosome_b = StringChromosome([string_a, string_a, string_b]) #aba
		
	def test_evaluate_fitness(self):
		"""
		Comprueba que el score asignado al cromosoma sea el correcto.
		"""
		self.chromosome_a.evaluate_fitness("aba")
		self.assertEqual(3, self.chromosome_a.score)

	def test_mutation(self):
		"""
		Comprueba que la mutacion retorne un valor distinto
		"""
		self.chromosome_a.set_mutation_rate(1.0)
		bits_values = list(map(lambda x: x.value, self.chromosome_a.value))
		self.chromosome_a.mutation()
		new_bits_values = list(map(lambda x: x.value, self.chromosome_a.value))
		self.assertNotEqual(bits_values, new_bits_values)

	def test_reproduction(self):
		"""
		Comprueba que la reproduccion de un hijo distinto al padre
		"""
		child = self.chromosome_a.reproduction(self.chromosome_b)
		self.assertNotEqual(child, self.chromosome_a)
		self.assertNotEqual(child, self.chromosome_b)
		self.assertEqual(len(child.value), len(self.chromosome_a.value))


if __name__ == '__main__':
	unittest.main()
