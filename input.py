from models import City
def getInputFromFile():
    cities = []
    with open("input1.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                name,y,x = line.split(',')
                city = City(name,int(float(x)),int(float(y)))
                cities.append(city)
            except:
                print("Error in line: ",line)
           
    # for x in cities:
    #     print(x)
    return cities
