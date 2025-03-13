import threading
import time
import random

THREADS = 4

def worker(barrier, thread_id):
    print(f"Thread {thread_id}: Performing initialization...")
    time.sleep(random.uniform(0.1, 0.5))

    print(f"Thread {thread_id}: Waiting at the barrier...")
    worker_id = barrier.wait()

    print(f"Thread {thread_id}: Passed the barrier! (worker id: {worker_id})")

    # Perform the next stage of the computation, now synchronized
    time.sleep(random.uniform(0.1, 0.5))

    print(f"Thread {thread_id}: Finishing.")

if __name__ == '__main__':
    barrier = threading.Barrier(THREADS)

    threads = []
    for i in range(THREADS):
        thread = threading.Thread(target=worker, args=(barrier, i))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
