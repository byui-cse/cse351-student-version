# Lesson 05 Team Teaching: Using mp.pool()

### Overview

You will be finding primes in a range of numbers.  This time, you will use mp.pool() to find those primes.

### Assignment

The main task is to use mp.pool().

### Files

- **team.py**: This is the team activity program file.  You will be writing your code here.

**Requirements**

- Convert the program to use processes
- Use mp.pool().  Remember that pool requires two arguments:
    - A function to process a number
    - A list of all numbers in a list
- use different number of processes for the pool.  Range of 1 to mp.cpu_count()
    - (ie., run with with 1 cpu, time the results, then add 1 to axis_cpus and time to yaxis_times, then run with 2 cpus, etc.  until you reach the max number of cpus)
- Keep track of the pool size and the time it took to process the numbers. plot the results

### Question

Why does your chart look the way it does?  Review [Amdahl's Law](https://en.wikipedia.org/wiki/Amdahl%27s_law).

### Sample Solution

When your program is finished, Here is a solution.  Compare them to your approach.

- [Solution](../team/team05-solution.py)

You should work to complete this team activity for the one hour period first, without looking at the sample solution. However, if you have worked on it for at least an hour and are still having problems, you may feel free to use the sample solution to help you finish your program.

### Submission

When complete, please report your progress in the associated Canvas quiz.



