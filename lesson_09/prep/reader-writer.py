import threading
import time
import random

shared_resource = "Initial Value"
reader_count = 0

def reader(reader_id, rc_lock, resource_lock):
    global shared_resource, reader_count
    thread_name = threading.current_thread().name

    while True:
        print(f"{thread_name} (Reader {reader_id}): Attempting to read...")

        with rc_lock:
            reader_count += 1
            if reader_count == 1:
                print(f"{thread_name} (Reader {reader_id}): First reader! Acquiring resource lock to block writers...")
                resource_lock.acquire()
                print(f"{thread_name} (Reader {reader_id}): Resource lock acquired by readers.")

        print(f"{thread_name} (Reader {reader_id}): *** READING -> '{shared_resource}' (Active Readers: {reader_count}) ***")
        time.sleep(random.uniform(0.3, 0.8))

        with rc_lock:
            reader_count -= 1
            print(f"{thread_name} (Reader {reader_id}): Finished reading. (Active Readers: {reader_count})")
            if reader_count == 0:
                 print(f"{thread_name} (Reader {reader_id}): Last reader! Releasing resource lock for writers.")
                 resource_lock.release()

        time.sleep(random.uniform(1, 3))


def writer(writer_id, resource_lock):
    global shared_resource
    thread_name = threading.current_thread().name

    while True:
        print(f"{thread_name} (Writer {writer_id}): Attempting to write...")

        print(f"{thread_name} (Writer {writer_id}): Acquiring resource lock...")
        with resource_lock:
            print(f"{thread_name} (Writer {writer_id}): ---> Lock acquired. *** WRITING ***")

            new_value = f"Value set by Writer {writer_id} at {time.time():.1f}"
            shared_resource = new_value
            print(f"{thread_name} (Writer {writer_id}): ---> Resource updated to '{new_value}'")
            time.sleep(random.uniform(0.8, 1.5))

            print(f"{thread_name} (Writer {writer_id}): ---> Finished writing. Releasing lock.")

        time.sleep(random.uniform(2, 5))


if __name__ == "__main__":
    NUM_READERS = 4
    NUM_WRITERS = 2

    threads = []
    stop_event = threading.Event()

    rc_lock = threading.Lock()
    resource_lock = threading.Lock()

    print("--- Starting Reader-Writer Simulation (Reader Priority) ---")

    for i in range(NUM_WRITERS):
        t = threading.Thread(target=writer, args=(i+1, resource_lock), name=f"Writer-{i+1}", daemon=True)
        threads.append(t)
        t.start()

    for i in range(NUM_READERS):
        t = threading.Thread(target=reader, args=(i+1, rc_lock, resource_lock), name=f"Reader-{i+1}", daemon=True)
        threads.append(t)
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n--- Simulation Interrupted ---")
        stop_event.set()

    print("\n--- Simulation End (Main thread exiting) ---")
