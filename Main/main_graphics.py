from Main.Tools import *
from time import time
import matplotlib.pyplot as plt
import numpy as np


#Parametros Globales
dataset_path = "../Data/ciudades_europa"   # 1- "../Data/ciudades_europa 2- "../Data/region_metropolitana 3- "../Data/cities
origin_name = "Barcelona"  #Nombre de la ciudad, depende del dataset

data_score = []
data_generations = []
data_time = []

outputs_array = range(4, 15)
for n in outputs_array:
	population_size = 50  #Individuos de poblacion
	generations_number = n #Limite de generaciones identicas

	
	
	## Creacion de lista de ciudades con caminos al azar
	## manteniendo ciudad elegida como base para el origen y destino final
	data_set = DataManagement(dataset_path)
	cities = data_set.create_cities(origin_name)
	# generate random
	Population = generate_random_route(population_size, cities, generations_number)
	
	# Algoritmo Principal
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
	#data.append([optimal, road, cities, round(optimal.score, 2)])
	print(n)
	data_score.append(round(optimal.score, 2))
	data_time.append(elapsed_time)
	data_generations.append(Population.generation)

plt.subplot(3, 1, 1)
plt.grid(True)
#plt.axis([3, max(outputs_array) + 1, min(data_score) , max(data_score) ])
plt.plot(outputs_array, data_score)
plt.title('Camino por Ciudades de Europa segun Tamaño de Población')
plt.ylabel('Optimo [km]')
plt.subplot(3, 1, 2)
plt.grid(True)
plt.plot(outputs_array, data_generations)
plt.ylabel('Generaciones')
plt.subplot(3, 1, 3)
plt.grid(True)
plt.plot(outputs_array, data_time)
plt.ylabel('Tiempo[s]')
plt.xlabel('Tamaño de Población')
plt.show()

