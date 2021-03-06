from Maze import Node
from sys import stderr, stdout


class Graph:
    def __init__(self):
        self.nodes = []
        self.batman = ''
        self.target = []
        self.near_list = ((1, 0), (-1, 0), (0, -1), (0, 1))
        self.trap = []

    def add_trap(self, node):
        self.trap.append(node)

    def add_node(self, node):
        self.nodes.append(node)

    def add_batman(self, node):
        self.batman = node

    def add_target(self, node):
        self.target.append(node)

    def check_valid(self, point, checked_point):
        valid_list = []
        for i, j in self.near_list:
            near_x = point.x + i
            near_y = point.y + j
            if Node(near_x, near_y) not in self.trap:
                if Node(near_x, near_y) not in checked_point:
                    valid_list.append(Node(near_x, near_y))
        return valid_list

    def finding_valid(self):
        checked_point = set([self.batman])
        valid_route = [self.batman]
        for extension in self.check_valid(self.batman, checked_point):
            valid_route.append([self.batman]+ [extension])
        checked_point.add(self.batman)
        valid_route.pop(0)
        for route in valid_route:
            if route[-1] in self.target:
                return route
        while True:
            for extension in self.check_valid(valid_route[0][-1], checked_point):
                valid_route.append(valid_route[0]+[extension])
                if extension in self.target:
                    return valid_route[-1]
            valid_route.pop(0)
            checked_point.add(valid_route[0][-1])
