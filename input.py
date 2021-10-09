from models import City
def getInputFromFile():
    cities = []
    with open("input.txt","r") as f:
        line = f.readline()
        name,x,y = line.split()
        city = City(name,x,y)
        cities.append(city)
    for x in cities:
        x.printC()


getInputFromFile()