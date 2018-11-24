import csv


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
				single_set.append(dict(enumerate(map(int, rest))))
				data_set.append(single_set)
				id_counter += 1
		return data_set
