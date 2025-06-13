# Assignment 08: Finding Paths in a Maze

### Overview

You will complete your two part program to find a path through a maze.

### Project Description

You will be finding a path between the start and end positions in a maze. In the image below, the starting position is in the top-left and the ending position the bottom-right.

![](./assets/maze.png)

There are two classes included in the assignment that you will be using.

**Maze**

This holds the maze of the program. It is given a bitmap image of the maze that represents walls and walkable spaces. You are able to get a lot of information about individual cells and the maze from this class. Please refer to the `maze.py` file for the methods that can be used.

**Screen**

This class is used by the Maze to save drawing commands while the program is finding a path or looking for the ending position. The reason for this class is that only the main thread can draw to the screen. Therefore, this class will save all of the drawing commands until asked to display them in your program. You should not need to look at this code for your assignment.

### Assignment

The assignment is broken into 2 sections.

### Part 1 - Find a Path

[Video Example of Finding a Path](./assets/find_path.mp4)

The file `prove_part_1.py` contains the starting point for this part of the assignment. There are functions that you are not allowed to change so make sure you note which ones they are.

The goal of this part of the assignment is to use recursion to find a path from the start to the exit. In the above video, you can see that if you need to backtrack because a path is a dead end, you indicate the locations that you have been with the grey color. Review the Maze class on the methods that you can call.

In this part of the assignment, the base case of the recursion is finding the end exit position. Review recursion from the links at the end of this page if you need help remediating your recursive programming skills.

Here is a sample run (log file) of part 1. For some of the mazes, your values will/might be different.

```
19:22:21| ****************************************
19:22:21| Part 1
19:22:21|
19:22:21| File: ./mazes/very-small.bmp
19:22:21| Drawing commands to solve = 88
19:22:22| Found path has length     = 11
19:22:22|
19:22:22| File: ./mazes/very-small-loops.bmp
19:22:22| Drawing commands to solve = 352
19:22:23| Found path has length     = 55
19:22:23|
19:22:23| File: ./mazes/small.bmp
19:22:23| Drawing commands to solve = 1360
19:22:24| Found path has length     = 79
19:22:24| 
19:22:24| File: ./mazes/small-loops.bmp
19:22:24| Drawing commands to solve = 1600
19:22:25| Found path has length     = 159
19:22:25| 
19:22:25| File: ./mazes/small-odd.bmp
19:22:25| Drawing commands to solve = 2536
19:22:26| Found path has length     = 79
19:22:26| 
19:22:26| File: ./mazes/small-open.bmp
19:22:26| Drawing commands to solve = 2496
19:22:27| Found path has length     = 319
19:22:27| 
19:22:27| File: ./mazes/large.bmp
19:22:27| Drawing commands to solve = 41984
19:22:28| Found path has length     = 1299
19:22:28| 
19:22:28| File: ./mazes/large-loops.bmp
19:22:28| Drawing commands to solve = 46064
19:22:29| Found path has length     = 803
19:22:29| ****************************************
```

### Part 2 - Find the End Position or Exit

[Video Example of Finding the End Position](./assets/find_end_position.mp4)

The file `prove_part_2.py` contains the starting point for this part of the assignment. There are functions that you are not allowed to change, pay attention!

In part 2 of the assignment, you will be using threads to find the exit position. You are not required to return a path from start to end like part 1.

When a thread comes to a fork or division in the maze, it will create a thread for each path except for one. The thread that found the fork in the path will take one of the paths. The other paths will be searched by the newly created threads. When one of the threads finds the end position, that thread needs to stop all other threads. Recursion is required for this part of the assignment.

In the example image below, the red thread starts the maze. It moves along until it comes to a fork. It created a thread (color blue) and that new thread continued down one of the paths. The red thread continues down the other path. Note that in some of the mazes, there can be 3 different paths at a fork.

In the sample below, there are a total of 7 threads created. In this example, the orange colored thread found the exit position. When that happens, it needs to tell the other threads to stop. **In order to receive full points for this part of the assignment, threads need to be moving through the maze concurrently.** Watch the video above to see an example.

In the header section of the Python file, are 2 questions that you are required to be answer as well.

![](./assets/maze-threads.png)

Here is a example log file output. Your values might/will be different for some mazes.

```
20:29:29| ****************************************
20:29:29| Part 2
20:29:29|
20:29:29| File: ./mazes/very-small.bmp
20:29:29| Number of drawing commands = 84
20:29:29| Number of threads created  = 3
20:29:32| 
20:29:32| File: ./mazes/very-small-loops.bmp
20:29:33| Number of drawing commands = 322
20:29:33| Number of threads created  = 7
20:29:35| 
20:29:35| File: ./mazes/small.bmp
20:29:40| Number of drawing commands = 1740
20:29:40| Number of threads created  = 21
20:29:41| 
20:29:41| File: ./mazes/small-loops.bmp
20:29:49| Number of drawing commands = 2052
20:29:49| Number of threads created  = 33
20:29:50| 
20:29:50| File: ./mazes/small-odd.bmp
20:29:58| Number of drawing commands = 2174
20:29:58| Number of threads created  = 153
20:30:00|
20:30:00| File: ./mazes/small-open.bmp
20:30:00| Number of drawing commands = 3010
20:30:00| Number of threads created  = 351
20:30:01|
20:30:01| File: ./mazes/large.bmp
20:30:01| Number of drawing commands = 30936
20:30:01| Number of threads created  = 356
20:30:03|
20:30:03| File: ./mazes/large-loops.bmp
20:30:03| Number of drawing commands = 29580
20:30:03| Number of threads created  = 464
20:30:04| ****************************************
```

### Links on Recursion:

If you need help understanding recursion or need to refresh your memory on how it works, please review these links:

- [Recursion (computer science)](https://en.wikipedia.org/wiki/Recursion_\(computer_science\))
- [Recursion in Python](https://realpython.com/python-thinking-recursively/#recursive-functions-in-python)
- [Understanding Recursion](https://stackabuse.com/understanding-recursive-functions-with-python/)
- [Video on Recursion](https://www.youtube.com/watch?v=ngCos392W4w)
- [What on Earth is Recursion? - Computerphile](https://www.youtube.com/watch?v=Mv9NEXX1VHc)

### Software Module Requirements

If not already install on your computer, you must install the module `opencv`. Use the same technique that you used to install `numpy` and `matplotlib`. The module's name is `opencv-python`.

```
<path of python> -m pip install opencv-python
```

### Rubric

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit. Assignments are individual and not team based. Any assignments found to be plagiarized will be graded according to the `ACADEMIC HONESTY` section in the syllabus. The Assignment will be graded in broad categories as outlined in the syllabus.

### Submission

Submit your Python files (`prove_part_1.py` and `prove_part_2.py`) to Canvas for feedback. You should add a submission comment that specifies the grading category that best describes your assignment along with a 1-2 sentence justification for your choice. The grading criteria discussed in the syllabus.

**DO NOT FORGET** to answer the questions at the top of the `prove_part_2.py` file.