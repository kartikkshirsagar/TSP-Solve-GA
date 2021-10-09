from genetic_algo import generate_random_population,fitness_function, select_parents
from input import getInputFromFile
from plot import plot_cities

INIT_POPULATION_SIZE = 4


def main():
    """
    Main function
    """
    # Get input from file
    input_data = getInputFromFile()
    # Generate random population
    population = generate_random_population(INIT_POPULATION_SIZE,input_data)
    # Print population with probabilities
    probs = fitness_function(population)
    maxx = max(probs)
    for i in range(len(probs)):
        if probs[i]==maxx:
            # print(population[i])
            plot_cities(population[i])
    print(probs)
    print(population)
    print(select_parents(population,probs))


if __name__=="__main__":
    main()