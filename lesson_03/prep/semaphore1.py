import threading
import time
import random

THREADS = 5

def do_work(thread_id):
    print(f"Thread {thread_id}: Acquired resource.")
    time.sleep(random.uniform(0.5, 2))
    print(f"Thread {thread_id}: Releasing resource.")


def access_resource_with(thread_id, semaphore):
    with semaphore:
        do_work(thread_id)


def access_resource_calls(thread_id, semaphore):
    semaphore.acquire()
    do_work(thread_id)
    semaphore.release()


def test(thread_func, message):
    print()-
    print('-' * 40)
    print(message)
    print('-' * 40)

    # Simulate a resource with limited capacity (e.g., 3 database connections)
    semaphore = threading.Semaphore(3)

    threads = []
    for i in range(THREADS):
        thread = threading.Thread(target=thread_func, args=(i, semaphore))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    test(access_resource_with, 'Using with statement')
    test(access_resource_calls, 'Using acquire() and release()')

