"""
Course: CSE 351, week 10
File: functions.py
Author: Andrew Meyers

Instructions:

Depth First Search
https://www.youtube.com/watch?v=9RHO6jU--GU

Breadth First Search
https://www.youtube.com/watch?v=86g8jAQug04


Requesting a family from the server:
family_id = 6128784944
data = get_data_from_server('{TOP_API_URL}/family/{family_id}')

Example JSON returned from the server
{
    'id': 6128784944, 
    'husband_id': 2367673859,        # use with the Person API
    'wife_id': 2373686152,           # use with the Person API
    'children': [2380738417, 2185423094, 2192483455]    # use with the Person API
}

Requesting an individual from the server:
person_id = 2373686152
data = get_data_from_server('{TOP_API_URL}/person/{person_id}')

Example JSON returned from the server
{
    'id': 2373686152, 
    'name': 'Stella', 
    'birth': '9-3-1846', 
    'parent_id': 5428641880,   # use with the Family API
    'family_id': 6128784944    # use with the Family API
}


--------------------------------------------------------------------------------------
You will lose 10% if you don't detail your part 1 and part 2 code below

Describe how to speed up part 1

<Add your comments here>


Describe how to speed up part 2

<Add your comments here>


Extra (Optional) 10% Bonus to speed up part 3

<Add your comments here>

"""
from common import *
import threading
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import queue

# -----------------------------------------------------------------------------
def depth_fs_pedigree(family_id, tree):
    # KEEP this function even if you don't implement it
    # TODO - implement Depth first retrieval
    # TODO - Printing out people and families that are retrieved from the server will help debugging
    # data = get_data_from_server('{TOP_API_URL}/family/{family_id}')
    # print("data", data)
    # print("get", tree.get_person_count())
    # ANCHOR
    # if tree.does_family_exist(family_id):
    #     return  # already visited

    # # Fetch and add the family
    # family_data = get_data_from_server(f'{TOP_API_URL}/family/{family_id}')
    # if not family_data:
    #     return
    # family = Family(family_data)
    # # print(f"Retrieved family: {family_data}")
    # tree.add_family(family)

    # # Fetch and add each person
    # for person_id in [family.get_husband(), family.get_wife()] + family.get_children():
    #     if person_id and not tree.does_person_exist(person_id):
    #         person_data = get_data_from_server(f'{TOP_API_URL}/person/{person_id}')
    #         if not person_data:
    #             continue
    #         person = Person(person_data)
    #         # print(f"Retrieved person: {person_data}")
    #         tree.add_person(person)

    #         # Recursively explore the person's parents
    #         parent_family_id = person.get_parentid()
    #         if parent_family_id:
    #             depth_fs_pedigree(parent_family_id, tree)
    
    visited_families = set()
    visited_people = set()
    lock = threading.Lock()

    threads = []

    def dfs(fam_id):
        with lock:
            if fam_id in visited_families:
                return
            visited_families.add(fam_id)

        # Fetch the family data
        family_data = get_data_from_server(f'{TOP_API_URL}/family/{fam_id}')
        if not family_data:
            return

        family = Family(family_data)
        with lock:
            tree.add_family(family)

        parent_fam_ids = []

        # Process husband, wife, and children
        for person_id in [family.get_husband(), family.get_wife()] + family.get_children():
            if not person_id:
                continue

            with lock:
                if person_id in visited_people:
                    continue
                visited_people.add(person_id)

            person_data = get_data_from_server(f'{TOP_API_URL}/person/{person_id}')
            if not person_data:
                continue

            person = Person(person_data)
            with lock:
                tree.add_person(person)

            parent_id = person.get_parentid()
            if parent_id:
                parent_fam_ids.append(parent_id)

        # Spawn threads for parent families
        for pid in parent_fam_ids:
            t = threading.Thread(target=dfs, args=(pid,))
            threads.append(t)
            t.start()

    # Start the recursion from the root family
    root_thread = threading.Thread(target=dfs, args=(family_id,))
    root_thread.start()
    threads.append(root_thread)

    # Wait for all threads to finish
    for t in threads:
        t.join()
# -----------------------------------------------------------------------------
def breadth_fs_pedigree(family_id, tree):
    # KEEP this function even if you don't implement it
    # TODO - implement breadth first retrieval
    # TODO - Printing out people and families that are retrieved from the server will help debugging

    visited_families = set()
    visited_people = set()
    lock = threading.Lock()
    family_queue = queue.Queue()

    family_queue.put(family_id)

    def fetch_and_add_person(pid):
        with lock:
            if pid in visited_people:
                return
            visited_people.add(pid)
        data = get_data_from_server(f'{TOP_API_URL}/person/{pid}')
        if data:
            person = Person(data)
            with lock:
                tree.add_person(person)
            # print(f"Retrieved person: {person.get_id()} - {person.get_name()}")

    def worker():
        while True:
            fam_id = family_queue.get()
            if fam_id is None:
                # Sentinel received, exit thread
                family_queue.task_done()
                break

            with lock:
                if fam_id in visited_families:
                    family_queue.task_done()
                    continue
                visited_families.add(fam_id)

            family_data = get_data_from_server(f'{TOP_API_URL}/family/{fam_id}')
            if not family_data:
                family_queue.task_done()
                continue

            family = Family(family_data)
            with lock:
                tree.add_family(family)
            # print(f"Retrieved family: {family.get_id()}")

            # Gather all person IDs in this family (husband, wife, children)
            person_ids = [family.get_husband(), family.get_wife()] + family.get_children()
            person_ids = [pid for pid in person_ids if pid]

            
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(fetch_and_add_person, person_ids)

            # Queue parent families for next level BFS
            with lock:
                for pid in person_ids:
                    person = tree.get_person(pid)
                    if person:
                        parent_fam_id = person.get_parentid()
                        if parent_fam_id and parent_fam_id not in visited_families:
                            family_queue.put(parent_fam_id)

            family_queue.task_done()

    # Start worker threads
    threads = []
    num_threads = 20
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # Wait for all tasks to be done
    family_queue.join()

    # Send sentinel values to stop all workers
    for _ in range(num_threads):
        family_queue.put(None)

    # Wait for threads to exit
    for t in threads:
        t.join()


# -----------------------------------------------------------------------------
def breadth_fs_pedigree_limit5(family_id, tree):
    # KEEP this function even if you don't implement it
    # TODO - implement breadth first retrieval
    #      - Limit number of concurrent connections to the FS server to 5
    # TODO - Printing out people and families that are retrieved from the server will help debugging

    pass