from GeneticPopulation import GeneticPopulation
from Gen import *
PopA = GeneticPopulation(generate_random_bits(10, 5))
PopA.evolution("10000")
