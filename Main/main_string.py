from Main import Tools
from time import time
import random

# Parametros Globales
palabra = "ve"
population_size = 8  # Individuos de poblacion
generations_number = 2
Population = Tools.generate_random_string(population_size, len(palabra), generations_number, palabra)

# Algoritmo Principal
print("Calculando la palabra...")
start_time = time()
while not Population.optimal:
	Population.evolution()

elapsed_time = time() - start_time

# Impresion de informacion
print("Generacion: " + str(Population.generation))
optimal = Population.population[0]
palabra = list(map(lambda x: x.value, optimal.value))
print("Palabra: " + str(palabra))

print("Score del bit optimo: " + str(round(optimal.score, 2)))
print("Tiempo demorado: %.10f segundos." % elapsed_time)
