from Main.Tools import *
from time import time
import matplotlib.pyplot as plt
import numpy


#Parametros Globales
dataset_path = "../Data/ciudades_europa"   # 1- "../Data/ciudades_europa 2- "../Data/region_metropolitana 3- "../Data/cities
origin_name = "Madrid"  #Nombre de la ciudad, depende del dataset
population_size = 20  #Individuos de poblacion
generations_number = 10  #Limite de generaciones identicas

## Creacion de lista de ciudades con caminos al azar
## manteniendo ciudad elegida como base para el origen y destino final
data_set = DataManagement(dataset_path)
cities = data_set.create_cities(origin_name)
# generate random
Population = generate_random_route(population_size, cities, generations_number)

# Algoritmo Principal
print("Calculando ruta optima...")
start_time = time()
count = 0
data_x = []
data_y = []
while not Population.optimal:
	data_x.append(count)
	data_y.append(numpy.mean(list(map(lambda x: x.score, Population.population))))
	Population.evolution()
	count += 1
elapsed_time = time() - start_time
print(data_y)

# Impresion de informacion
print("Generacion: " + str(Population.generation))
optimal = Population.population[random.randint(0, Population.size - 1)]
road = list(map(lambda x: x.value, optimal.cities))
print("Camino optimo: " + str(road))
cities = list(map(lambda x: x.name, optimal.cities))
print("Ciudades: " + str(cities))
print("Peso de camino optimo: " + str(round(optimal.score, 2)) + " km")
print("Tiempo demorado: %.10f segundos." % elapsed_time)

plt.grid(True)
plt.plot(data_x, data_y)
plt.title('Camino más corto según generación. ')
plt.xlabel("Generacion de la poblacion")
plt.show()

