import multiprocessing as mp
import os
import time

def worker_function(name):
    """A simple function to be executed in a separate process."""
    print(f"Worker process (PID: {os.getpid()}) starting, name: {name}")
    time.sleep(2)
    print(f"Worker process (PID: {os.getpid()}) finishing, name: {name}")

if __name__ == '__main__':
    print(f"Main process (PID: {os.getpid()}) starting")

    # Create a Process object
    process1 = mp.Process(target=worker_function, args=("Process 1",))
    process2 = mp.Process(target=worker_function, args=("Process 2",))

    # Start the process
    process1.start()
    process2.start()

    # Optionally, wait for the process to finish
    process1.join()
    process2.join()

    print("Main process finishing")
