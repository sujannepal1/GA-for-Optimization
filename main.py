# function to optimize F = x**2+y**2-2*z**2+5*x*y*z+7
import random


A = 1
B = 1
C = 1
D = 1
initial_population = [
    [0, A, 4],
    [2, 1, 2],
    [10, D, 12],
    [3, 5, 14],
    [2, 15, B],
    [C, 5, 2],
]


# generate binary representation for variables x,y,z making a 16bit chromosome
def convert_to_binary(value: int) -> str:
    return format(value, "04b")


def to_decimal(b):
    return int(b, 2)


for i in range(len(initial_population)):
    x, y, z = initial_population[i]
    binary_x = convert_to_binary(x)
    binary_y = convert_to_binary(y)
    binary_z = convert_to_binary(z)
    chromosome = binary_x + binary_y + binary_z
    print(f"Individual {i + 1}: x={x}, y={y}, z={z}, Chromosome: {chromosome}")

POPULATION_SIZE = len(initial_population)

# finding the fitness of each individual in the population


def fitness_function(x: int, y: int, z: int) -> int:
    return x**2 + y**2 - 2 * z**2 + 5 * x * y * z + 7


highest_value = []
for i in range(POPULATION_SIZE):
    x, y, z = initial_population[i]
    fitness = fitness_function(x, y, z)
    print(f"Individual {i + 1}: x={x}, y={y}, z={z}, Fitness: {fitness}")
    highest_value.append(fitness)

max_fitness = max(highest_value)
min_fitness = min(highest_value)
print(f"Highest fitness value: {max_fitness}")
print(f"Lowest fitness value: {min_fitness}")

index_of_highest = highest_value.index(max_fitness)
index_of_lowest = highest_value.index(min_fitness)
random_indexes = [random.choice(range(POPULATION_SIZE)) for _ in range(2)]

final_indexes_for_crossover = [
    index_of_highest,
    index_of_highest,
    index_of_lowest,
] + random_indexes
print(f"Indexes selected for crossover: {final_indexes_for_crossover}")

# now two point crossover
