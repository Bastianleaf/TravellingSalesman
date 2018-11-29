import random
from GeneticAlgorithm.CityChromosome import CityChromosome
from GeneticAlgorithm.CityPopulation import CityPopulation
from GeneticAlgorithm.BitChromosome import BitChromosome
from GeneticAlgorithm.BitGen import BitGen
from GeneticAlgorithm.BitPopulation import BitPopulation
from GeneticAlgorithm.StringGen import StringGen
from GeneticAlgorithm.StringChromosome import StringChromosome
from GeneticAlgorithm.StringPopulation import StringPopulation
import string




def generate_random_route(n, city_gen_array, generation_limit):
	"""
	Genera un CityPopulation con variaciones al azar del arreglo de citygen
	:param n: cantidad de rutas distintas
	:param city_gen_array: arreglo de CityGen
	:param generation_limit: limite de generaciones iguales antes de detener evolucion
	:return: CityPopulation con los cromosomas
	"""
	route_array = []
	random_cities = city_gen_array[1:len(city_gen_array) - 2]
	base = [city_gen_array[0]]
	for i in range(n):
		route_array.append(CityChromosome(city_gen_array))
		random.shuffle(random_cities)
		city_gen_array = base + random_cities + base
		
	return CityPopulation(route_array, generation_limit)


def generate_random_bits(n, size, generation_limit, solution):
	bits = ["0", "1"]
	bits_chromosome_array = []
	for i in range(n):
		bits_array = []
		for j in range(size):
			bits_array.append(BitGen(random.choice(bits)))
		bits_chromosome_array.append(BitChromosome(bits_array))
	return BitPopulation(bits_chromosome_array, generation_limit, solution)


def generate_random_string(n, size, generation_limit, solution):
	word = 'abcdefghijklmnopqrstuvwxyz'
	string_chromosome_array = []
	for i in range(n):
		string_array = []
		for j in range(size):
			string_array.append(BitGen(random.choice(word)))
			string_chromosome_array.append(BitChromosome(string_array))
	return BitPopulation(string_chromosome_array, generation_limit, solution)
