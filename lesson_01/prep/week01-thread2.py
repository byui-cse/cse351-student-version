"""
Simple Threaded Function with one argument
Note: Tuples that contain only one element must have a trailing comma.
"""

import threading
import time

def thread_function(name):
    """This is the function the thread will run"""
    print(f'Thread "{name}": starting')
    time.sleep(2)
    print(f'Thread "{name}": finishing')

if __name__ == '__main__':
    print('Main  : before creating thread')

    t = threading.Thread(target=thread_function, args=('Bob',))

    print('Main  : before running thread')
    t.start()

    print('Main  : wait for the thread to finish')
    t.join()

    print('Main  : all done')

