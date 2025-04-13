"""
Course: CSE 351 
Lesson: L01 Team Activity
File:   team-solution.py
Author: Brother Comeau

Purpose: Find prime numbers.
"""

from datetime import datetime, timedelta
import threading
import random

# Include cse 351 common Python files
from cse351 import *

prime_count = 0
numbers_processed = 0

def is_prime(n: int):
    """Primality test using 6k+-1 optimization.
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


def process_range(start, end, thread_number, thread_count, lock_prime, lock_processed):
    global prime_count
    global numbers_processed
    for i in range(start + thread_number, end, thread_count):
        if is_prime(i):
            with lock_prime:
                prime_count += 1
            print(i, end=', ', flush=True)

        with lock_processed:
            numbers_processed += 1

def main():
    log = Log(show_terminal=True)
    log.start_timer()

    start = 10000000000

    # create random range count and number of threads    
    range_count = random.randint(100000, 110000)
    number_threads = random.randint(2, 10)

    numbers_processed = 0
    prime_count = 0

    log.start_timer()

    # Is there a critical section?  YES!!!! TWO of them!!!
    # the prime count variable AND numbers_processed
    lock_prime = threading.Lock()
    lock_processed = threading.Lock()

    threads = []

    # Create threads and give each one a start and step to test
    for i in range(number_threads):
        t = threading.Thread(target=process_range, args=(start, start + range_count, i, number_threads, lock_prime, lock_processed))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for them to finish
    for t in threads:
        t.join()

    log.write('')
    log.write(f'{range_count = }')
    log.write(f'{number_threads = }')
    log.write(f'Numbers processed = {numbers_processed}')
    log.write(f'Primes found = {prime_count}')
    log.stop_timer('Total time')

if __name__ == '__main__':
    main()
