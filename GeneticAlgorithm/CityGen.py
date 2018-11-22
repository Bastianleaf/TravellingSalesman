import random


class CityGen:
	
	def __init__(self, value, city_dicts):
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

