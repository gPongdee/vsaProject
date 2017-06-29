# proj09: Simulating robots
# Name:
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
        # Compute the change in position.
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)
    def __str__(self):
        return "<" +str(self.x) + ", "+ str(self.y)+">"
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
        self.cleaned = []


    
    def cleanTileAtPosition(self, pos):
        self.cleaned.append(pos)

    def isTileCleaned(self, m, n):
        for tile in self.cleaned:
            if m == tile.getX() and n == tile.getY():
                return True
        return False
    
    def getNumTiles(self):
        self.numtiles = self.width * self.height
        return self.numtiles

    def getNumCleanedTiles(self):
        return len(self.cleaned)

    def getRandomPosition(self):
        x = float(random.randint(0,self.width))
        y = float(random.randint(0, self.height))
        return Position(x, y)

    def isPositionInRoom(self, pos):
        x = pos.getX()
        y = pos.getY()
        if x >= 0 and x <= self.width and y >= 0 and y <= self.height:
            return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        self.room = room
        self.speed = float(speed)
        self.position = self.room.getRandomPosition()
        degrees = []
        for i in range(0, 361):
            degrees.append(i)
        direction = random.choice(degrees)
        self.direction = float(direction)
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """


    def getRobotPosition(self):
        return self.position
    
    def getRobotDirection(self):
        return self.direction

    def setRobotPosition(self, position):
        self.position = position

    def setRobotDirection(self):
        degrees = []
        for i in range(0, 361):
            degrees.append(i)
        direction = random.choice(degrees)
        self.direction = float(direction)

    '''def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError'''

class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):

        new_pos = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(new_pos) == False:
            self.setRobotDirection()
        else:
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(new_pos)

'''
room = RectangularRoom(10, 10)
robot1 = StandardRobot(room, 1.0)
v = 1
for step in range(10):
    print v
    robot1.updatePositionAndClean()
    print robot1.position
    print robot1.room.cleaned
    v = v + 1'''
# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    room=RectangularRoom(width, height)
    cleaned=[]
    for i in range(num_trials):
        while (len(cleaned)/room.getNumTiles()) < min_coverage:
            position= room.getRamdomPosition()


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
#	 20x0, 20x16, 40x10, 50x8, 80x5, and 1000x4?

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
