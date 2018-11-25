from Main.Tools import *

#  data TODO: importar desde la carpeta data

#path = "../Data/region_metropolitana"
path = "../Data/ciudades_europa"

data_set = DataManagement(path)
#print(data_set.data_set)
cities = list()
for city in data_set.data_set:
	city_gen = CityGen(city[0], city[1], city[2])
	cities.append(city_gen)
	
# generate random
N = 20
G = 100
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
print("Peso de camino optimo: " + str(round(optimal.score, 2)) + " km")
