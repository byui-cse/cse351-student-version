import threading
import queue
import time
import random

THREAD_COUNT = 3

def producer(thread_index, q, num_items):
    for i in range(num_items):
        item = random.randint(1, 100) * (thread_index + 1) ** 10

        q.put(item)  # Put the item in the queue

        print(f"Producer: Produced {item}")

        time.sleep(random.random() * 0.1)

    # Add a sentinel.  This is how the consumer() function knows
    # that there are no more items coming down the queue.
    # ALL consumers() MUST receive a None so that they can stop
    for i in range(THREAD_COUNT):
        q.put(None) 

def consumer(q):
    while True:
        item = q.get()  # Get an item from the queue (blocks if empty)
        if item is None:
            break
        print(f"Consumer: Consumed {item}")
        time.sleep(random.random() * 0.2)

if __name__ == '__main__':
    q = queue.Queue()
    num_items = 5

    producers = []
    consumers = []

    for i in range(THREAD_COUNT):
        producers.append(threading.Thread(target=producer, args=(i, q, num_items)))
        consumers.append(threading.Thread(target=consumer, args=(q,)))

    for p in producers + consumers:
        p.start()

    for p in producers + consumers:
        p.join()

    print("Producer-consumer example finished.")
