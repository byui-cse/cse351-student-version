import threading
import queue
import time
import random

BUFFER_SIZE = 3
ITEMS_TO_PRODUCE = 7

def producer_bounded(q):
    producer_id = threading.current_thread().name
    print(f"{producer_id}: Starting...")
    for i in range(ITEMS_TO_PRODUCE):
        item = f"Item-{i+1}"
        print(f"{producer_id}: Trying to put '{item}' (Queue size: {q.qsize()})...")
        q.put(item)
        print(f"{producer_id}: Successfully put '{item}' (Queue size: {q.qsize()}).")
        time.sleep(random.uniform(0.1, 0.3))
    q.put(None)
    print(f"{producer_id}: Finished producing. Stop signal sent.")

def consumer_bounded(q):
    consumer_id = threading.current_thread().name
    print(f"{consumer_id}: Starting...")
    while True:
        print(f"{consumer_id}: Trying to get item (Queue size: {q.qsize()})...")
        item = q.get()
        print(f"{consumer_id}: Successfully got item (Queue size: {q.qsize()})...")
        if item is None:
            print(f"{consumer_id}: Stop signal received. Exiting.")
            q.task_done() # Acknowledge the None sentinel for join() if used
            break
        print(f"{consumer_id}: Consuming '{item}'...")
        time.sleep(random.uniform(0.5, 1.0))
        print(f"{consumer_id}: Finished consuming '{item}'.")
        q.task_done() # Signal item processing complete for join() if used
    print(f"{consumer_id}: Exiting.")


if __name__ == "__main__":
    print(f"Main: Setting up Bounded Buffer (Size: {BUFFER_SIZE})...")

    shared_queue = queue.Queue(maxsize=BUFFER_SIZE)

    producer_thread = threading.Thread(target=producer_bounded, args=(shared_queue,), name="Producer")
    consumer_thread = threading.Thread(target=consumer_bounded, args=(shared_queue,), name="Consumer")

    print("Main: Starting threads...")
    producer_thread.start()
    consumer_thread.start()

    print("Main: Waiting for threads to finish...")
    producer_thread.join()
    consumer_thread.join()

    print("Main: Bounded Buffer program complete.")
