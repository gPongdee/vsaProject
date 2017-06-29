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
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.cleaned_tiles = []

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        if (int(pos.getX()),int(pos.getY())) not in self.cleaned_tiles:
            self.cleaned_tiles.append((int(pos.getX()),int(pos.getY())))

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (int(m),int(n)) in self.cleaned_tiles
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        m = random.random() * (self.width)
        n = random.random() * (self.height)
        return Position(m,n)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return ((0 <= pos.getX() < self.width)) and ((0 <= pos.getY() < self.height))

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        #self.position = self.room.getRandomPosition()
        self.position = Position(0,0)

        self.direction = random.randrange(360)

        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        new_pos = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(self.position)
        else:
            self.setRobotDirection(random.randrange(0, 360))

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
    results = []

    for i in range(0, int(num_trials)):
        anim = proj09_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        robots = []
        min_clean = round(room.getNumTiles() * min_coverage)
        for i in range(0, int(num_robots)):
            if robot_type == StandardRobot:
                robots.append(StandardRobot(room, speed))
            else:
                robots.append(RandomWalkRobot(room, speed))
        time = 0
        while room.getNumCleanedTiles() < min_clean:
            for robot in robots:
                robot.updatePositionAndClean()
            anim.update(room, robots)
            time += 1
        anim.done()
        results.append(time)

    ans = sum(results)/len(results)
    return ans



# === Problem 4
#
# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?
#
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 

    times = []
    for num_robots in range(1, 11):
        times.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 30, StandardRobot))
    pylab.plot(range(1,11), times)
    pylab.title("Number of Robots vs. Time to Clean 80% of 20x20 Room")
    pylab.xlabel("Number of robots")
    pylab.ylabel("Time to Clean 80% of 20x20 Room")
    pylab.show()

#showPlot1()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    rooms = [RectangularRoom(20, 20), RectangularRoom(25, 16), RectangularRoom(40, 10),
             RectangularRoom(50, 8), RectangularRoom(80, 5), RectangularRoom (100, 4)]

    ratios = []
    times = []
    for room in rooms:
        ratios.append(float(room.getWidth())/float(room.getHeight()))
        times.append(runSimulation(2, 1.0, room.getWidth(), room.getHeight(), 0.8, 100,
                                   StandardRobot))
    pylab.plot(ratios, times)
    pylab.title("Ratio of Width:Hieght of Room vs. Time to Clean 80% of Room")
    pylab.xlabel("Ratio of Width:Height of Room with Area 400")
    pylab.ylabel("Time to Clean 80% of Room with 2 Robots")
    pylab.show()

#showPlot2()


# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.setRobotDirection(random.randrange(0, 360))
        new_pos = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(self.position)


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    times1 = []
    times2 = []
    for num_robots in range(1, 11):
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 30, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 30, RandomWalkRobot))
    pylab.plot(range(1, 11), times1)
    pylab.plot(range(1, 11), times2)
    pylab.legend(("Standard Robot", "Random Walk Robot"))
    pylab.title("Number of Robots vs. Time to Clean 80% of 20x20 Room")
    pylab.xlabel("Number of robots")
    pylab.ylabel("Time to Clean 80% of 20x20 Room")
    pylab.show()

#showPlot3()



# testRoom = RectangularRoom(10, 5)
# # Call parts of self
# print testRoom.width
# print testRoom.height
#
# # Call def (function)
# testRoom.cleanTileAtPosition(Position(3, 4))
# print testRoom.isTileCleaned(4,4)

runSimulation(1, 1, 10, 10, 1, 1, StandardRobot)