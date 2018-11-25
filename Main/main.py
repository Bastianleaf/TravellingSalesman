from Main.Tools import *
from time import time

#Parametros Globales
path = "../Data/ciudades_europa"   # 1- "../Data/ciudades_europa 2- "../Data/region_metropolitana 3- "../Data/cities
name = "Belgrade"  #Nombre de la ciudad, depende del dataset
N = 20  #Individuos de poblacion
G = 20  #Limite de generaciones identicas



## Creacion de lista de ciudades con caminos al azar
## manteniendo ciudad elegida como base para el origen y destino final
data_set = DataManagement(path)
cities = list()
base_city = None
for city in data_set.data_set:
	city_gen = CityGen(city[0], city[1], city[2])
	if city[1] == name:
		base_city = city_gen
	else:
		cities.append(city_gen)
cities.insert(0, base_city)
cities.append(base_city)
cities_list = list(map(lambda x: x.name, cities))
# generate random
Population = generate_random_route(N, cities, G)

# Algoritmo Pirncipal
print("Calculando ruta optima...")
start_time = time()
while not Population.optimal:
	Population.evolution()
elapsed_time = time() - start_time

# Impresion de informacion
print("Generacion: " + str(Population.generation))
optimal = Population.population[random.randint(0, Population.size - 1)]
road = list(map(lambda x: x.value, optimal.cities))
print("Camino optimo: " + str(road))
cities = list(map(lambda x: x.name, optimal.cities))
print("Ciudades: " + str(cities))
print("Peso de camino optimo: " + str(round(optimal.score, 2)) + " km")
print("Tiempo demorado: %.10f segundos." % elapsed_time)

