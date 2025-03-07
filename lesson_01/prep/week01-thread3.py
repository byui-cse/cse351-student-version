"""
Multiple Threads with multiple arguments
"""

import threading
import time

def thread_function(name, sleep_time):
    """This is the function the thread will run"""
    print(f'Thread "{name}": starting')
    time.sleep(sleep_time)
    print(f'Thread "{name}": finishing')

if __name__ == '__main__':
    print('Main  : before creating thread')

    # Create a threads
    t1 = threading.Thread(target=thread_function, args=('Bob', 3))
    t2 = threading.Thread(target=thread_function, args=('Jim', 2))
    t3 = threading.Thread(target=thread_function, args=('Mary', 1))

    print('Main  : before running thread')

    t1.start()
    t2.start()
    t3.start()

    print('Main  : wait for the thread to finish')

    t1.join()
    t2.join()
    t3.join()

    print('Main  : all done')
