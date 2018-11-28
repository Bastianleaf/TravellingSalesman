class BitGen:
	
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
		if self.value == "0":
			self.value = "1"
		else:
			self.value = "0"
