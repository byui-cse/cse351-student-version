import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        print("Task 1 acquired lock1")
        time.sleep(0.1)  # Simulate some work
        with lock2:
            print("Task 1 acquired lock2")

def task2():
    with lock2:
        print("Task 2 acquired lock2")
        time.sleep(0.1)
        with lock1:
            print("Task 2 acquired lock1")

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Finished (but will likely deadlock before this)")