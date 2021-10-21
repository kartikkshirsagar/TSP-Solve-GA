import math
class City:
    def __init__(self,name,x,y):
        self.name = name
        self.__x = x
        self.__y = y
    def __eq__(self,other):
        if type(other) is not City:
            return False
        # print(self.__x ,other.getX())
        return self.name == other.name and self.__y == other.getY()

    def __hash__(self):
        return hash(self.name)
    def __str__(self):
        return "{0} located at {1},{2}".format(self.name,self.getX(),self.getY())
    def __repr__(self):
        return "{0}".format(self.name)

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distanceFrom(self,otherCity):
        # return euclidean distance between cities
        return math.sqrt(( (self.getX() - otherCity.getX())**2 + (self.getY() - otherCity.getY())**2 ))

