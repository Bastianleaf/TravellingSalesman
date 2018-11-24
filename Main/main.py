from Main.Tools import *

#  data TODO: importar desde la carpeta data
city_0_dict = {0: 0, 1: 10, 2: 20, 3: 30}
city_1_dict = {0: 10, 1: 0, 2: 12, 3: 8}
city_2_dict = {0: 20, 1: 12, 2: 0, 3: 12}
city_3_dict = {0: 30, 1: 8, 2: 12, 3: 0}
city_0 = CityGen(0, "ciudad_0", city_0_dict)
city_1 = CityGen(1, "ciudad_1", city_1_dict)
city_2 = CityGen(2, "ciudad_2", city_2_dict)
city_3 = CityGen(3, "ciudad_3", city_3_dict)
cities = [city_0, city_1, city_2, city_3]
# generate random
N = 8
Population = generate_random_route(N, cities)
# print(list(map(lambda x: x.cities, Population.population)))
while not Population.optimal:
	Population.evolution()
#for road in Population.population:
#	print(str(list(map(lambda x: x.value, road.cities))) + "puntaje: " + str(road.score))
print("Generacion: " + str(Population.generation))
optimal = Population.population[(random.randint(0, Population.size - 1))]
road = list(map(lambda x: x.value, optimal.cities))
print("Camino optimo: " + str(road))
cities = list(map(lambda x: x.name, optimal.cities))
print("Ciudades: " + str(cities))
print("Peso de camino optimo: " + str(optimal.score))
