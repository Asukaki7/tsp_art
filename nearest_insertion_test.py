

# Required Libraries
import pandas as pd

# GA
from pyCombinatorial.algorithm import genetic_algorithm
from pyCombinatorial.utils import graphs, util

# Loading Coordinates # Berlin 52 (Minimum Distance = 7544.3659)
coordinates = pd.read_csv('https://bit.ly/3Oyn3hN', sep = '\t')
coordinates = coordinates.values

# Obtaining the Distance Matrix
distance_matrix = util.build_distance_matrix(coordinates)

# GA - Parameters
parameters = {
            'population_size': 15,
            'elite': 1,
            'mutation_rate': 0.1,
            'mutation_search': 8,
            'generations': 1000,
            'verbose': True
             }

# GA - Algorithm
route, distance = genetic_algorithm(distance_matrix, **parameters)

# Plot Locations and Tour
graphs.plot_tour(coordinates, city_tour = route, view = 'browser', size = 10)
print('Total Distance: ', round(distance, 2))
