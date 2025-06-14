"""
Course: CSE 351 
Assignment: 08 Prove Part 2
File:   prove_part_2.py
Author: <Add name here>

Purpose: Part 2 of assignment 8, finding the path to the end of a maze using recursion.

Instructions:
- Do not create classes for this assignment, just functions.
- Do not use any other Python modules other than the ones included.
- You MUST use recursive threading to find the end of the maze.
- Each thread MUST have a different color than the previous thread:
    - Use get_color() to get the color for each thread; you will eventually have duplicated colors.
    - Keep using the same color for each branch that a thread is exploring.
    - When you hit an intersection spin off new threads for each option and give them their own colors.

This code is not interested in tracking the path to the end position. Once you have completed this
program however, describe how you could alter the program to display the found path to the exit
position:

What would be your strategy?

I would have passed a path list as an argument to the move() function.
this list would store the path of each thread. when a thread reaches
the end it would print that threads path as each thread would have a 
copy of the path list that way they don't interfere with one another.

Why would it work?

Each thread would have its own unique path. Since each thread would have a copy
in each recurssive call each route is then tracked seperatly
and can determine the correct path by just displaying the thread that finished
since it would have the correct path list.

"""

import math
import threading 
from screen import Screen
from maze import Maze
import sys
import cv2

# Include cse 351 files
from cse351 import *

SCREEN_SIZE = 700
COLOR = (0, 0, 255)
COLORS = (
    (0,0,255),
    (0,255,0),
    (255,0,0),
    (255,255,0),
    (0,255,255),
    (255,0,255),
    (128,0,0),
    (128,128,0),
    (0,128,0),
    (128,0,128),
    (0,128,128),
    (0,0,128),
    (72,61,139),
    (143,143,188),
    (226,138,43),
    (128,114,250)
)
SLOW_SPEED = 100
FAST_SPEED = 0

# Globals
current_color_index = 0
thread_count = 0
stop = False
speed = SLOW_SPEED
path = []

def get_color():
    """ Returns a different color when called """
    global current_color_index
    if current_color_index >= len(COLORS):
        current_color_index = 0
    color = COLORS[current_color_index]
    current_color_index += 1
    return color


# TODO: Add any function(s) you need, if any, here.

def move(x , y, maze, color):
    global stop, thread_count

    if stop:
        return
    
    maze.move(x, y, color)
    if maze.at_end(x,y):
        stop = True
        return
    
    moves = maze.get_possible_moves(x,y)

    if len(moves) == 0:
        return
    
    elif len(moves) == 1:
        next_x, next_y = moves[0]
        move(next_x, next_y, maze, color)
    else:
        for i, (next_x, next_y) in enumerate(moves):
            if stop:
                break

            branch_color = color if i == 0 else get_color()
            t = threading.Thread(target=move, args =(next_x, next_y, maze, branch_color))
            thread_count += 1
            t.start()

            # if i == 0:
            #     move(next_x, next_y, maze, color)
            # else:
            #     new_color = get_color()
            #     t = threading.Thread(target=move, args =(next_x, next_y, maze, new_color))
            #     thread_count += 1
            #     t.start()

    # start = maze.get_start_pos()
    # path.append(start)
    # color = get_color()
    # maze.move(path[-1][0], path[-1][1], color)
    # possible = maze.get_possible_moves(path[-1][0], path[-1][1])
    # for paths in len(possible) - 1:
    #     t = threading.Thread()
    # # def split_moves()


def solve_find_end(maze):
    """ Finds the end position using threads. Nothing is returned. """
    # When one of the threads finds the end position, stop all of them.
    # global path
    global stop
    stop = False
    start_x, start_y = maze.get_start_pos()
    color = get_color()
    move(start_x, start_y, maze, color)

    # possible = maze.get_possible_moves()
    # start = maze.get_start_pos()
    # path.append(start)
    # maze.move(path[-1][0], path[-1][1])
    # possible = maze.get_possible_moves(path[-1][0], path[-1][1])
    # for paths in len(possible) - 1:
    #     t = threading.Thread()




def find_end(log, filename, delay):
    """ Do not change this function """

    global thread_count
    global speed

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename, delay=delay)

    solve_find_end(maze)

    log.write(f'Number of drawing commands = {screen.get_command_count()}')
    log.write(f'Number of threads created  = {thread_count}')

    done = False
    while not done:
        if screen.play_commands(speed): 
            key = cv2.waitKey(0)
            if key == ord('1'):
                speed = SLOW_SPEED
            elif key == ord('2'):
                speed = FAST_SPEED
            elif key == ord('q'):
                exit()
            elif key != ord('p'):
                done = True
        else:
            done = True


def find_ends(log):
    """ Do not change this function """

    files = (
        ('very-small.bmp', True),
        ('very-small-loops.bmp', True),
        ('small.bmp', True),
        ('small-loops.bmp', True),
        ('small-odd.bmp', True),
        ('small-open.bmp', False),
        ('large.bmp', False),
        ('large-loops.bmp', False),
        ('large-squares.bmp', False),
        ('large-open.bmp', False)
    )

    log.write('*' * 40)
    log.write('Part 2')
    for filename, delay in files:
        filename = f'./mazes/{filename}'
        log.write()
        log.write(f'File: {filename}')
        find_end(log, filename, delay)
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_ends(log)


if __name__ == "__main__":
    main()