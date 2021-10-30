# TSP-Solve-GA
TSP solver using genetic algorithms.

## Crossover operator :
This application uses an operator which tries to take advantage of the problem properties.
The operator is defined as follows:
1) Think of a TSP solution in terms of a collection of edges from city(i) to city(i+1).
2) Get all the edges in which have their cost less than the median cost of edges in that solution and consider them as "good" edges.
3) Propagate these "good" edges to the respective children, and then fill the remaining cities in the same order as the other parent(which was not used for the good edges calculation).

This way you get a child which is a mixture of both the parents and the "good" edge concept comes from domain knowledge.

## Mutation Operator : 
This also uses some domain heuristic to mutate any individual.
1) Consider A,B,C and D as any 4 cities in the solution. (A,B,C,D are random integers and corresspond to the index of the *city* in the *cities* array).
2) A,B,C,D selected such that the solution has an edge A->B and C->D, in other words select i,j such that i!=j and then A=cities[i], B=cities[i+1], C = cities[j], D = cities[j+1].
3) Now if dist(A,B) + dist(C,D) > dist(A,C) + dist(B,D) then swap B with C.
4) I do this only once i.e. on only one set of (i,j) which is generated randomly.

## Selection : 
Every population is divided into two halves : Elites and non-Elites. Elites are the ones having better fitness values, and then only the elites are considered for the mating pool.

## Fitness function : 
Let the cost of a solution be C.(the summation of costs of all edges present in some TSP solution).
Ci is the cost of ith solution.


![CodeCogsEqn(2)](https://user-images.githubusercontent.com/42300545/139224356-6854ee69-af10-4050-a35a-f73f5562efe8.png)
