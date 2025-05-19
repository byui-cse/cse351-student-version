""" 
Course: CSE 351
Lesson: L05 Team Activity
File:   team.py
Author: <Add name here>
Purpose: Find prime numbers

Instructions:

- Don't include any other Python packages or modules
- Review and follow the team activity instructions (team.md)
"""

from datetime import datetime, timedelta
import multiprocessing as mp
import random
from matplotlib.pylab import f, plt  # load plot library


# Include cse 351 common Python files
from cse351 import *

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def process_number(number):
    if is_prime(number):
        return number
    return None

def main():
    log = Log(show_terminal=True)
    log.start_timer()

    xaxis_cpus = []
    yaxis_times = []

    start = 10000000000
    range_count = 100000

    numbers = list(range(start, start + range_count + 1))

    for pool_size in range(1, mp.cpu_count() + 1):
        print(f'Pool of {pool_size:2} CPU cores', end='')
        xaxis_cpus.append(pool_size)
        with mp.Pool(pool_size) as pool:
            start_time = datetime.now()
            results = pool.map(process_number, numbers)
            end_time = datetime.now()
            elapsed_time = (end_time - start_time).total_seconds()
            print(f' took {elapsed_time:.2f} seconds')
            yaxis_times.append(elapsed_time)

    # create plot of results and also save it to a PNG file
    plt.plot(xaxis_cpus, yaxis_times)
    
    plt.title('Time VS CPUs')
    plt.xlabel('CPU Cores')
    plt.ylabel('Seconds')
    plt.legend(loc='best')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
