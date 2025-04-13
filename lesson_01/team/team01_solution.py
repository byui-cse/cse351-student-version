"""
Course: CSE 351 
Lesson: L01 Team Activity
File:   team-solution.py
Author: Brother Comeau

Purpose: Find prime numbers.
"""

from datetime import datetime, timedelta
import threading


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


def process_range(start, end, lock_prime, lock_processed):
    global prime_count
    global numbers_processed
    for i in range(start, end):
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
    range_count = 100000

    # Is there a critical section?  TWO of them!!
    # the prime count variable AND numbers_processed
    lock_prime = threading.Lock()
    lock_processed = threading.Lock()

    number_threads = 10
    threads = []
    thread_range = range_count // number_threads

    # Create threads and give each one a range to test
    for i in range(10):
        thread_start = start + (thread_range * i)
        thread_end = thread_start + thread_range
        t = threading.Thread(target=process_range, args=(thread_start, thread_end, lock_prime, lock_processed))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for them to finish
    for t in threads:
        t.join()

    # Should find 4306 primes
    log.write('')
    log.write(f'{range_count = }')
    log.write(f'{number_threads = }')
    log.write(f'Numbers processed = {numbers_processed}')
    log.write(f'Primes found = {prime_count}')
    log.stop_timer('Total time')


if __name__ == '__main__':
    main()
