"""
Course: CSE 351 
Lesson: L02 team activity
File:   prove.py
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

# global
call_count = 0

class GetUrl(threading.Thread):

    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.name = ''

    def get_name(self):
        return self.name

    def run(self):
        item = get_data_from_server(self.url)
        self.name = item['name']


def get_urls(film6, kind):
    global call_count

    threads = []
    for url in film6[kind]:
        t = GetUrl(url)
        call_count += 1
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

    print(kind)
    for t in threads:
        print(f'  - {t.get_name()}')


def main():
    global call_count

    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    film6 = get_data_from_server(f'{TOP_API_URL}/films/6')
    call_count += 1
    print_dict(film6)

    # Retrieve people
    get_urls(film6, 'characters')
    get_urls(film6, 'planets')
    get_urls(film6, 'starships')
    get_urls(film6, 'vehicles')
    get_urls(film6, 'species')

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')

if __name__ == "__main__":
    main()
