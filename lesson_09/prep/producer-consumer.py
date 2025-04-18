import threading
import queue
import time
import random

def producer(q, num_items):
    producer_id = threading.current_thread().name
    print(f"{producer_id}: Starting to produce {num_items} items...")
    for i in range(num_items):
        item = f"Data Packet {i+1}"
        time.sleep(random.uniform(0.1, 0.5))
        q.put(item)
        print(f"{producer_id}: Produced '{item}'. Queue size approx: {q.qsize()}")
    q.put(None)
    print(f"{producer_id}: Finished producing. Sent stop signal.")

def consumer(q):
    consumer_id = threading.current_thread().name
    print(f"{consumer_id}: Starting to consume...")
    while True:
        item = q.get()
        if item is None:
            print(f"{consumer_id}: Received stop signal. Exiting.")
            break
        print(f"{consumer_id}: Consuming '{item}'...")
        time.sleep(random.uniform(0.2, 1.0))
        print(f"{consumer_id}: Finished consuming '{item}'.")
    print(f"{consumer_id}: Exiting.")

if __name__ == "__main__":
    NUMBER_OF_ITEMS = 5

    shared_queue = queue.Queue()

    print("Main: Setting up Producer and Consumer threads.")
    producer_thread = threading.Thread(target=producer, args=(shared_queue, NUMBER_OF_ITEMS), name="Producer")
    consumer_thread = threading.Thread(target=consumer, args=(shared_queue,), name="Consumer")

    print("Main: Starting threads...")
    producer_thread.start()
    consumer_thread.start()

    print("Main: Waiting for threads to finish...")
    producer_thread.join()

    print("Main: Producer thread has finished.")
    consumer_thread.join()

    print("Main: Program complete.")
