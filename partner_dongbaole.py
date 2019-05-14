#!/usr/bin/env python3
from sys import stdin, stdout, stderr
from queue import Queue


class Agent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        stdin.readline()
        stdin.readline()
        stdout.write("I AM {name}\n\n".format(name=self.name))

        vm_answer = stdin.readline()
        self.name = vm_answer[-2]  # get player's name
        stdin.readline()
        stdout.write("OK\n\n")

    def read_maze(self):
        # read maze from vm
        maze = []

        stdin.readline()
        while True:
            line = stdin.readline()
            if line == "\n":
                break
            maze.append(line)

        return Maze(maze)

    def move(self, direction):
        # send player's move to vm
        stdout.write("MOVE {direction}\n\n".format(direction=direction))


class Maze:
    def __init__(self, maze=[[]]):
        self.map = maze

    def find_agent_location(self):
        for i in range(self.height()):
            for j in range(self.width()):
                if self.map[i][j] == player.name:
                    return Point(i, j)

    def height(self):
        return len(self.map)

    def width(self):
        return len(self.map[0])

    def get_value(self, location):
        return self.map[location.row][location.col]


class Point:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def get_direction(self, target):
        # get direction from the point to the target
        if target.row == self.row - 1:
            return "UP"
        if target.row == self.row + 1:
            return "DOWN"
        if target.col == self.col - 1:
            return "LEFT"
        if target.col == self.col + 1:
            return "RIGHT"


class Controller:
    def __init__(self, maze):
        self.maze = maze
        self.nearest_coin = None

    def bfs_nearest_coin(self, start):
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        queue_unvisited = Queue()  # keep track of points to be checked
        neighbour_points = {}

        agent_location = self.maze.find_agent_location()
        queue_unvisited.put(start)
        neighbour_points[start] = start  # init start point

        while not queue_unvisited.empty() and not self.nearest_coin:
            point = queue_unvisited.get()  # get point to check

            for direction in directions:
                neighbour = Point(point.row + direction[0],
                                  point.col + direction[1])
                if neighbour not in neighbour_points:
                    if self.maze.get_value(neighbour) == ' ':
                        neighbour_points[neighbour] = point

                        # add neighbour of node to queue
                        queue_unvisited.put(neighbour)

                    if self.maze.get_value(neighbour) in ['o', '!']:
                        # found nearest_coin
                        neighbour_points[neighbour] = point
                        self.nearest_coin = neighbour
                        break

        return neighbour_points

    def reconstruct_path(self, start):
        path = []
        neighbour_points = self.bfs_nearest_coin(start)
        last_location = self.nearest_coin

        path.append(last_location)
        while last_location is not start:
            neighbour = neighbour_points[last_location]  # backtracking 1 step
            path.append(neighbour)
            last_location = neighbour  # move

        return path


if __name__ == "__main__":
    player = Agent("A")
    player.greet()
    while True:
        maze = player.read_maze()
        agent_location = maze.find_agent_location()
        controller = Controller(maze)
        path = controller.reconstruct_path(agent_location)
        player.move(path[-1].get_direction(path[-2]))
