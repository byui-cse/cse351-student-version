# Week 10 Team Teach: Merge Sort

### Overview

The [merge sort](https://en.wikipedia.org/wiki/Merge_sort) is "an efficient, general-purpose, comparison-based sorting algorithm."

### Assignment

The code provided to you in the [team.py](../team/team.py) file contains a working merge function that sorts 1,000,000 numbers in a list. We have configured the file to automatically run and report on three different implementations of the merge sort. One will be the standard merge sort that we provided for you, one will be merge sort done by threads, and one will be merge sort done by processes.

You will be changing the program to add the two missing implementations:

1. Implement the function `merge_sort_thread()` to use threads in the recursion. When your merge function makes a recursive call to itself, you will create a new thread to handle that function.
2. Implement the function `merge_sort_process()` to use processes in the recursion. When your merge function makes a recursive call to itself, you will create a new process to handle that function.

### Sample Solution

We will go over the solution in the last class of this week.

### Submission

When complete, please report your progress in the associated Canvas quiz. If you decided to do additional work on the program after your team activity, either by yourself or with others, feel free to include that additional work when you report on your progress in Canvas.
