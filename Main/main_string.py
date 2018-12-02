from Main import Tools
from time import time
import random

# Parametros Globales
palabra = "cat"
population_size = 500  # Individuos de poblacion
generations_number = 15
Population = Tools.generate_random_string(population_size, len(palabra), generations_number, palabra)

# ve 300 15
# Algoritmo Principal
print("Calculando la palabra...")
start_time = time()
while not Population.optimal:
	Population.evolution()

elapsed_time = time() - start_time

# Impresion de informacion
print("Generacion: " + str(Population.generation))
optimal = Population.best
print("Palabra: " + str(optimal))

print("Score de la palabra optima: " + str(round(Population.best_score, 2)))
print("Tiempo demorado: %.10f segundos." % elapsed_time)
