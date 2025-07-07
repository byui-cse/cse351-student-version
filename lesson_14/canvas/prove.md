# Assignment 14: Family Search using C#

## Overview

This is the same assignment from week 10.  However, this assignment is required to be written in C#.

There are a number of classes that you can use:

**Person**

This class will decode and hold person details sent from the server.

**Family**

This class holds the family information from the server.

**Tree**

The tree class allows you to build a family tree from the families and individuals that you retrieve from the server.

## Assignment

### Assignment files

- `server.py` - Python server for the assignment.  Run it in a terminal window or from VSCode.
- Folder `assignment14` - C# assignment project files
- `runs.txt` - Contains which search algorithms will be run and how many generations will be retrieved from the server.  You can modify this file while you are testing your program.

### FS Server

There is a server program that you will need to run in it's own terminal window on your computer.  The program is `server.py`.  

1. Open a command or terminal window on your computer.
1. Go to the directory of the assignment.
1. Type `python server.py` to start the server.
1. Note if the server is very busy it might not reply with a 200 reply code or might return an empty JSON.  You should handle these issues in your program.
1. There are two API calls that you will be making to build your tree.  The details are found in `functions.py`.

While running, the server will display requests and replies from your assignment.  It also displays the current number of active threads making requests and the maximum number of threads.

### Part 1

- The function `Solve.DepthFS()` will retrieve the family tree using a recursive algorithm.
- Your task is to use threads to make this function faster.  There is no limit on the number of threads you can use.
- You must build the pedigree tree starting with the starting family id.  You must write your program to handle different family information from the server (ie., number of families, number of children, etc.).  A family might be missing a parent and the number of children is random.
- You must retrieve all individuals in a family and add them to the tree object. (ie., husband, wife and children)
- Suggestion: get the function to work without using threads first.
- **Your goal is to execute part 1 in under 10 seconds for 6 generations**

### Part 2

- In this part, you will be retrieving the family information using a breadth-first algorithm in the function `Solve.BreathFS()`.
- Your goal is to make this function as fast as possible by using threads.
- You must retrieve all individuals in a family (ie., husband, wife and children)
- Do not use recursion for this algorithm.
- **Your goal is to execute part 2 in under 10 seconds for 6 generations**

### Misc

- The server will create a log file called `server.log`
- You assignment program will create a log file named `assignment.log`

## Submission

Assignments are individual and not team based.  Any assignments found to be plagiarised will be graded according to the `ACADEMIC HONESTY` section in the syllabus. The Assignment will be graded in broad categories as outlined in the syllabus:

- Upload the folowing files in canvas:
    - `Solve.cs`
    - `assignment.log`
- You must clearly show in your code that you are using DFS and BFS algorithms.

