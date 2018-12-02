import random


class StringChromosome:
	
	def __init__(self, value):
		self.value = value
		self.mutation_rate = 0.01
		self.score = 0
		
	def evaluate_fitness(self, solution):
		score = 0
		for a, b in zip(self.value, solution):
			if a.value == b:
				score += 1
		self.score = score
		
	def set_mutation_rate(self, rate):
		"""
		Modifica el ratio de mutacion
		:param rate: nuevo ratio de mutacion
		"""
		self.mutation_rate = rate
	
	def mutation(self):
		if random.uniform(0, 1) < self.mutation_rate:
			index = random.randint(0, len(self.value) - 1)
			self.value[index].mutate()
			self.value = self.value[:index] + [self.value[index]] + self.value[index + 1:]
	
	def reproduction(self, gen):
		random_index = random.randint(0, len(self.value) - 1)
		gen_value = []
		for i in range(0, random_index):
			gen_value.append(self.value[i])
		for j in range(random_index, len(self.value)):
			gen_value.append(gen.value[j])
		child = StringChromosome(gen_value)
		child.mutation()
		return child
	
	

