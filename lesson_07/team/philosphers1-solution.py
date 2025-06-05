"""
Course: CSE 251
Lesson Week: 09 lesson 2
File: philosphers1.py
Author: Brother Comeau
Purpose: Dining Philosophers
based on: https://rosettacode.org/wiki/Dining_philosophers#Python
"""

import time
import random
import threading

PHILOSOPHERS = 5
TIMES_TO_EAT = PHILOSOPHERS * 5
DELAY = 1

# TODO - run program for 30 seconds instead of number of times eating

# race condition - need a lock for both of these global variables
meal_count = 0
meals = [0] * PHILOSOPHERS

class Philosopher(threading.Thread):
    
    def __init__(self, id, lock_meals, left, right):
        threading.Thread.__init__(self)
        self.id = id
        self.left = left
        self.right = right
        self.lock_meals = lock_meals
 
    def run(self):
        global meal_count
        global meals
        done = False
        while not done:
            with self.lock_meals:
                if meal_count >= TIMES_TO_EAT:
                    done = True
                    continue

            # try to eat
            self.left.acquire()  # blocking
            if not self.right.acquire(blocking=False):
                # we can't grab the right fork, so let left go and try again
                self.left.release()

                # swap the forks
                self.left, self.right = self.right, self.left
                continue

            self.dining()

            with self.lock_meals:
                meal_count += 1
                meals[self.id] += 1

            self.left.release()
            self.right.release()

            self.thinking()

        pass

    def dining(self):
        print ("Philosopher", self.id, " starts to eat.")
        time.sleep(random.uniform(1, 3) / DELAY)
        print ("Philosopher", self.id, " finishes eating and leaves to think.")

    def thinking(self):
        time.sleep(random.uniform(1, 3) / DELAY)



def main():
    global meal_count

    meal_count = 0

    forks = [threading.Lock() for _ in range(PHILOSOPHERS)]

    lock_meals = threading.Lock()

    philosophers = [Philosopher(i, lock_meals, forks[i % PHILOSOPHERS], forks[(i + 1) % PHILOSOPHERS]) for i in range(PHILOSOPHERS)]
 
    for p in philosophers: 
        p.start()

    for p in philosophers: 
        p.join()

    print('All Done:', meal_count, meals)


if __name__ == '__main__':
    main()
