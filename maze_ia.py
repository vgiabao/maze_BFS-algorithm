#!/usr/bin/env python3
from sys import stdin, stdout, stderr
from Maze import Node
from Graph import Graph
import time


def get_data(player_name):
    content = input()
    p = Graph()
    y = 0
    while content != '':
        # stderr.write(str(content) + '\n\n')
        for x, value in enumerate(content):
            if value is player_name:
                p.add_batman(Node(x, y))
            elif value is 'o' or value is '!':
                p.add_target(Node(x, y))
            elif value is '#':
                p.add_trap(Node(x, y))
            elif value is not '':
                p.add_node(Node(x, y))
        y += 1
        content = input()
    return p


def finding_coin(player_name):
    content = get_data(player_name)
    list_moving2 = []
    dic = {'MOVE UP' : (0, -1), 'MOVE DOWN': (0, 1), 'MOVE RIGHT' : (1, 0),
           'MOVE LEFT': (-1, 0)}
    # stderr.write(str(content.batman) + '\n\n')
    list_moving = content.finding_valid()
    # for value in list_moving:
    #     stdout.write(str(value) + '\n\n')
    dis_x = list_moving[1].x - list_moving[0].x
    dis_y = list_moving[1].y - list_moving[0].y
    for item in dic:
        if dic[item] == (dis_x, dis_y):
            return item
    # return list_moving2


def read_input():
    steps = []
    while True:
        command = stdin.readline()
        if 'HELLO' in command:
            print('I AM BAO\n')
        elif 'YOU ARE' in command:
            player_name = command[-2]
            print('OK\n')
        elif 'MAZE' in command:
            steps = finding_coin(player_name)
            print(steps+'\n')
            pass


if __name__ == '__main__':
    read_input()
