import random
from GeneticAlgorithm import AbstractGen
from time import time


class GeneticPopulation:

	def __init__(self, population):
		self.population = population
		self.gen = 1
		self.size = len(self.population)
		self.equal_counter = 0
		
	def evaluate_fitness(self, solution):
		comp = self.population[0].value
		equal = True
		for p in self.population:
			p.score = p.evaluate_fitness(solution)
			if p.value != comp:
				equal = False
		if equal:
			self.equal_counter += 1
		if self.equal_counter == 3:
			return self.population[0]
			
	def selection(self, k):
		best = None
		for i in range(k):
			ind = self.population[random.randint(0, len(self.population) - 1)]
			if (best is None) or ind.score > best.score:
				best = ind
		return best
	
	def get_best(self):
		best = []
		for i in range( 2 * self.size):
			best.append(self.selection(self.size))
		return best
	
	def reproduction(self, pool):
		new_pool = []
		for i in range(0, len(pool), 2):
			new_pool.append(pool[i].reproduction(pool[i + 1]))
		self.gen += 1
		self.population = new_pool

	def evolution(self, solution):
		start_time = time()
		condition = False
		print("Generación " + str(self.gen))
		while not condition:
			#print(self.equal_counter)
			sol = self.evaluate_fitness(solution)
			if sol is not None:
				elapsed_time = time() - start_time
				condition = True
				
			else:
				best = self.get_best()
				self.reproduction(best)
				print("Generación " + str(self.gen))
		print("Encontrado en generacion " + str(self.gen) + ", tiempo demorado: %.10f segundos " %elapsed_time)
		print("Valor: " + str(self.population[0].value))