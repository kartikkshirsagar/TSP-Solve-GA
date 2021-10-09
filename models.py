import math
class City:
    def __init__(self,name,x,y):
        self.name = name
        self.__x = x
        self.__y = y
    
    def printC(self):
        print("{0} located at {1},{2}".format(self.name,self.getX(),self.getY()))

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distanceFrom(self,otherCity):
        # return euclidean distance between cities
        return math.sqrt(( (self.getX() - otherCity.getX())**2 + (self.getY() - otherCity.getY())**2 ))

