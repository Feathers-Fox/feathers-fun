# proj09: Simulating robots
# Name: ariana and bonnie SAVED
# Date:

import math
import random

import proj09_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        area = width*height
        dirtylist = []
        self.cleanedlist = []
        #
        # """
        # Initializes a rectangular room with the specified width and height.
        #
        # Initially, no tiles in the room have been cleaned.
        #
        # width: an integer > 0
        # height: an integer > 0
        # """
    
    def cleanTileAtPosition(self, pos):
        x = pos.getX()
        y = pos.getY()

        self.cleanedlist.append((x, y))
        print "we added a position to the list of clean tiles. It's ", (x, y)
        print "the list of clean tiles is now: ", self.cleanedlist

        # """
        # Mark the tile under the position POS as cleaned.
        #
        # Assumes that POS represents a valid position inside this room.
        #
        # pos: a Position

        # """

    def isTileCleaned(self, m, n):
        self.m = m
        self.n = n

        if (m, n) in self.cleanedlist:
            print "The tile is clean!"
            print "the list of cleaned tiles after we run isTileCleaned and returning True is ", self.cleanedlist
            return True
        else:
            print "The tile is not clean!"
            print "the list of cleaned tiles after we run isTileCleaned and returning False is ", self.cleanedlist
            return False

        # """
        # Return True if the tile (m, n) has been cleaned.
        #
        # Assumes that (m, n) represents a valid tile inside the room.
        #
        # m: an integer
        # n: an integer
        # returns: True if (m, n) is cleaned, False otherwise
        # """
    
    def getNumTiles(self):
        return int(area)
        # """
        # Return the total number of tiles in the room.
        #
        # returns: an integer
        # """


    def getNumCleanedTiles(self):

        # tilenumber = 0
        # while len(self.cleanedlist) <= self.width*self.height:
        #     self.cleanedlist.append(self.number)
        #     tilenumber = tilenumber + 1
        #     asdf = int(len(self.cleanedlist - 1))
        # print asdf
        # return asdf
        return len(self.cleanedlist)

        # """
        # Return the total number of clean tiles in the room.
        #
        # returns: an integer
        # """


    def getRandomPosition(self):

        allnumbersw = []
        allnumbersh = []


        for item in range(0, self.width):
            allnumbersw.append(item)

        for item2 in range(0, self.height):
            allnumbersh.append(item2)
        randomw = random.choice(allnumbersw)
        randomh = random.choice(allnumbersh)
        return (randomw, randomh)





        # """
        # Return a random position inside the room.
        #
        # returns: a Position object.
        # """


    def isPositionInRoom(self, pos):
        if pos.getX() < self.width and pos.getY() < self.height:
            print "alsotrue"
            return True
        raise NotImplementedError
        # """
        # Return True if pos is inside the room.
        #
        # pos: a Position object.
        # returns: True if pos is in the room, False otherwise.
        # """


room = RectangularRoom(10,10)
print room.getNumCleanedTiles()
print room.cleanTileAtPosition(Position(4,5))
print room.isTileCleaned(4,5)
print room.getNumCleanedTiles()
print room.getRandomPosition()
print room.isPositionInRoom(Position(4, 5))



class Robot(object):

    # """
    # Represents a robot cleaning a particular room.
    #
    # At all times the robot has a particular position and direction in the room.
    # The robot also has a fixed speed.
    #
    # Subclasses of Robot should provide movement strategies by implementing
    # updatePositionAndClean(), which simulates a single time-step.
    # """
    def __init__(self, room, speed):
        self.room = room
        self.speed = speed
        self.position= self.room.getRandomPosition()
        self.direction = 0

        #cleanTileAtPosition(x, y)

        # """
        # Initializes a Robot with the given speed in the specified room. The
        # robot initially has a random direction and a random position in the
        # room. The robot cleans the tile it is on.
        #
        # room:  a RectangularRoom object.
        # speed: a float (speed > 0)
        # """
        # raise NotImplementedError

    def getRobotPosition(self):
        #print "yayiusdfishfsak"
        return self.position
        # "
        # Return the position of the robot.
        #
        # returns: a Position object giving the robot's position.
        # """


    def getRobotDirection(self):
        dlist = []

        for degrees in range(0, 361):
            dlist.append(degrees)

        randomd = random.choice(dlist)
        #print dlist
        print "the randomly generated direction/degree is", randomd
        return randomd
        # """
        # Return the direction of the robot.
        #
        # returns: an integer d giving the direction of the robot as an angle in
        # degrees, 0 <= d < 360.
        # """
    def setRobotPosition(self, position):
        position = wally.getRobotPosition()
        print "blaaaaaaa", position
        return position
        # """
        # Set the position of the robot to POSITION.
        #
        # position: a Position object.
        # """
    def setRobotDirection(self, direction):

        direction = wally.getRobotDirection()
        print "glaaaaaaaa", direction
        return direction

        # """
        # Set the direction of the robot to DIRECTION.
        # direction: integer representing an angle in degrees
        # """

    def updatePositionAndClean(self):

        raise NotImplmementedError

        # """
        # Simulate the raise passage of a single time-step.
        # Move the robot to a new position and mark the tile it is on as having
        # been cleaned.
        # """

wally = Robot(room, 1)
print "wally's speed is ", wally.speed
print "wally's randomly-generated location is ", wally.getRobotPosition()
print wally.getRobotDirection()
print wally.setRobotPosition(Position(wally, Position))
print wally.setRobotDirection(Position(wally, Position))
#print wally.updatePositionAndClean()
# === Problem 2

class StandardRobot(Robot):


    # """
    # A StandardRobot is a Robot with the standard movement strategy.
    #
    # At each time-step, a StandardRobot attempts to move in its current direction; when
    # it hits a wall, it chooses a new direction randomly.
    # """
    def updatePositionAndClean(self):
        # """
        # Simulate the passage of a single time-step.
        #
        # Move the robot to a new position and mark the tile it is on as having
        # been cleaned.
       # """





        newposition = getNewPosition(self, angle, speed)
        angle = self.getRobotDirection()
        self.cleanTileAtPosition(getRobotPosition())
        newdirection = self.setRobotDirection()
        currentposition = self.getRobotPosition()
        newposition = self.setRobotPosition(Position(SirWallace, Position))

        currentposition = newposition in currentdirection
        for self.x, self.y in currentposition:
            if self.x > self.width or self.y > self.height:
                currentdirection = newdirection
        print "a,fdflsalieuil"
        return self.cleanedlist
        raise NotImplementedError

        #
        # """
        # Computes and returns the new Position after a single clock-tick has
        # passed, with this object as the current position, and with the
        # specified angle and speed.
        #
        # Does NOT test whether the returned position fits inside the room.
        #
        # angle: float representing angle in degrees, 0 <= angle < 360
        # speed: positive float representing speed
        #
        # Returns: a Position object representing the new position.
        # """

SirWallace = StandardRobot(room, 1)
print SirWallace.updatePositionAndClean()
# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    raise NotImplementedError


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    raise NotImplementedError

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    raise NotImplementedError

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    raise NotImplementedError


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    raise NotImplementedError
