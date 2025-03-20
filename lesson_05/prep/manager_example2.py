import multiprocessing as mp

def worker_value(shared_value, process_id):
    """Worker process to increment a shared Value."""
    for _ in range(5):
        shared_value.value += 1
        print(f"Process {process_id}: Value incremented to {shared_value.value}")

def worker_array(shared_array, process_id):
    """Worker process to modify a shared Array."""
    for i in range(len(shared_array)):
        shared_array[i] += process_id + 1
        print(f"Process {process_id}: Array[{i}] updated to {shared_array[i]}")

if __name__ == '__main__':
    # Create a shared Value object
    shared_int = mp.Manager().Value('i', 0)  # 'i' for signed integer, initial value 0
    print(f"Initial shared_int: {shared_int.value}")

    # Create a shared Array object
    shared_array_data = [1.0, 2.5, 3.0]
    shared_float_array = mp.Manager().Array('d', shared_array_data)  # 'd' for double float
    print(f"Initial shared_float_array: {list(shared_float_array)}")

    # Create and start worker processes for the Value
    num_value_processes = 3
    value_processes = []
    for i in range(num_value_processes):
        p = mp.Process(target=worker_value, args=(shared_int, i))
        value_processes.append(p)
        p.start()

    # Create and start worker processes for the Array
    num_array_processes = 2
    array_processes = []
    for i in range(num_array_processes):
        p = mp.Process(target=worker_array, args=(shared_float_array, i))
        array_processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in value_processes:
        p.join()
    for p in array_processes:
        p.join()

    # Print the final shared Value and Array
    print(f"\nFinal shared_int: {shared_int.value}")
    print(f"Final shared_float_array: {list(shared_float_array)}")
