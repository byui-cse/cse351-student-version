"""
Course: CSE 251
Lesson Week: 09 lesson 2
File: philosphers2.py
Author: Brother Comeau
Purpose: Dining Philosophers using a waiter
Based on: https://www.programmersought.com/article/22367487068/
"""

import time
import random
import threading

PHILOSOPHERS = 5
TIMES_TO_EAT = PHILOSOPHERS * 5
DELAY = 1

# race condition - need a lock for both of these global variables
meals = 0
meal_counts = [0] * PHILOSOPHERS

# ----------------------------------------------------------------------------------------------
class Waiter:
    def __init__(self):
        self.lock = threading.Lock()   # thread safe
        self.forks = [False] * PHILOSOPHERS

    def can_eat(self, id):
        with self.lock:
            left = self.forks[id]
            right = self.forks[(id + 1) % PHILOSOPHERS]
            if left == False and right == False:
                self.forks[id] = True
                self.forks[(id + 1) % PHILOSOPHERS] = True
                return True
            else:
                return False
         
    def finished_eating(self, id):
        with self.lock:
            self.forks[id] = False
            self.forks[(id + 1) % PHILOSOPHERS] = False

# ----------------------------------------------------------------------------------------------
class Philosopher(threading.Thread):
    
    def __init__(self, id, waiter, philo_lock):
        threading.Thread.__init__(self)
        self.id = id
        self.waiter = waiter
        self.meal_lock = philo_lock
 
    def run(self):
        global meals
        global meal_counts
        done = False
        while not done:
            with self.meal_lock:
                if meals > TIMES_TO_EAT:
                    done = True
                    continue
            if self.waiter.can_eat(self.id):
                self.dining()
                with self.meal_lock:
                    meals += 1
                    meal_counts[self.id] += 1
                self.waiter.finished_eating(self.id)
                self.thinking()
            else:
                # wait a little before trying again
                time.sleep(random.uniform(0.05, 0.2))


    def dining(self):
        print ("Philosopher", self.id, " starts to eat.")
        time.sleep(random.uniform(1, 3) / DELAY)
        print ("Philosopher", self.id, " finishes eating and leaves to think.")

    def thinking(self):
        time.sleep(random.uniform(1 , 3) / DELAY)


# ----------------------------------------------------------------------------------------------
def main():
    global meal_counts

    waiter = Waiter()
    meal_lock = threading.Lock()

    philosophers = [Philosopher(i, waiter, meal_lock) for i in range(PHILOSOPHERS)]
 
    for p in philosophers: 
        p.start()

    for p in philosophers: 
        p.join()

    print('All Done')
    print(f'Meals: {meal_counts}, Total = {sum(meal_counts)}')


if __name__ == '__main__':
    main()
