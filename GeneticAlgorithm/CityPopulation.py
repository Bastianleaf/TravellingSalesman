import random
from time import time


class CityPopulation:

	def __init__(self, population):
		self.population = population
		self.__generation = 1
		self.size = len(self.population)
		self.homogeneous_counter = 0
		self.optimal = False
	
	@property
	def generation(self):
		"""
		Generacion evolutiva de la poblacion
		:return: retorna la generacion en que se encuenta la poblacion
		"""
		return self.__generation
	
	@generation.setter
	def generation(self, value):
		"""
		Setea la generacion de la poblacion
		:param value: generacion
		"""
		if value < 1:
			raise ValueError("Generacion no puede ser menor a 1.")
		self.__generation = value
		
		
	def evaluate_fitness(self):
		"""
		Metodo que compara el puntaje asociado a los caminos de las ciudades,
		si los puntajes son iguales para todas las configuraciones durante 3 generaciones
		se considera optimo
		:return: chromosoma con la configuracion optima
		"""
		comparator = self.population[0].score
		equal_count = True
		for chromosome in self.population:
			if chromosome.score != comparator:
				equal_count = False
		if equal_count:
			self.homogeneous_counter += 1
		if self.homogeneous_counter == 3:
			self.optimal = True
			
	def tournament_selection(self, k):
		"""
		Dado un parametro k de variabilidad, selecciona el mejor de la poblacion
		Se considera el mejor el que tenga un puntaje mas bajo.
		:param k: parametro de variabilidad.
		:return: un cromosoma de ciudades.
		"""
		best = None
		for i in range(k):
			ind = self.population[random.randint(0, len(self.population) - 1)]
			if (best is None) or ind.score < best.score:
				best = ind
		return best
	
	def selection(self):
		"""
		Selecciona un grupo de cromosomas del doble de tamaño que la poblacion.
		Utilza la seleccion de torneo.
		:return:
		"""
		best = []
		for i in range(2 * self.size):
			best.append(self.tournament_selection(self.size))
		return best
	
	def reproduction(self, pool):
		"""
		Teniendo una pool de cromosomas, genera un nuevo pool en base a la reproduccion
		de estos.
		:param pool: pool de cromosomas seleccionados
		"""
		new_pool = []
		for i in range(0, len(pool), 2):
			new_pool.append(pool[i].reproduction(pool[i + 1]))
		self.population = new_pool
		

	def evolution(self):
		selection = self.selection()
		self.reproduction(selection)
		self.generation += 1
		
		
		