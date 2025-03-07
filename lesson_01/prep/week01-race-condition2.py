"""
Race Condition Example
Note: Run with Python 3.9.x
"""

import threading

TIMES = 1000000

counter = 0
lock = threading.Lock()  # Create a lock object

def increment_counter():
    global counter
    for _ in range(TIMES):
        # Acquire the lock before entering the critical section
        lock.acquire()
        try:
            # Critical Section (now protected by the lock)
            value = counter
            value += 1
            counter = value
        finally:
            # Release the lock after leaving the critical section
            lock.release()

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter:,}, expected: {2 * TIMES:,}")