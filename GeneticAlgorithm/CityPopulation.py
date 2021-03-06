import random
from time import time


class CityPopulation:

	def __init__(self, population, generation_limit):
		"""
		Constructor que crea una poblacion de cromosomas de ciudad
		:param generation_limit: limite de generaciones identicas para detener evolucion
		:param population: poblacion de cromosomas
		"""
		self.population = population
		self.__generation = 1
		self.size = len(self.population)
		self.homogeneous_counter = 0
		self.optimal = False
		self.equal_count = True
		self.generation_limit = generation_limit
		self.best = None
		self.best_score = 0
		self.best_cities = []
	
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
		si los puntajes son iguales para todas las configuraciones durante 100 generaciones
		se considera optimo
		"""
		if self.best is None:
			self.best = self.population[0]
			self.best_score = self.population[0].score
			self.best_cities = list(map(lambda x: x.name, self.population[0].cities))
		comparator = self.population[0].score
		self.equal_count = True
		for chromosome in self.population:
			if chromosome.score < self.best_score:
				self.best = list(map(lambda x: x.value, chromosome.cities))
				self.best_score = chromosome.score
				self.best_cities = list(map(lambda x: x.name, self.population[0].cities))
			if chromosome.score != comparator:
				self.equal_count = False
		if self.equal_count:
			self.homogeneous_counter += 1
		else:
			self.homogeneous_counter = 0
		if self.homogeneous_counter == self.generation_limit:
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
		Selecciona el 25% de la poblacion.
		Utilzia la seleccion de torneo.
		:return: retorna una cantidad igual al doble del tamaño de la generacion basado en el 25%
		"""
		best = []
		for i in range(int(self.size / 4)):
			best.append(self.tournament_selection(self.size))
		best = best * 8
		if len(best) < self.size * 2:
			while len(best) < self.size * 2:
				best.append(best[random.randint(0, len(best) - 1)])
		elif len(best) > self.size * 2:
			while len(best) > self.size * 2:
				best.pop(0)
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
		"""
		Ejecuta el proceso evolutivo de la poblacion:
			-Se evalua el fitness
			-Si es que no es el optimo se realiza la seleccion, reproduccion y
			se aumenta el contador de generacion
		"""
		self.evaluate_fitness()
		if not self.optimal:
			selection = self.selection()
			self.reproduction(selection)
			self.generation += 1

