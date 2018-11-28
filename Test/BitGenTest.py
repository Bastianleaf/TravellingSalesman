import unittest
from GeneticAlgorithm.BitGen import BitGen


class BitGenTest(unittest.TestCase):
	def setUp(self):
		bit_a = "0"
		bit_b = "1"
		self.bit_a = BitGen(bit_a)
		self.bit_b = BitGen(bit_b)
		
	def test_mutate(self):
		self.bit_a.mutate()
		self.bit_b.mutate()
		self.assertEqual("1", self.bit_a.value)
		self.assertEqual("0", self.bit_b.value)


if __name__ == '__main__':
	unittest.main()
