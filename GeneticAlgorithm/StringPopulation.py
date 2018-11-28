import random


class StringPopulation:
	
	def __init__(self, population, generation_limit, solution):
		"""
		Constructor que crea una poblacion de cromosomas de ciudad
		:param generation_limit: limite de generaciones identicas para detener evolucion
		:param population: poblacion de cromosomas
		:param solution: solucion del problema
		"""
		self.population = population
		self.__generation = 1
		self.size = len(self.population)
		self.homogeneous_counter = 0
		self.optimal = False
		self.equal_count = True
		self.generation_limit = generation_limit
		self.solution = solution
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
		self.population[0].evaluate_fitness(self.solution)
		comparator = self.population[0].score
		self.equal_count = True
		for chromosome in self.population:
			chromosome.evaluate_fitness(self.solution)
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
		# print("Generación: " + str(self.generation))
		self.evaluate_fitness()
		if not self.optimal:
			selection = self.selection()
			self.reproduction(selection)
			self.generation += 1

