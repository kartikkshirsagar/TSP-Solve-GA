# TSP-Solve-GA
TSP solver using genetic algorithms.

## Crossover operator :
This application uses an operator which tries to take advantage of the problem properties.
The operator is defined as follows:
1) Think of a TSP solution in terms of a collection of edges from city(i) to city(i+1).
2) Get all the edges in which have their cost less than the median cost of edges in that solution and consider them as "good" edges.
3) Propagate these "good" edges to the respective children, and then fill the remaining cities in the same order as the other parent(which was not used for the good edges calculation).

This way you get a child which is a mixture of both the parents and the "good" edge concept comes from domain knowledge.
