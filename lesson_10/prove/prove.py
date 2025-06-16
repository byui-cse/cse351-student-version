"""
Course: CSE 351
Lesson Week: 10
File: assignment.py
Author: <your name>
Purpose: Assignment 10 - Family Search
"""
import time
import threading
import json
import requests
from common import *
from functions import depth_fs_pedigree, breadth_fs_pedigree, breadth_fs_pedigree_limit5

from cse351 import *

DFS = 'Depth First Search'
BFS = 'Breadth First Search'
BFS5 = 'Breadth First Search limit 5'

def run_part(log, start_id, generations, title, func):
    tree = Tree(start_id)

    get_data_from_server(f'{TOP_API_URL}/start/{generations}')

    log.write('\n')
    log.write('#' * 45)
    log.start_timer(f'{title}: {generations} generations')
    log.write('#' * 45)
    func(start_id, tree)
    total_time = log.stop_timer()

    server_data = get_data_from_server(f'{TOP_API_URL}/end')

    print_dict(server_data)
    
    tree.display(log)
    log.write('')
    log.write(f'total_time                    : {total_time:.5f}')
    log.write(f'Generations                   : {generations}')
    log.write(f'People % Families / second    : {(tree.get_person_count()  + tree.get_family_count()) / total_time:.5f}')
    log.write('')

    log.write(f'STATS        Retrieved | Server details')
    log.write(f'People  :   {tree.get_person_count():>10,} | {server_data["people"]:>14,}')
    log.write(f'Families:   {tree.get_family_count():>10,} | {server_data["families"]:>14,}')
    log.write(f'API Calls            : {server_data["api"]}')
    log.write(f'Max number of threads: {server_data["threads"]}')


def main():
    log = Log(show_terminal=True, filename_log='assignment.log')

    # starting family
    data = get_data_from_server(f'{TOP_API_URL}')
    start_id = data['start_family_id']
    print(f'Starting Family id: {start_id}')

    # load runs.txt
    # part number, number of generations
    with open('runs.txt') as runs:
        for line in runs:
            parts = line.split(',')
            part_to_run = int(parts[0])
            generations = int(parts[1])

            if part_to_run == 1:
                run_part(log, start_id, generations, DFS, depth_fs_pedigree)
            elif part_to_run == 2:
                run_part(log, start_id, generations, BFS, breadth_fs_pedigree)
            elif part_to_run == 3:
                run_part(log, start_id, generations, BFS5, breadth_fs_pedigree_limit5)


if __name__ == '__main__':
    main()

