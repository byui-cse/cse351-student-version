""" 
Course: CSE 351
Lesson: L01 Team Activity
File:   team.py
Author: <Add name here>
Purpose: Find prime numbers

Instructions:

- Don't include any other Python packages or modules
- Review and follow the team activity instructions (team.md)

TODO 1) Get this program running.  Get cse351 package installed
TODO 2) move the following for loop into 1 thread
TODO 3) change the program to divide the for loop into 10 threads
TODO 4) change range_count to 100007.  Does your program still work?  Can you fix it?
Question: if the number of threads and range_count was random, would your program work?
"""

from datetime import datetime, timedelta
import threading
import random

# Include cse 351 common Python files
from cse351 import *

# Global variable for counting the number of primes found
prime_count = 0
numbers_processed = 0

def is_prime(n):
    """
        Primality test using 6k+-1 optimization.
        From: https://en.wikipedia.org/wiki/Primality_test
    """
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

def process_range(start, end, lock_prime, lock_processed):
    global prime_count
    global numbers_processed
    for i in range(start, end):
        if is_prime(i):
                with lock_prime:
                    prime_count += 1
            # print(i, end=', ', flush=True)
        with lock_processed:
            numbers_processed += 1


def main():
    # global prime_count                  # Required in order to use a global variable
    # global numbers_processed            # Required in order to use a global variable

    log = Log(show_terminal=True)
    log.start_timer()

    start = 10000000000
    range_count = 100000
    numbers_processed = 0
    number_threads = 10
    threads = []
    thread_range = range_count // number_threads

    lock_prime = threading.Lock()
    lock_processed = threading.Lock()

    for i in range(10):
        threadStart = start + (thread_range * i)
        threadEnd = threadStart + thread_range
        t = threading.Thread(target=process_range, args=(threadStart, threadEnd, lock_prime, lock_processed))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    
    # for i in range(start, start + range_count):
    #     numbers_processed += 1
    #     if is_prime(i):
    #         prime_count += 1
    #         print(i, end=', ', flush=True)
    print(flush=True)

    # Should find 4306 primes
    log.write(f'Numbers processed = {numbers_processed}')
    log.write(f'Primes found      = {prime_count}')
    log.stop_timer('Total time')


if __name__ == '__main__':
    main()
