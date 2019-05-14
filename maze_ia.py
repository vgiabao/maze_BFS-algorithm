#!/bin/python3
from sys import stdin, stdout, stderr
from Maze import Node
from Graph import Graph


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
    # stderr.write(str(content.batman) + '\n\n')
    list_moving = content.finding_valid()
    # for value in list_moving:
    #     stdout.write(str(value) + '\n\n')
    for item in list_moving:
        stderr.write(str(item)+'\n\n')
    return list_moving

def read_input():
    player_name = 'A'
    while True:
        command = stdin.readline()
        if 'HELLO' in command:
            stdout.write('I AM BAO\n\n')
        elif 'YOU ARE' in command:
            player_name = command[-2]
            stdout.write('OK\n\n')
        elif 'MAZE' in command:
            finding_coin(player_name)


if __name__ == '__main__':
    read_input()