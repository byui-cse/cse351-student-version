import threading
import queue
import time
import random

def producer(q, num_items):
    for i in range(num_items):
        item = random.randint(1, 100)  # Generate a random item

        q.put(item)  # Put the item in the queue

        print(f"Producer: Produced {item}")

        time.sleep(random.random() * 0.1)

    # Add a sentinel.  This is how the consumer() function knows
    # that there are no more items coming down the queue.
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
    num_items = 10

    producer_thread = threading.Thread(target=producer, args=(q, num_items))
    consumer_thread = threading.Thread(target=consumer, args=(q,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()  # Wait for the producer to finish
    consumer_thread.join()  # wait for the consumer to finish

    print("Producer-consumer example finished.")
