from genetic_algo import *
from models import *

def uniquenessTests():
    pop = [1,2,3,4,5,6,7,8]
    ct=0
    ct1=0
    for i in range(100):
        random.shuffle(pop)
        parents = []
        parents.append(copy.deepcopy(pop))
        random.shuffle(pop)
        parents.append(copy.deepcopy(pop))
        children = heuristicBasedCrossover(parents,City('Delhi',0,0))
        if len(set(children[0])) == len(children[0]):
            ct+=1
        if len(set(children[1])) == len(children[1]):
            ct1+=1
    if ct == 100 and ct1 == 100:
        print("Uniqueness test passed")
    else:
        print("Uniqueness test failed")    

uniquenessTests()    
