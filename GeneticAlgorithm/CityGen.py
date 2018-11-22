import random


class CityGen:
	
	def __init__(self, value, city_dicts):
		self.value = value
		self.distance = city_dicts
		
	# retorna la distancia a otra ciudad
	def evaluate_distance(self, city):
		return self.distance[city.value]

