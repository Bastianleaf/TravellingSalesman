class CityGen:
	
	def __init__(self, value, city_dicts):
		"""
		Crea una ciudad gen
		:param value: indice de la ciudad
		:param city_dicts: diccionario con indices de ciudades y respectivas distancias
		"""
		self.value = value
		self.distance = city_dicts
		
	# retorna la distancia a otra ciudad
	def evaluate_distance(self, city):
		"""
		Evalua la distancia que hay entre si misma y otra ciudad
		:param city: el indice de la segunda ciudad
		:return: la distancia entre ambas ciudad
		"""
		return self.distance[city.value]

