import multiprocessing as mp
import time

def worker(q):
    while True:
        item = q.get()      # Blocks until an item is available
        if item is None:    # value to stop
            break
        print(f"Worker: Processing {item}")
        time.sleep(0.5)
    print("Worker: Exiting")

if __name__ == '__main__':
    q = mp.Queue()

    # Create and start worker processes
    processes = []
    for _ in range(3):
        p = mp.Process(target=worker, args=(q,))
        processes.append(p)
        p.start()

    # Put items into the queue
    for i in range(10):
        q.put(i)

    # Add value to stop the workers - one for each
    for _ in range(3):
        q.put(None)

    for p in processes:
        p.join()

    print("All tasks completed")
