import multiprocessing as mp
from multiprocessing.shared_memory import SharedMemory
import numpy as np

def worker_shmem(name, shape, dtype):
    shm = SharedMemory(name=name)  # Connect to the existing shared memory
    shared_array = np.ndarray(shape, dtype=dtype, buffer=shm.buf)
    shared_array[:] += 1  # Modify the array in place
    print(f"Worker: {shared_array}")
    shm.close()

if __name__ == '__main__':
    # Create a NumPy array
    a = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    shm = SharedMemory(create=True, size=a.nbytes)  # Create shared memory

    # Create a NumPy array that uses the shared memory as its buffer
    shared_array = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
    shared_array[:] = a[:]  # Copy data into the shared memory

    p = mp.Process(target=worker_shmem, args=(shm.name, a.shape, a.dtype))
    p.start()
    p.join()

    print(f"Main process: {shared_array}")  # Access the modified array

    shm.close()
    shm.unlink()  # Release the shared memory (important!)
    