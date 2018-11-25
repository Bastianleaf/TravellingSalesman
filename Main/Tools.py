import random
from Data.DataManagement import DataManagement
from GeneticAlgorithm.CityGen import CityGen
from GeneticAlgorithm.CityChromosome import CityChromosome
from GeneticAlgorithm.CityPopulation import CityPopulation


def generate_random_route(n, city_gen_array, generation_limit):
	"""
	Genera un CityPopulation con variaciones al azar del arreglo de citygen
	:param n: cantidad de rutas distintas
	:param citygen_array: arreglo de CityGen
	:param generation_limit: limite de generaciones iguales antes de detener evolucion
	:return: CityPopulation con los cromosomas
	"""
	route_array = []
	for i in range(n):
		route_array.append(CityChromosome(city_gen_array))
		random.shuffle(city_gen_array)
	return CityPopulation(route_array, generation_limit)
