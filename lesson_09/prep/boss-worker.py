import random
import threading
import queue
import time

def simple_worker(task_queue, worker_id):
    thread_name = threading.current_thread().name
    print(f"{thread_name} (Worker {worker_id}): Ready.")
    while True:
        task_description = task_queue.get()

        if task_description is None:
            print(f"{thread_name} (Worker {worker_id}): Stop signal received, exiting.")
            break

        print(f"{thread_name} (Worker {worker_id}): Processing '{task_description}'...")
        time.sleep(random.uniform(0.5, 1.0)) # Simulate work
        print(f"{thread_name} (Worker {worker_id}): Finished '{task_description}'.")

        task_queue.task_done()

if __name__ == "__main__":
    NUM_WORKERS = 2
    NUM_TASKS = 5

    task_queue = queue.Queue()

    print(f"BOSS: Starting {NUM_WORKERS} workers...")
    worker_threads = []
    for i in range(NUM_WORKERS):
        worker_id = i + 1
        thread = threading.Thread(target=simple_worker, args=(task_queue, worker_id), name=f"Worker-{worker_id}")
        thread.start()
        worker_threads.append(thread)

    print(f"BOSS: Adding {NUM_TASKS} tasks to the queue...")
    for i in range(NUM_TASKS):
        task_queue.put(f"Task-{i+1}")

    print("BOSS: Sending stop signals to workers...")
    for _ in range(NUM_WORKERS):
        task_queue.put(None)

    print("BOSS: Waiting for worker threads to exit...")
    for thread in worker_threads:
        thread.join()

    print("BOSS: All workers have finished. Program complete.")
