import matplotlib.pyplot as plt
import numpy as np
def plot_cities(cities):
    """
    Plot cities on a map.
    """
    fig = plt.figure(figsize=(10, 10))
    X = []
    Y = []
    names = []
    for city in cities:
        X.append(city.getX())
        Y.append(city.getY())
        names.append(city.name)
    plt.scatter(np.array(X), np.array(Y), s=10)
    for i, name in enumerate(names):
        plt.annotate(name, (X[i], Y[i]))
    plt.savefig('cities.png')

def plot_cost(X,Y):
    fig = plt.figure(figsize=(10, 10))
    plt.plot(X,Y)
    plt.savefig('cost.png')
