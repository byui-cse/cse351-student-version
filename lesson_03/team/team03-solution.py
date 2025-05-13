"""
Course: CSE 351 
Lesson: L03 team activity
File:   W03team-solution.py
Author: <Add name here>

Purpose: Retrieve Star Wars details from a server

Instructions:

- This program requires that the server.py program be started in a terminal window.
- The program will retrieve the names of:
    - characters
    - planets
    - starships
    - vehicles
    - species

- the server will delay the request by 0.5 seconds

TODO
- Create a threaded class to make a call to the server where
  it retrieves data based on a URL.  The class should have a method
  called get_name() that returns the name of the character, planet, etc...
- The threaded class should only retrieve one URL.

- Speed up this program as fast as you can by:
    - creating as many as you can
    - start them all
    - join them all

"""

from datetime import datetime, timedelta
import threading
import queue

from common import *

# Include cse 351 common Python files
from cse351 import *

# global
THREADS = 10
call_count = 0

def worker(que):
    global call_count

    while True:
        call_count += 1
        url = que.get()
        if url is None:
            break

        data = get_data_from_server(url)
        print(f'  - {data['name']}')


def main():
    global call_count

    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    film6 = get_data_from_server(f'{TOP_API_URL}/films/6')
    call_count += 1
    print_dict(film6)

    # Create shared queue
    que = queue.Queue()

    # Create threads
    threads = []
    for i in range(THREADS):
        t = threading.Thread(target=worker, args=(que,))
        threads.append(t)

    # Start threads
    for t in threads:
        t.start()

    # fill queue with urls

    for url in film6['characters']:
        que.put(url)
    
    for url in film6['planets']:
        que.put(url)
    
    for url in film6['starships']:
        que.put(url)
    
    for url in film6['vehicles']:
        que.put(url)
    
    for url in film6['species']:
        que.put(url)

    # MUST add a "all done" message for each worker
    for i in range(THREADS):
        que.put(None)
    
    # Join threads - wait for the workers to finish
    for t in threads:
        t.join()

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')

if __name__ == "__main__":
    main()
