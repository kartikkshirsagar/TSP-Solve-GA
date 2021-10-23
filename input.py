from models import City
from plot import plot_cities
def getInputFromFile():
    cities = []
    with open("input.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                name,y,x = line.split(',')
                city = City(name,int(float(x)),int(float(y)))
                cities.append(city)
            except:
                print("Error in line: ",line)
    plot_cities(cities)       
    # for x in cities:
    #     print(x)
    return cities
