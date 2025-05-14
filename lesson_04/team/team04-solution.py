""" 
Course: CSE 351
Team  : Week 04
File  : team04-solution.py
Author: Brother Comeau

See instructions in canvas for this team activity.

"""

import random
import threading

# Include CSE 351 common Python files. 
from cse351 import *
from matplotlib.pyplot import bar

# Constants
MAX_QUEUE_SIZE = 10
PRIME_COUNT = 1000
FILENAME = 'primes.txt'
PRODUCERS = 3
CONSUMERS = 5

# ---------------------------------------------------------------------------
def is_prime(n: int):
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

# ---------------------------------------------------------------------------
class Queue351():
    """ This is the queue object to use for this class. Do not modify!! """

    def __init__(self):
        self.__items = []
   
    def put(self, item):
        assert len(self.__items) <= 10
        self.__items.append(item)

    def get(self):
        return self.__items.pop(0)

    def get_size(self):
        """ Return the size of the queue like queue.Queue does -> Approx size """
        extra = 1 if random.randint(1, 50) == 1 else 0
        if extra > 0:
            extra *= -1 if random.randint(1, 2) == 1 else 1
        return len(self.__items) + extra

# ---------------------------------------------------------------------------
def producer(id, que, empty_slots, full_slots, barrier):
    for i in range(PRIME_COUNT):
        number = random.randint(1, 1_000_000_000_000)

        # must acquire an empty slot before putting
        empty_slots.acquire()
        que.put(number)

        # must release a full slot after putting
        full_slots.release()

    # wait for all producers to finish
    barrier.wait()

    # TODO - select one producer to send the "All Done" message
    if id == 0:
        for _ in range(CONSUMERS):
            empty_slots.acquire()
            que.put(None)
            full_slots.release()

# ---------------------------------------------------------------------------
def consumer(que, empty_slots, full_slots, filename):
    while True:
        # must acquire a full slot before getting
        full_slots.acquire()
        number = que.get()

        # must release an empty slot after getting
        empty_slots.release()

        if number is None:
            break

        if is_prime(number):
            print(f"Found prime: {number}")
            with open(filename, 'a') as f:
                f.write(f"{number}\n")

# ---------------------------------------------------------------------------
def main():

    random.seed(102030)

    # clear the file
    with open(FILENAME, 'w') as f:
        ...  

    que = Queue351()

    # create semaphores for the queue (see Queue351 class)
    # Note: the values of the two semaphores MUST ALWAYS be MAX_QUEUE_SIZE
    empty_slots = threading.Semaphore(MAX_QUEUE_SIZE)
    full_slots = threading.Semaphore(0)

    # create barrier
    barrier = threading.Barrier(PRODUCERS)

    # create producers threads (see PRODUCERS value)
    producers = []
    for i in range(PRODUCERS):
        p = threading.Thread(target=producer, args=(i, que, empty_slots, full_slots, barrier))
        p.start()
        producers.append(p)

    # create consumers threads (see CONSUMERS value)
    consumers = []
    for i in range(CONSUMERS):
        c = threading.Thread(target=consumer, args=(que, empty_slots, full_slots, FILENAME))
        c.start()
        consumers.append(c)

    # wait for all to finish
    for t in producers + consumers:
        t.join()

    # Show the number of primes found

    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            primes = len(f.readlines())
    else:
        primes = 0
    print(f"Found {primes} primes.")


if __name__ == '__main__':
    main()
