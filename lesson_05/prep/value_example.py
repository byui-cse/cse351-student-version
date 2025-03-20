import multiprocessing as mp

def worker_value(shared_int, shared_float):
    shared_int.value += 1
    shared_float.value *= 2.0

if __name__ == '__main__':
    shared_int = mp.Value('i', 10)  # Shared integer
    shared_float = mp.Value('d', 3.14)  # Shared double

    p = mp.Process(target=worker_value, args=(shared_int, shared_float))
    p.start()
    p.join()

    print(f"Shared integer: {shared_int.value}")
    print(f"Shared float: {shared_float.value}")
