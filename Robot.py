class Robot:

    __number = 0

    def __init__(self, N, Y):
        self.__ID = Robot.__number + 1
        self.name = N
        if type(Y) == int:
            self.__buildYear = Y
        else:
            raise TypeError("The build year must be an int")
        Robot.__number = Robot.__number + 1
        
    def __str__(self):
        return("Robot %s from %d " % (self.name, self.__buildYear))

    def printRobotAttributes(R):
        print("%s first appeared in %d" % (R.name, R.buildYear))

    def getNumber(self):
        return(Robot.__number)
    
    def getID(self):
        return(self.__ID)

robot1 = Robot("Marvin", 1978)
robot2 = Robot("WALL-E", 2008)

