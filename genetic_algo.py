#first step - generate a random initial population of N members
#second step - evaluate the fitness of each member of the population
# choose crossover function
import random
import copy

def select_parents(population,fitness):
    parents = []
    for i in range(len(population)//2):
        parent_pair = random.choices(population,weights=fitness,k=2)
        parents.append(parent_pair)
    
    return parents

def crossover(parents):
    # trying to implement two point crossover with replacement (TPXwR)
    # research paper source - https://www.scitepress.org/papers/2015/55902/55902.pdf
    p1 = parents[0]
    p2 = parents[1]
    child1 = [None]*len(p1)
    child2 = [None]*len(p2)
    low = random.randint(1,len(p1)//2)
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
    return [child1,child2]

def fitness_function(population):
    fitness_values = []
    fitness_values_scaled = []

    def fitness_function_calc(route):
        # given a route, calculate the cost incurred
        
        cost = 0
        for i in range(1,len(route)):
            cost += route[i].distanceFrom(route[i-1])
        cost+=route[-1].distanceFrom(route[0])
        return cost

    for i in range(len(population)):
        fitness_value = fitness_function_calc(population[i])
        fitness_values.append(fitness_value)

    # scale it between 0 to 1
    weights = [1.0 / w for w in fitness_values]           # Invert all weights
    sum_weights = sum(weights)
    # print(weights)
    fitness_values_scaled = [w / sum_weights for w in weights]  # Normalize weights
    return fitness_values_scaled
    
    
def generate_random_route(cities):
    return random.sample(cities,len(cities))


def generate_random_population(size,city_list):
    population = []
    for i in range(size):
        population.append(generate_random_route(city_list))
    return population
