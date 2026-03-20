# function to optimize F = x**2+y**2-2*z**2+5*x*y*z+7
import random

ROLL_NUMBER = "25001"


def get_digit_from_roll_number(roll_number, position) -> int:
    return int(str(roll_number)[position])


A = get_digit_from_roll_number(ROLL_NUMBER, -4)
B = get_digit_from_roll_number(ROLL_NUMBER, -3)
C = get_digit_from_roll_number(ROLL_NUMBER, -2)
D = get_digit_from_roll_number(ROLL_NUMBER, -1)

print(f"A: {A}, B: {B}, C: {C}, D: {D}")

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


def fitness_function(x: int, y: int, z: int) -> int:
    return x**2 + y**2 - 2 * z**2 + 5 * x * y * z + 7


def evolve_population(initial_population):
    chromosomes = []
    for i in range(len(initial_population)):
        x, y, z = initial_population[i]
        binary_x = convert_to_binary(x)
        binary_y = convert_to_binary(y)
        binary_z = convert_to_binary(z)
        chromosome = binary_x + binary_y + binary_z
        chromosomes.append(chromosome)
        print(f"Individual {i + 1}: x={x}, y={y}, z={z}, Chromosome: {chromosome}")

    POPULATION_SIZE = len(initial_population)

    # finding the fitness of each individual in the population

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
    random_indexes = [random.choice(range(POPULATION_SIZE)) for _ in range(3)]

    final_indexes_for_crossover = [
        index_of_highest,
        index_of_highest,
        index_of_lowest,
    ] + random_indexes
    print(f"Indexes selected for crossover: {final_indexes_for_crossover}")

    new_population = []
    for i in final_indexes_for_crossover:
        new_population.append(initial_population[i])
    print("Selected population for crossover:")
    for i in range(len(new_population)):
        print(f"Individual {i + 1}: population: {new_population[i]}")

    # now two point crossover
    def two_point_crossover(parent1: str, parent2: str):
        point1 = random.randint(1, len(parent1) - 4)
        point2 = random.randint(point1 + 1, len(parent1) - 1)
        child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
        child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
        return child1, child2

    # mutation
    def mutate(chromosome: str, mutation_rate: float) -> str:
        new_chromosome = ""
        for gene in chromosome:
            if random.random() < mutation_rate:
                new_gene = "1" if gene == "0" else "0"
                new_chromosome += new_gene
                print(
                    "Mutation occurred at chromosome:"
                    + chromosome
                    + " -> "
                    + new_chromosome
                )
            else:
                new_chromosome += gene
        return new_chromosome

    new_population_chromosomes = []

    for i in new_population:
        x, y, z = i
        binary_x = convert_to_binary(x)
        binary_y = convert_to_binary(y)
        binary_z = convert_to_binary(z)
        chromosome = binary_x + binary_y + binary_z
        new_population_chromosomes.append(chromosome)

    offspring = []
    for i in range(0, len(new_population_chromosomes), 2):
        parent1 = new_population_chromosomes[i]
        parent2 = new_population_chromosomes[i + 1]
        child1, child2 = two_point_crossover(parent1, parent2)
        child1 = mutate(child1, 0.1)
        child2 = mutate(child2, 0.1)
        offspring.append(child1)
        offspring.append(child2)

    print("Offspring after crossover:")
    for i in range(len(offspring)):
        print(f"Offspring {i + 1}: Chromosome: {offspring[i]}")

    # calculate fitness of offspring
    final_population = []
    for i in range(len(offspring)):
        child = offspring[i]
        x = to_decimal(child[:4])
        y = to_decimal(child[4:8])
        z = to_decimal(child[8:])
        fitness = fitness_function(x, y, z)
        final_population.append((x, y, z))
        print(f"Offspring {i + 1}: x={x}, y={y}, z={z}, Fitness: {fitness}")

    return final_population


for i in range(2):
    final_pop = evolve_population(initial_population)
    final_pop = evolve_population(final_pop)
    final_pop = evolve_population(final_pop)

    fitness_value = []
    for individual in final_pop:
        x, y, z = individual
        fitness = fitness_function(x, y, z)
        fitness_value.append(fitness)
        print(f"Final Individual: x={x}, y={y}, z={z}, Fitness: {fitness}")

    max_fitness = max(fitness_value)
    index_of_max_fitness = fitness_value.index(max_fitness)
    best_individual = final_pop[index_of_max_fitness]
    print(
        f"Best Individual: x={best_individual[0]}, y={best_individual[1]}, z={best_individual[2]}, Fitness: {max_fitness}"
    )
