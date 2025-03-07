"""
Create a class that extends the threading.Thread class.
"""

import threading

class MyThread(threading.Thread):
    def run(self):
        # Code to be executed in the thread
        print(f"Thread {self.name} is running")

thread1 = MyThread(name="Thread-1")
thread1.start()
thread1.join()

print("Main all done")

