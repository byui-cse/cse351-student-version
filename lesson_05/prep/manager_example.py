import multiprocessing as mp

def worker_manager(shared_list, shared_dict):
    shared_list.append(mp.current_process().name)
    shared_dict[mp.current_process().name] = len(shared_list)

if __name__ == '__main__':
    with mp.Manager() as manager:  # Use as a context manager
        shared_list = manager.list()  # Create a shared list
        shared_dict = manager.dict()  # Create a shared dictionary

        processes = []
        for _ in range(3):
            p = mp.Process(target=worker_manager, args=(shared_list, shared_dict))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        print(f"Shared list: {shared_list}")
        print(f"Shared dict: {shared_dict}")
