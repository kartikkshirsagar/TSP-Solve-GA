#first step - generate a random initial population of N members
#second step - evaluate the fitness of each member of the population
# choose crossover function
import random
import copy

INIT_POPULATION_SIZE = 8
MUTATION_PROB = 0.7

def select_parents(population,fitness,src):
    parents = []
    fit = [1- w for w in fitness]
    flag=0
    
    for i in range(len(population)//2):
        parent_pair = random.choices(population,weights=fitness,k=2)
        # if parent_pair[0][0]!=src or parent_pair[1][0]!=src:
        #     print("HERE select parents")
        #     print(parent_pair)
        #     print("\n")
        #     print(population)
        #     # exit(0)
        while(parent_pair[0] == parent_pair[1]):
            parent_pair = random.choices(population,weights=fitness,k=2)
        parents.append(parent_pair)
    return parents

def crossoverPairWise(parents,src):
    # trying to implement two point crossover with replacement (TPXwR)
    # research paper source - https://www.scitepress.org/papers/2015/55902/55902.pdf
    p1 = parents[0]
    p2 = parents[1]
    child1 = [None]*len(p1)
    child2 = [None]*len(p2)
    low = random.randint(1,len(p1)-1)
    high = random.randint(low+1,len(p1))
    # low = 3
    # high = 7
    # print((low,high))
    # p1 can be divided into a,b and c and p2 can be divided into d,e and f
    # according to the above convention
    # [1,2,3,4,5,6,7,8] low = 3, high = 5
    # a = [1,2,3], b = [4,5], c = [6,7,8]
    a = p1[:low]
    b = p1[low:high]
    c = p1[high:]
    d = p2[:low]
    e = p2[low:high]
    f = p2[high:]
    # copy a and c to child1 exactly and copy d and f to child2
    child1[:low] = copy.deepcopy(a)
    child1[high:] = copy.deepcopy(c)
    child2[:low] = copy.deepcopy(d)
    child2[high:] = copy.deepcopy(f)
    # now the middle parts
    child1[low:high] = copy.deepcopy(e)
    toReplace = []
    for i in e:
        if i in a or i in c:
            toReplace.append(i)
    for i in toReplace:
        # replace with an element of d
        for j in d:
           if j not in child1:
                for x in range(low,high):
                    if child1[x] == i:
                        child1[x] = j
                        break
                break
        # if replacement did not happen in the above loop, then replace with an element of f
        for j in f:
            if j not in child1:
                for x in range(low,high):
                    if child1[x] == i:
                        child1[x] = j
                        break
                break
    # now for the second child
    child2[low:high] = copy.deepcopy(b)
    toReplace = []
    for i in b:
        if i in d or i in f:
            toReplace.append(i)
    for i in toReplace:
        # replace with an element of a
        for j in a:
           if j not in child2:
                for x in range(low,high):
                    if child2[x] == i:
                        child2[x] = j
                        break
                break
        # if replacement did not happen in the above loop, then replace with an element of c
        for j in c:
            if j not in child2:
                for x in range(low,high):
                    if child2[x] == i:
                        child2[x] = j
                        break
                break
    # if child1[0]!=src or child2[0]!=src:
    #     print("HERE crossover")
    #     print(parents)
    #     exit(0)
            
    return [child1,child2]

def fitness_function_calc(route):
        # given a route, calculate the cost incurred
        
        cost = 0
        for i in range(1,len(route)):
            cost += route[i].distanceFrom(route[i-1])
        cost+=route[-1].distanceFrom(route[0])
        return cost

def fitness_function(population):
    fitness_values = []
    fitness_values_scaled = []


    for i in range(len(population)):
        fitness_value = fitness_function_calc(population[i])
        fitness_values.append(1 / fitness_value)

    # scale it between 0 to 1
    sum_weights = sum(fitness_values)
    # print(weights)
    fitness_values_scaled = [(w / sum_weights) for w in fitness_values]  # Normalize weights
    return fitness_values
    
    
def generate_random_route(cities):
    return random.sample(cities,len(cities))


def generate_random_population(size,city_list,src):
    # generate population such that all individuals begin with src
    population = []
    for i in range(size):
        route = generate_random_route(city_list)
        route.remove(src) 
        route.insert(0,src) # add the source city at the beginning
        # if route[0]!=src:
        #     print("HERE generate random population")
        #     print(route)
        #     exit(0)
        population.append(route)
    # print(population)
    # for r in population:
    #     if r[0]!=src:
    #         print("IN RANDOM")
    return population

def generateChildPop(parentPop,fitnessValues,src):
    childPop = []
    flag=0
    for i in range(INIT_POPULATION_SIZE//2):
        parents = select_parents(copy.deepcopy(parentPop),fitnessValues,src)
        children = crossoverPairWise(copy.deepcopy(parents[i]),src)
        # if children[0][0]!=src or children[1][0]!=src:
        #     print("HERE generate child pop")
        #     print(children)
        #     exit(0)
        childrenMutated1 = mutate(copy.deepcopy(children[0]))
        childrenMutated2 = mutate(copy.deepcopy(children[1]))
        childPop.extend([childrenMutated1,childrenMutated2])
    for p in childPop:
        if p[0]!=src:
            print("IN GENERATE CHILD POP\n")
            flag=1
            print(childPop)
    return childPop




def mutate(population):
    # simple TWORS mutation which swaps any two cities
    prob = random.random()
    if prob<MUTATION_PROB:
        # print("Mutation occured")
        i = random.randint(1,len(population)-1)
        
        j = random.randint(1,len(population)-1)
        # if i==0 or j==0:
        #     print("NOOOOOOOOO")
        while(i==j):
            j = random.randint(1,len(population)-1)
        population[i],population[j] = population[j],population[i]
    return population 