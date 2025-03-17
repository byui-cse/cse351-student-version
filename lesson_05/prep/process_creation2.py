import multiprocessing as mp
import os
import time

PROCESSES = 5

def worker_function(name):
    """A simple function to be executed in a separate process."""
    print(f"Worker process (PID: {os.getpid()}) starting, name: {name}")
    time.sleep(2)
    print(f"Worker process (PID: {os.getpid()}) finishing, name: {name}")

if __name__ == '__main__':
    print(f"Main process (PID: {os.getpid()}) starting")

    processes = []
    for i in range(PROCESSES):
        process = mp.Process(target=worker_function, args=(f"Process {i + 1}",))
        processes.append(process)

    # Start the processes
    for p in processes:
        p.start()

    # wait for them to finish
    for p in processes:
        p.join()

    print("Main process finishing")
