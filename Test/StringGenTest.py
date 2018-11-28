import unittest
from GeneticAlgorithm.StringGen import StringGen


class StringGenTest(unittest.TestCase):
	def setUp(self):
		string_a = "a"
		string_b = "b"
		string_c = "c"
		self.string_a = StringGen(string_a)
		self.string_b = StringGen(string_b)
		self.string_c = StringGen(string_c)
		
	def test_mutate(self):
		"""
		Comprueba que el string sea distinto al mutar
		"""
		self.string_a.mutate()
		self.string_b.mutate()
		self.assertNotEqual("a", self.string_a.value)
		self.assertNotEqual("b", self.string_b.value)


if __name__ == '__main__':
	unittest.main()
