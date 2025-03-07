"""
Simple Threaded Function with multiple arguments
"""

import logging
import threading
import time

def thread_function(name, sleep_time):
    """This is the function the thread will run"""
    print(f'Thread "{name}": starting')
    time.sleep(sleep_time)
    print(f'Thread "{name}": finishing')

if __name__ == '__main__':
    print('Main : before creating thread')

    # Create a thread. This doesn't start it, just it's creation
    # The args argument allow the main code to pass arguments to the thread.
    t = threading.Thread(target=thread_function, args=('Sleep Function', 2))

    print('Main : before running thread')
    # Start the thread and then keep executing. 
    # It will not wait for the thread to finish.
    t.start()

    print('Main : wait for the thread to finish')
    # Joining a thead back to the main thread.
    # The main thread will wait for this until the thread is finished
    t.join()

    print('Main : all done')

