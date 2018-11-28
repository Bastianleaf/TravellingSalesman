import unittest
from Data.DataManagement import DataManagement


class DataManagementTest(unittest.TestCase):
	
	def setUp(self):
		self.file_path = "test_cities"
		
	def test_dictionary(self):
		"""
		Test que prueba el funcionamiento correcto de la funcion diccionario
		"""
		self.DataSet = DataManagement(self.file_path)
		self.assertEqual(self.DataSet.data_set[0], [0, "Ciudad_0", {0: 0, 1: 10, 2: 20, 3: 30}])

	# Todo: hacer test de funcion que crea ciudades


if __name__ == '__main__':
	unittest.main()
