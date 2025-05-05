"""
Course: CSE 351 
Lesson: L02 team activity
File:   team02-solution2.py
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

from common import *

# Include cse 351 common Python files
from cse351 import *

CHAR = 'characters'
PLAN = 'planets'
STAR = 'starships'
VEH = 'vehicles'
SPEC = 'species'

# global
call_count = 0

results = {}            # <type, [names]>

class GetUrl(threading.Thread):

    def __init__(self, kind, url):
        threading.Thread.__init__(self)
        self.kind = kind
        self.url = url
        self.name = ''

    def get_name(self):
        return self.name

    def run(self):
        item = get_data_from_server(self.url)
        self.name = item['name']


def get_urls(urls):
    global call_count
    global results

    threads = []
    for kind, url in urls:
        t = GetUrl(kind, url)
        call_count += 1
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

    for t in threads:
        kind = t.kind
        if kind not in results:
            results[kind] = [t.get_name()]
        else:
            results[kind].append(t.get_name())


def main():
    global call_count

    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    film6 = get_data_from_server(f'{TOP_API_URL}/films/6')
    call_count += 1
    # print_dict(film6)

    all_urls = []           # list of tuples (type, url)

    # Retrieve all
    def _add_urls(t, all_urls, urls):
        for url in urls:
            all_urls.append((t, url))

    _add_urls(CHAR, all_urls, film6['characters'])
    _add_urls(PLAN, all_urls, film6['planets'])
    _add_urls(STAR, all_urls, film6['starships'])
    _add_urls(VEH,  all_urls, film6['vehicles'])
    _add_urls(SPEC, all_urls, film6['species'])

    get_urls(all_urls)

    for kind, names in results.items():
        print(kind)
        for name in names:
            print(f'  - {name}')

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')


if __name__ == "__main__":
    main()
