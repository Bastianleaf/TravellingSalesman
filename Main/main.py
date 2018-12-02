from Main.Tools import *
from time import time
from Data import DataManagement
#Parametros Globales
dataset_path = "../Data/ciudades_europa"   # 1- "../Data/ciudades_europa 2- "../Data/region_metropolitana 3- "../Data/cities
origin_name = "Madrid"  #Nombre de la ciudad, depende del dataset
population_size = 100  #Individuos de poblacion
generations_number = 40  #Limite de generaciones identicas


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
print("Camino optimo: " + str(Population.best))
cities = Population.best_cities
print("Ciudades: " + str(cities))
print("Peso de camino optimo: " + str(round(Population.best_score, 2)) + " km")
print("Tiempo demorado: %.10f segundos." % elapsed_time)

