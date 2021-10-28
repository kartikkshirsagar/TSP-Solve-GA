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
    plt.title("Location of cities",fontsize=30)
    plt.savefig('cities.png')
    plt.clf()

def plot_cost(epochs,costs):
    fig = plt.figure(figsize=(10, 10))
    MOVING = 20
    temp = costs[:MOVING]
    avgs = [] + temp
    # avgs.append(np.mean(temp))
    for i in range(MOVING, len(costs)):
        temp.pop(0)
        temp.append(costs[i])
        avgs.append(np.mean(temp))
    # print(avgs)
    plt.plot(epochs,avgs,linestyle='--',color='r', label='{0}-epoch moving average'.format(MOVING))
    plt.plot(costs)
    plt.title("Cost graph of TSP (Cost vs epochs)")
    plt.xlabel("Number of epochs")
    plt.ylabel("Cost of the tour")
    plt.savefig('cost.png')
    plt.clf()
    fig = plt.figure(figsize=(10, 10))
    plt.plot(epochs,avgs,linestyle='--',color='r', label='{0}-epoch moving average'.format(MOVING))
    plt.title("Moving avg graph of TSP (AVG vs epochs)")
    plt.xlabel("Number of epochs")
    plt.ylabel("Cost of the tour")
    plt.savefig('avg.png')
    plt.clf()

def plot_route(route):
    X = [r.getX() for r in route]
    Y = [r.getY() for r in route]
    names = [r.name for r in route]
    fig = plt.figure(figsize=(25, 25))
    plt.plot(X,Y, marker='o', color='r')
    plt.title("The obtained min cost route",fontsize=30)
    for i, name in enumerate(names):
        plt.annotate(name, (X[i], Y[i]))
    plt.savefig('route.png')
    plt.clf()
