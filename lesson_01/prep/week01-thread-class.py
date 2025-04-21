"""
Create a class that extends the threading.Thread class.
"""

import threading

class MyThread(threading.Thread):
    def __init__(self, name, value):
        threading.Thread.__init__(self)
        self.name = name                    # remember the variable 
        self.value = value                  # remember the variable 
        self.results = None                 # The value to "return" from the thread

    def run(self):
        # Code to be executed in the thread
        print(f"Thread {self.name} with value = {self.value} is running")
        self.results = 'This is the answer'


my_thread = MyThread("Thread-1", 1234)    # Creates the thread
my_thread.start()                         # This calls run() in the class
my_thread.join()                          # wait it (ie., the run() function) to finish

answer = my_thread.results
print(f'The answer from the thread is: {answer}')

print("Main all done")
