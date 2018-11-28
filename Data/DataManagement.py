import csv
from GeneticAlgorithm.CityGen import CityGen


class DataManagement:
	def __init__(self, file_path):
		self.file_path = file_path
		self.data_set = self.dictionary()

	def dictionary(self):
		"""
		Funcion que crea el atributo de la forma
		[id, nombre, diccionario de pesos]
		en base a un csv ordenado
		:return: retorna el arreglo creado
		"""
		with open(self.file_path) as data:
			reader = csv.reader(data)
			id_counter = 0
			data_set = list()
			for row in reader:
				single_set = list()
				single_set.append(id_counter)  # id
				single_set.append(row[0])  # nombre
				rest = row[1:len(row)]  #ciudades y pesos
				single_set.append(dict(enumerate(map (float, rest))))
				data_set.append(single_set)
				id_counter += 1
		return data_set

	def create_cities(self, origin_name):
		"""
		Dado un nombre de ciudad, crea un arreglo de CityGen con esa ciudad al inicio y fin.
		:param origin_name: nombre de ciudad
		:return: arreglo de CityGen
		"""
		cities = list()
		base_city = None
		for city in self.data_set:
			city_gen = CityGen(city[0], city[1], city[2])
			if city[1] == origin_name:
				base_city = city_gen
			else:
				cities.append(city_gen)
		cities.insert(0, base_city)
		cities.append(base_city)
		return cities
