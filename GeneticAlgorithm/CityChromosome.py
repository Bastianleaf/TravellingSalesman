import random

class CityChromosome:
	
	def __init__(self, cities):
		self.cities = cities
		self.score = self.evaluate_fitness()

	#
	def evaluate_fitness(self):
		"""
		Metodo que calcula la suma de distancias desde la primera ciudad hasta la ultima.
		:return:
		Retorna la suma total.
		"""
		score = 0
		for i in range(len(self.cities) - 1):
			score += self.cities[i].evaluate_distance(self.cities[i + 1])
		return score
	

	def reproduction(self, chromosome):
		retention = len(self.cities) / 3  #cuantos genes se mantienen en su posicion para los hijos
		retention_parent = random.randint(0, 1)  #quien retiene esos genes 0 -> padre 1 -> madre
		retention_index = random.randint(0, len(self.cities) - (retention + 1)) #en que ubicación se retienen
		print(retention)
		print(retention_index)
		print(retention_parent)
		
		
		
		
		
