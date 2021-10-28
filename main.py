from genetic_algo import checkConvergence, fitness_function_calc, generate_random_population,fitness_function, generateChildPop, select_parents,INIT_POPULATION_SIZE
from input import getInputFromFile
from models import City
from plot import plot_cities, plot_cost, plot_route
import copy

EPOCHS = 2500
CONVERGENCE_VALUE = 12
def main():
    """
    Main function
    """
    src = City("Delhi",int(72.33),int(28.66))
    # Get input from file
    input_data = getInputFromFile()
    best_route = []
    best_cost = 9999999999
    for run in range(5):
        print("RUN1")
        # Generate random population
        population = generate_random_population(INIT_POPULATION_SIZE,input_data,src)
        # Print population with probabilities
        probs = fitness_function(population)
        # maxx = max(probs)
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
        last_costs = [None]*CONVERGENCE_VALUE
        k = 0
        for i in range(EPOCHS):
            if i > CONVERGENCE_VALUE:
                if checkConvergence(last_costs): 
                    # plot_cost([j for j in range(k)],costs)
                    # plot_route(population[idx])
                    if best_cost> minCost:
                        best_cost = minCost
                        best_route = population[idx]
                        plot_cost([i for i in range(k)],costs)
                    break
            children = generateChildPop(copy.deepcopy(population),probs,src)
            population = copy.deepcopy(children)
            costList = list(map(fitness_function_calc,copy.deepcopy(children)))
            minCost = min(costList)
            idx = costList.index(minCost)
            costs.append(minCost)
            print("epoch {0}, fitness - {1}, {2}".format(i,max(fitness_function(copy.deepcopy(children))),minCost))
            last_costs[i%CONVERGENCE_VALUE] = minCost
            k+=1
            if best_cost> minCost:
                best_cost = minCost
                best_route = population[idx]
                plot_cost([i for i in range(k)],costs)
        # print(population[idx])
        # print(population)
        
    print(best_cost)
    print(best_route)
    plot_route(best_route)
    
if __name__=="__main__":
    main()