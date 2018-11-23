import random


class CityChromosome:
	
	def __init__(self, cities):
		self.cities = cities
		self.score = self.evaluate_fitness()
		self.mutation_rate = 0.1

	#
	def evaluate_fitness(self):
		"""
		Metodo que calcula la suma de distancias desde la primera ciudad hasta la ultima.
		:return: distancia total desde la primera ciudad a la ultima.
		"""
		score = 0
		for i in range(len(self.cities) - 1):
			score += self.cities[i].evaluate_distance(self.cities[i + 1])
		return score
	
	def set_mutation_rate(self, rate):
		"""
		Modifica el ratio de mutacion
		:param rate: nuevo ratio de mutacion
		"""
		self.mutation_rate = rate
		
	def mutation(self):
		"""
		Toma dos indices al azar e intercambia las ciudades de esos indices
		"""
		if random.uniform(0, 1) < self.mutation_rate:
			
			lenght_cities = len(self.cities)
			index_a = random.randint(0, lenght_cities)
			index_b = random.randint(0, lenght_cities)
			while index_b == index_a:
				index_b = random.randint(0, lenght_cities) # aseguramos que sean distintos
			city_to_change = self.cities[index_a]
			self.cities[index_a] = self.cities[index_b]
			self.cities[index_b] = city_to_change

	def reproduction(self, chromosome):
		"""
		Crea un hijo a partir de dos cromosomas, el que llama al metodo y el argumento,
		estos comparten los genes de ambos padres en proporciones al azar, realizando
		crossover y mutacion
		:param chromosome: el otro padre
		:return: cromosoma hijo
		"""
		lenght_cities = len(self.cities)
		retention = int(lenght_cities / 3)  #cuantos genes se mantienen en su posicion para los hijos
		retention_parent = random.randint(0, 1)  #quien retiene esos genes 0 -> padre 1 -> madre
		retention_index = random.randint(0, lenght_cities - (retention + 1)) #en que ubicación se retienen
		child = [-1] * lenght_cities # se crea un hijo del mismo tamaño que los padres
		
		# C r o s s o v e r
		if retention_parent == 0:
			retention_genes = self.cities[retention_index:retention_index + retention] #genes a guardar
			rest = [item for item in chromosome.cities if item not in retention_genes] #el resto de los genes
			for i in range(0, lenght_cities):
				if i in range(retention_index, retention_index + retention):
					child[i] = self.cities[i]
				else:
					child[i] = rest.pop(0)
		else:
			retention_genes = chromosome.cities[retention_index:retention_index + retention]
			rest = [item for item in chromosome.cities if item not in retention_genes]
			for i in range(0, lenght_cities):
				if i in range(retention_index, retention_index + retention):
					child[i] = chromosome.cities[i]
				else:
					child[i] = rest.pop(0)
					
		# M u t a c i o n
		child_chromosome = CityChromosome(child)
		child_chromosome.mutation()
		return child_chromosome
