from genetic_algo import fitness_function_calc, generate_random_population,fitness_function, generateChildPop, select_parents,INIT_POPULATION_SIZE
from input import getInputFromFile
from models import City
from plot import plot_cities, plot_cost
import copy

EPOCHS = 2500

def main():
    """
    Main function
    """
    src = City("Delhi",int(72.33),int(28.66))
    # Get input from file
    input_data = getInputFromFile()
    # Generate random population
    population = generate_random_population(INIT_POPULATION_SIZE,input_data,src)
    # Print population with probabilities
    probs = fitness_function(population)
    maxx = max(probs)
    # for i in range(len(probs)):
    #     if probs[i]==maxx:
            # print(population[i])
            # plot_cities(population[i])
    # print(probs)
    # print(population)
    # print(select_parents(population,probs))
    # given fitness values, population 
    # select parents and produce new population until termination condition is met
    costs = []
    for i in range(EPOCHS):
        
        children = generateChildPop(copy.deepcopy(population),probs,src)
        # for p in children:
        #     if p[0]!=src:
        #         print("IN LOOP")
        #         print(population)
        population = copy.deepcopy(children)
        costList = list(map(fitness_function_calc,copy.deepcopy(children)))
        minCost = min(costList)
        idx = costList.index(minCost)
        costs.append(minCost)
        print("epoch {0}, fitness - {1}, {2}".format(i,max(fitness_function(copy.deepcopy(children))),minCost))
    print(population[idx])
    plot_cost([i for i in range(EPOCHS)],costs)


if __name__=="__main__":
    main()