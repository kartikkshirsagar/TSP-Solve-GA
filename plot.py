import matplotlib.pyplot as plt
import numpy as np
def plot_cities(cities):
    """
    Plot cities on a map.
    """
    fig = plt.figure(figsize=(20, 20))
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
    fig = plt.figure(figsize=(20, 20))
    plt.plot(X,Y)
    plt.savefig('cost.png')

def plot_route(route):
    X = [r.getX() for r in route]
    Y = [r.getY() for r in route]
    names = [r.name for r in route]
    fig = plt.figure(figsize=(20, 20))
    plt.plot(X,Y)
    for i, name in enumerate(names):
        plt.annotate(name, (X[i], Y[i]))
    plt.savefig('route.png')
