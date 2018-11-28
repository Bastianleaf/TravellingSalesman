import random
import string

class StringGen:
	
	def __init__(self, value):
		"""
		Crea un objeto bit, almacenado como string
		:param value: el bit a crear
		"""
		self.value = value
	
	def mutate(self):
		"""
		Modifica el bit dando su valor inverso
		"""
		not_val = self.value
		while self.value == not_val:
			self.value = random.choice(string.ascii_letters)
