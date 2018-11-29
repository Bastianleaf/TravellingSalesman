from Main import Tools
from time import time
import random
#Parametros Globales
bit = "1001"
population_size = 25  #Individuos de poblacion
generations_number = 1
Population = Tools.generate_random_bits(population_size, len(bit), generations_number, bit)

# Algoritmo Principal
print("Calculando el bit...")
start_time = time()
while not Population.optimal:
	Population.evolution()
	
elapsed_time = time() - start_time

# Impresion de informacion
print("Generacion: " + str(Population.generation))
optimal = Population.population[0]
bits = list(map(lambda x: x.value, optimal.value))
print("Bits: " + str(bits))

print("Score del bit optimo: " + str(round(optimal.score, 2)))
print("Tiempo demorado: %.10f segundos." % elapsed_time)
