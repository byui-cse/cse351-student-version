"""
Race Condition Example
Note: Run with Python 3.9.x
"""

import threading
import time

TIMES = 1000000

counter = 0  # Shared resource

def increment_counter():
    global counter
    for _ in range(TIMES):
        # Critical Section (but not protected!)
        value = counter  # Read
        value += 1       # Modify
        counter = value  # Write

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
