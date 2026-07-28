"""
Course: CSE 351 
Lesson: L03 team activity
File:   team.py
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
- Create a threaded function to make a call to the server where
  it retrieves data based on a URL.  The function should have a method
  called get_name() that returns the name of the character, planet, etc...
- The threaded function should only retrieve one URL.
- Create a queue that will be used between the main thread and the threaded functions

- Speed up this program as fast as you can by:
    - creating as many as you can
    - start them all
    - join them all

"""
import random
import time
from datetime import datetime, timedelta
import threading
from common import *
from queue import Queue

# Include cse 351 common Python files
from cse351 import *

# global
NUM_THREADS = 8
call_count = 0

def process_url(q: Queue, barrier: threading.Barrier):
    global call_count
    while True:
        url = q.get()
        if url is None:
            break
        call_count += 1
        item = get_data_from_server(url)
        print(f'  - {item["name"]}', flush=True)

    if barrier.wait() == 0:
        print('All threads done!', flush=True)
    time.sleep(random.uniform(0, 1))
    if barrier.wait() == 0:
        print('All threads REALLY done!', flush=True)



def get_urls(film6, kind, q: Queue):
    global call_count

    urls = film6[kind]
    print(kind)
    for url in urls:
        q.put(url)
        # call_count += 1
        # item = get_data_from_server(url)
        # print(f'  - {item["name"]}')

def main():
    global call_count

    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    film6 = get_data_from_server(f'{TOP_API_URL}/films/6')
    call_count += 1
    print_dict(film6)
    q = Queue()
    # barrier = threading.Barrier(NUM_THREADS, action=lambda: print(f'All threads done! ({call_count})', flush=True))
    barrier = threading.Barrier(NUM_THREADS)

    threads = [threading.Thread(target=process_url, args=(q,barrier,)) for _ in range(NUM_THREADS)]
    for t in threads:
        t.start()

    # Retrieve people
    get_urls(film6, 'characters', q)
    get_urls(film6, 'planets', q)
    get_urls(film6, 'starships', q)
    get_urls(film6, 'vehicles', q)
    get_urls(film6, 'species', q)

    # add the sentinels
    for _ in threads:
        q.put(None)

    for t in threads:
        t.join()

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')

if __name__ == "__main__":
    main()
