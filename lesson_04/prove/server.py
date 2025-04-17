"""
Course: CSE 351
Lesson Week: 4
File: server.py
Author: Brother Comeau
Purpose: Assignment 4 - Weather Program

Instructions:

Open a terminal window and run this program

*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************

req = Request_thread(f'{TOP_API_URL}/end')
req.start()
req.join()

API

/start
/end
/city/{city}
/record/{city}/{recno}`

"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import datetime
import json
import time
import random
import threading
import ast

# Consts
hostName = "127.0.0.1"
serverPort = 8123

SLEEP = 0.1
MAX_GENERATIONS = 6

DATA_FOLDER = 'data/'

# Global Variables
max_thread_count = 0
call_count = 0
thread_count = 0
lock = threading.Lock()

CITIES = (
    # City name, city filename
    ('sandiego' , 'san_diego.dat'),
    ('philadelphia' , 'philadelphia.dat'),
    ('san_antonio' , 'san_antonio.dat'),
    ('san_jose' , 'san_jose.dat'),
    ('new_york' , 'new_york.dat'),
    ('houston', 'houston.dat'),
    ('dallas' , 'dallas.dat'),
    ('chicago' , 'chicago.dat'),
    ('los_angeles' , 'los_angeles.dat'),
    ('phoenix' , 'phoenix.dat'),
)

# key = 'city name', value [[date, temp], ...]
cities_data = {}

start_time = time.time()
end_time = time.time()

# ----------------------------------------------------------------------------
class Log:

    def __init__(self, filename):
        super().__init__()
        self.lock = threading.Lock()
        self.filename = filename
        self.file = open(filename, 'w')

    def write(self, line):
        with self.lock:
            self.file.write(line)
            self.file.write('\n')
            self.file.flush()

    def __del__(self):
        self.file.close()

# Global log object
log = Log('server.log')

# ----------------------------------------------------------------------------
class Handler(BaseHTTPRequestHandler):

    def get_city_details(self, name):
        # global people
        # if id in people:
        #     return people[id].get_dict()
        # else:
        #     return None
        pass


    def get_city_record(self, name, recno):
        # global families
        # if id in families:
        #     return families[id].get_dict()
        # else:
        #     return None
        pass

   
    def do_GET(self):
        global thread_count
        global lock
        global max_thread_count
        global call_count
        global log

        with lock:
            thread_count += 1
            call_count += 1
            if thread_count > max_thread_count:
                max_thread_count = thread_count
            print(f'Current: active threads / max count: {thread_count} / {max_thread_count}')
            log.write(f'Current: active threads / max count: {thread_count} / {max_thread_count}')

        print('- ' * 35)
        print(s := f'Request: {self.path}')
        log.write(s)

        # START ---------------------------------------------------
        if 'start' in self.path:
            global start_time
            global cities_data

            # Load DAT files
            cities_data = {}
            for name, filename in CITIES:
                print(s := f'Loading city data {name}')
                log.write(s)
                with open(DATA_FOLDER + filename, 'r') as f:
                    cities_data[name] = json.load(f)

            max_thread_count = 1
            thread_count = 1
            call_count = 1

            start_time = time.time()

            json_data = '{"status":"OK"}'


        # END ---------------------------------------------------
        elif 'end' in self.path:
            global end_time

            end_time = time.time()

            print('#' * 80)
            log.write('#' * 80)

            print(s := f'Total number of API calls     : {call_count}')
            log.write(s)

            print(s := f'Final thread count (max count): {max_thread_count}')
            log.write(s)

            print(s := f'Total time (seconds)          : {end_time - start_time}')
            log.write(s)

            print(s := f'Calls per second              : {call_count / (end_time - start_time)}')
            log.write(s)

            data_str = '{' + \
                       f'"status":"OK", "api": {call_count}, "threads": {max_thread_count}, "total_time": {end_time - start_time}, "calls_per_second": {call_count / (end_time - start_time)}' + \
                       '}'
            json_data = json.dumps(ast.literal_eval(data_str))

            print('#' * 80)
            log.write('#' * 80)

        # CITY DETAILS  ---------------------------------------------------
        elif 'city' in self.path:
            parts = self.path.split('/')
            # print('****************************')
            # print(parts)

            if len(parts) != 3:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            try:
                name = parts[-1].lower()
            except:
                name = None

            if name == None:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            if name not in cities_data:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            data_str = '{' + \
                       f'"status":"OK", "city": "{name}", "records": {len(cities_data[name])}' + \
                       '}'
            json_data = json.dumps(ast.literal_eval(data_str))

        # CITY RECORD  ---------------------------------------------------
        elif 'record' in self.path:

            if SLEEP > 0:
                time.sleep(SLEEP)

            parts = self.path.split('/')
            # print('****************************')
            # print(parts)

            if len(parts) != 4:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            try:
                name = parts[-2].lower()
                record = int(parts[-1])
            except:
                name = None
                record = None

            if name == None or record == None:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            if name not in cities_data:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            date_str = cities_data[name][record][0]         # Format "mmdd hhmmss"
            temp = cities_data[name][record][1]

            # Expand date string to "mm-dd hh:mm:ss"
            #         01234567890
            # format "mmdd hhmmss"
            date_str = date_str[:2] + '-' + date_str[2:4] + ' ' + date_str[5:7] + ':' + date_str[7:9] + ':' + date_str[9:]

            data_str = '{' + \
                       f'"status":"OK", "city": "{name}", "date": "{date_str}", "temp": {temp}' + \
                       '}'
            json_data = json.dumps(ast.literal_eval(data_str))

        else:
            json_data = None


        if json_data == None:
            self.send_response(404)
            self.send_header("Content-type",  "application/json")
            self.end_headers()
        else:
            print('Sending:', json_data)
            log.write(f'Sending: {json_data}')

            self.send_response(200)
            self.send_header("Content-type",  "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_data, "utf8"))

        with lock:
            thread_count -= 1


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    server = ThreadingSimpleServer((hostName, serverPort), Handler)
    print(f'Starting server.  Waiting on {hostName}:{serverPort}, use <Ctrl-C> or <Command-C> to stop')
    server.serve_forever()

