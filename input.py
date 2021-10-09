from models import City
def getInputFromFile():
    cities = []
    with open("input.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            name,y,x = line.split(',')
            city = City(name,float(x),float(y))
            cities.append(city)
    # for x in cities:
    #     print(x)
    return cities
