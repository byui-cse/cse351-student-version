# Lesson 5: Python Processes

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
5.1 | [Introduction to Processes](#Introduction-to-Processes)
5.2 | [Inter-Process Communication](#Inter-Process-Communication)
5.3 | [Process Communication](#Process-Communication)
5.4 | [Process Pools](#Process-Pools)
5.5 | [When to Use Processes](#When-to-Use-Processes)
5.6 | [Process Synchronization](#Process-Synchronization)

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

## 5.1 Introduction to Processes

Processes are fundamental to modern operating systems and form the basis for true parallelism, especially in Python, where the Global Interpreter Lock (GIL) limits the effectiveness of threads for CPU-bound tasks. This section introduces the concept of processes, contrasts them with threads, and demonstrates basic process management in Python.

### What is a Processes?

A process is an independent instance of a program in execution.  It's a self-contained unit that has the following:

- **Memory Space:** Each process has its own private memory space, completely isolated from other processes. This includes the program's code, data, heap (for dynamically allocated memory), and stack.
- **System Resources:** Processes have their own set of resources allocated by the operating system, such as file handles, network sockets, and device access.
- **Execution Context:** This includes the program counter (which instruction is currently being executed), CPU registers, and other information needed to manage the process's execution.
- **Security Credentials:** Processes have associated user and group IDs, which determine their privileges and access rights.

Because of this isolation, a crash in one process typically does not affect other processes. This makes processes more robust than threads.

### Process vs. Thread in Python

Both processes and threads provide a way to achieve concurrency, but they differ significantly in their structure and behavior. Here's a table summarizing the key differences:

| Feature | Process | Thread |
|---|---|---|
| Memory Space | Independent; each process has its own private memory space. | Shared; all threads within a process share the same memory space. |
| Resource Usage | Higher overhead; creating and managing processes is more resource-intensive. | Lower overhead; creating and managing threads is generally faster and uses fewer resources. |
| Communication | Inter-Process Communication (IPC) mechanisms are required (e.g., pipes, queues, shared memory). IPC is generally more complex. | Direct communication through shared memory. Easier but requires careful synchronization (locks, etc.) to avoid race conditions. |
| Context Switching | Slower; context switching between processes is typically slower because it involves switching entire memory spaces. | Faster; context switching between threads is faster because they share the same memory space. |
| Fault Isolation | Higher; a crash in one process usually does not affect other processes. | Lower; a crash in one thread can bring down the entire process (and all its threads). |
| Parallelism | True parallelism; processes can run concurrently on multiple CPU cores. | Concurrency, but true parallelism is often limited in CPython by the GIL for CPU-bound tasks. |
| Creation | OS system calls (e.g., fork() on Unix-like systems, CreateProcess() on Windows) or higher-level libraries like multiprocessing. | OS system calls or libraries like threading. |

#### In summary

- Processes are isolated and independent, offering robustness and true parallelism, but with higher overhead and more complex communication.
- Threads are lightweight and share resources within a single process, making communication easier, but are more susceptible to shared-memory issues and (in CPython) limited by the GIL for CPU-bound tasks.


### Process Creation and Management (in Python's multiprocessing module)

Python's multiprocessing module provides a high-level interface for creating and managing processes, similar in style to the threading module.

### Process Example 1

The following Python program creates processes that are parallel.  It looks very similar to how threads are created and used (ie., create, start, then join).  For processes, the package `multiprocessing` must be used

```python
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
```

Program Output:

From the output, you can see three different processes.  The main process and two created processes.

```text
Main process (PID: 24719) starting
Worker process (PID: 24722) starting, name: Process 2
Worker process (PID: 24721) starting, name: Process 1
Worker process (PID: 24722) finishing, name: Process 2
Worker process (PID: 24721) finishing, name: Process 1
Main process finishing
```

### Process Example 2


```python
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
```

Program Output:

```text
Main process (PID: 24837) starting
Worker process (PID: 24840) starting, name: Process 2
Worker process (PID: 24841) starting, name: Process 3
Worker process (PID: 24839) starting, name: Process 1
Worker process (PID: 24843) starting, name: Process 5
Worker process (PID: 24842) starting, name: Process 4
Worker process (PID: 24841) finishing, name: Process 3
Worker process (PID: 24839) finishing, name: Process 1
Worker process (PID: 24843) finishing, name: Process 5
Worker process (PID: 24842) finishing, name: Process 4
Worker process (PID: 24840) finishing, name: Process 2
Main process finishing
```

### Process IDs (PIDs)

Every process in an operating system has a unique numerical identifier called a Process ID (PID).  The PID is used by the OS to track and manage processes.

- `os.getpid()`: In Python, you can get the PID of the current process using the `os.getpid()` function (from the os module).
- `os.getppid()`: Get the parent's process ID.


#### PIDs are useful for

- **Monitoring:** You can use PIDs to monitor processes using system tools (e.g., top, ps on Linux/macOS; Task Manager on Windows).
- **Debugging:** PIDs can help you identify which process is associated with which output or error messages.
- **Inter-Process Communication:** Some IPC mechanisms (e.g., signals) use PIDs to target specific processes.
- **Process Management:** You can use PIDs to control processes (e.g., sending signals to them).

The example above demonstrates using `os.getpid()` to print the PID of both the main process and the worker processes.  You'll see that each process has a different PID. This confirms that they are indeed running in separate processes with their own memory spaces.  If the above example was using threads instead of processes, `os.getpid()` would return the same ID in main() and in the threads.


## 5.2 Inter-Process Communication

Inter-Process Communication (IPC) refers to the mechanisms provided by an operating system that allow different processes to exchange data and synchronize their execution. Unlike threads, which share the same memory space within a single process, processes have their own independent memory spaces. This isolation provides robustness (a crash in one process won't necessarily bring down others), but it also necessitates specific mechanisms for communication and coordination.

### Why IPC? (Data Sharing, Coordination between Processes)

IPC is essential for a variety of reasons:

#### Data Sharing

Processes often need to share data.  

- A web server might have multiple worker processes handling client requests, and they might need to share a cache of frequently accessed data.  
- A data processing pipeline might have separate processes for reading data, transforming it, and writing results.  
- A scientific simulation might distribute calculations across multiple processes to leverage multiple CPU cores.


#### Coordination and Synchronization

Processes may need to coordinate their activities.

- A producer process generating data and a consumer process consuming it.
- Multiple processes accessing a shared resource (like a file or database) in a controlled manner.
- A process launching and controlling other processes (e.g., a shell executing commands).
- Signaling between processes. One process might need to notify another process that an event has occurred.

#### Resource Sharing

IPC can be used to share resources that are not directly shareable, such as hardware devices or network connections. A single process might manage access to the resource and communicate with other processes via IPC.

#### Modularity and Fault Isolation

Dividing a large application into multiple processes can improve modularity and fault isolation.  If one process crashes, it's less likely to affect other processes.  This is particularly important for long-running applications or systems that require high reliability.

#### Overcoming the GIL (in Python)

As discussed in the threading section, CPython's Global Interpreter Lock (GIL) limits true parallelism for CPU-bound tasks within a single process.  Using multiple processes bypasses the GIL, allowing you to fully utilize multiple CPU cores for CPU-bound computations. This is the primary reason to use multiprocessing in Python.

### Challenges of IPC (Data Consistency, Synchronization)

While IPC is powerful, it introduces its own set of challenges, many of which are analogous to the challenges of multithreading, but often more complex due to the lack of shared memory.

#### Data Consistency

Since processes don't share memory directly, ensuring data consistency requires careful design.  Data must be serialized (converted to a byte stream) for transmission between processes and then deserialized.  This process can introduce overhead and potential errors.

#### Synchronization

Just like with threads, processes need mechanisms to synchronize their access to shared resources (even if those resources are managed through IPC).  Race conditions can occur if multiple processes try to modify the same data simultaneously without proper coordination.  IPC mechanisms often provide synchronization primitives similar to those used in threading (e.g., locks, semaphores, queues).

#### Overhead

IPC is generally more expensive (in terms of performance) than inter-thread communication.  Data needs to be copied between processes, and the operating system kernel is involved in managing the communication channels. This overhead can be significant, especially for frequent or large data transfers.

#### Complexity

IPC can be more complex to implement than threading.  You need to choose an appropriate IPC mechanism, handle serialization/deserialization, and manage the communication channels.

#### Deadlocks and Livelocks

Similar to threading, improper use of synchronization primitives in IPC can lead to deadlocks (where processes are blocked indefinitely waiting for each other) or livelocks (where processes repeatedly change their state without making progress).

#### Security

When processes communicate across machine boundaries (e.g., over a network), security becomes a critical concern.  IPC mechanisms need to provide secure ways to authenticate processes and encrypt data.

#### Data Marshalling/Serialization

Data passed between processes often needs to be converted into a format suitable for transmission. This process, called marshalling or serialization, can be complex, especially for custom data structures. Common serialization formats include JSON, XML, and Pickle (in Python).  However, Pickle is generally not recommended for untrusted data due to security risks.

In summary, despite these challenges, IPC is a fundamental and essential technique for building robust, scalable, and parallel applications.  Python's multiprocessing module provides a high-level interface for working with processes and various IPC mechanisms, simplifying many of these complexities. The next sections will delve into specific IPC mechanisms available in Python.

## 5.3 Process Communication

Since processes have separate memory spaces, they can't directly share variables like threads do.  Inter-Process Communication (IPC) mechanisms are required for processes to exchange data and synchronize their activities. Python's multiprocessing module (mp) provides several convenient IPC tools.

### mp.Queue

mp.Queue is a process-safe queue, similar in concept to queue.Queue (used for threads), but designed for communication between processes. It handles all the necessary serialization (pickling) and synchronization internally.

#### Purpose

A general-purpose, FIFO (first-in, first-out) queue for passing objects between processes.

#### Key Features

- **Process-safe:** Handles locking and synchronization automatically.
- **Blocking Operations:** `put()` and `get()` block by default, simplifying coordination.
- **Pickling:** Objects sent through the queue are pickled (serialized) and unpickled (deserialized).

#### Methods (same as queue.Queue)

- `put(obj, block=True, timeout=None):` Adds an item to the queue.
- `get(block=True, timeout=None):` Removes and returns an item from the queue.
- `qsize():` Returns the approximate size of the queue.
- `empty():` Returns True if the queue is empty, False otherwise.
- `full():` Returns True if the queue is full (if maxsize was set), False otherwise.
- `close():` Indicates that no more data will be put on the queue by the current process.
- `join_thread():` Must be called after close. Waits until the background thread exits.
- `cancel_join_thread():` Prevents join_thread from blocking.

### Queue Example

```python
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
```

Program Output:

```text
Worker: Processing 0
Worker: Processing 1
Worker: Processing 2
Worker: Processing 3
Worker: Processing 4
Worker: Processing 5
Worker: Processing 6
Worker: Processing 7
Worker: Processing 8
Worker: Processing 9
Worker: Exiting
Worker: Exiting
Worker: Exiting
All tasks completed
```

### mp.Pipe

mp.Pipe provides a simple, unidirectional (or bidirectional) communication channel between two processes. It's typically used for communication between a parent process and a child process.

Purpose is to Direct communication between two processes.

#### Key Features

- Two Connection Objects: Pipe() returns a pair of connection objects representing the two ends of the pipe.
-  Unidirectional or Bidirectional: By default, pipes are bidirectional, but Pipe(duplex=False) creates a unidirectional pipe. Unidirectional pipes are generally safer and easier to reason about.
- Pickling: Objects are pickled for transmission.

#### Pipe Methods

- `send(obj)`: Sends an object to the other end of the pipe.
- `recv()`: Receives an object from the other end of the pipe (blocks until an object is available).
- `close()`: Closes the connection. Crucially important to close unused ends.
- `poll(timeout=None)`: Returns True if data is available to be read, False otherwise. Can be used to avoid blocking indefinitely on recv().

### Pipe Example

```python
import multiprocessing as mp

def child_process(conn):
    while True:
        message = conn.recv()  # Receive data from the parent
        if message is None:
            break
        print(f"Child: Received '{message}' from parent")
    print("Child Exiting")

    # very important to close the connect once finished using it
    conn.close()

def parent_process(conn):
    messages_to_send = ["one", 1, "two", 2, None]
    for message in messages_to_send:
        print(f"Parent: Sending '{message}' to child")
        conn.send(message)
    print("Parent Finished Sending")

    # very important to close the connect once finished using it
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = mp.Pipe()  # Create a bidirectional pipe

    parent = mp.Process(target=parent_process, args=(parent_conn,))
    child = mp.Process(target=child_process, args=(child_conn,))

    child.start()
    parent.start()

    parent.join()
    child.join()

    print("Both Parent and Child Exited")
```

Program Output:

```text
Parent: Sending 'one' to child
Parent: Sending '1' to child
Parent: Sending 'two' to child
Parent: Sending '2' to child
Parent: Sending 'None' to child
Parent Finished Sending
Child: Received 'one' from parent
Child: Received '1' from parent
Child: Received 'two' from parent
Child: Received '2' from parent
Child Exiting
Both Parent and Child Exited
```

### mp.Queue VS mp.Pipe()

Both `mp.Queue()` and `mp.Pipe()` in Python's multiprocessing module provide mechanisms for inter-process communication (IPC), but they have distinct characteristics and are suited for different use cases.

#### 1. Communication Direction:

- `mp.Pipe():` Creates a bidirectional communication channel. Data can flow in both directions through the pipe. You get two connection objects, one for each end of the pipe. Each process involved typically uses one end for sending and/or receiving.   
- `mp.Queue():` Creates a unidirectional communication channel Data flows in a first-in, first-out (FIFO) manner from producers to consumers. Multiple processes can put items onto the queue, and multiple processes can get items from it.


#### 2. Number of Connections:

- `mp.Pipe():` Typically involves two endpoints connected directly. It's primarily designed for communication between two closely related processes (e.g., a parent and a child).   
- `mp.Queue():` Can have multiple producers putting items onto the queue and multiple consumers taking items off. It's better suited for scenarios where you have a pool of workers and a set of tasks to be distributed, or where multiple sources need to send data to multiple destinations in a decoupled way.   


#### 3. Structure and Usage:

- `mp.Pipe():` Returns a tuple of two connection objects. Each process needs to hold onto its end of the connection and use the send() and recv() methods to exchange data. You often close the unused end of the pipe in each process to avoid potential deadlocks or unexpected behavior.   
- `mp.Queue():` Returns a single queue object. Processes use the `put()` method to add items to the queue and the `get()` method to retrieve items.

#### 4. Buffering and Capacity:

- `mp.Pipe():` May have some internal buffering, but it's generally considered less explicitly managed than a queue. The capacity might be limited by the operating system's pipe buffer size. Blocking behavior on `send()` and `recv()` depends on the buffer and the state of the other end.
- `mp.Queue():` Provides more explicit control over buffering. You can create a queue with a specific maxsize to limit the number of items it can hold. `put()` can block if the queue is full (unless block=False is used), and `get()` can block if the queue is empty (unless block=False is used).

#### 5. Complexity of Management:

- `mp.Pipe():` Requires more manual management of the connection objects, especially when dealing with more than two processes. You need to ensure each process has the correct end of the pipe and closes the unnecessary one.
- `mp.Queue():` Offers a higher-level abstraction, simplifying the management of communication between multiple processes. The queue handles the routing and synchronization of messages.   

#### 6. Use Cases:

- `mp.Pipe():` Best suited for direct, two-way communication between two related processes.  A parent process sending commands to a child process and receiving results.  Two worker processes collaborating on a specific task.
- `mp.Queue():` Ideal for distributing work among multiple processes or for scenarios where you have multiple producers and/or consumers.  A pool of worker processes processing tasks from a job queue.  Multiple sensor processes feeding data into a central processing unit.  Implementing producer-consumer patterns.


#### 7. Closing:

- `mp.Pipe():` It's crucial to explicitly close both ends of the pipe in all involved processes when communication is finished to release system resources and avoid potential issues.   
- `mp.Queue():` Don't need to close a queue.


### mp.Manager()

mp.Manager() provides a way to create shared objects that can be safely accessed and modified by multiple processes. It uses a server process to manage the shared objects and provides proxies to access them from other processes.

#### Purpose

Creating shared objects (lists, dictionaries, values, etc.) that can be safely modified by multiple processes without explicit locking.

#### Key Features

- **Proxy Objects:** The manager creates proxy objects that act as intermediaries to the shared objects. Operations on the proxies are automatically synchronized.
- **Variety of Shared Objects:** Supports lists, dictionaries, namespaces, locks, semaphores, barriers, queues, and Value/Array.
- **Server Process:** Uses a separate server process to manage the shared objects, ensuring consistency.

#### Methods

- `Manager()`: Creates a manager object. It's best to use this as a context manager (with a `with` statement).
- `list()`, `dict()`, `Namespace()`, `Lock()`, `RLock()`, `Semaphore()`, `BoundedSemaphore()`, `Condition()`, `Event()`, `Barrier()`, `Queue()`, `Value()`, `Array()`.  These methods are used to create shared objects of various types.

### Manager() Example 1

```python
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
```

Program Output:

```text
Shared list: ['Process-2', 'Process-4', 'Process-3']
Shared dict: {'Process-2': 2, 'Process-4': 2, 'Process-3': 3}
```

### Manager() Example 2

```python
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
```

Program Output:

```text
Initial shared_int: 0
Initial shared_float_array: [1.0, 2.5, 3.0]
Process 0: Value incremented to 1
Process 1: Value incremented to 2
Process 0: Value incremented to 4
Process 1: Value incremented to 4
Process 1: Value incremented to 5
Process 0: Value incremented to 5
Process 1: Value incremented to 6
Process 0: Value incremented to 6
Process 1: Value incremented to 7
Process 0: Value incremented to 7
Process 2: Value incremented to 8
Process 0: Array[0] updated to 2.0
Process 2: Value incremented to 9
Process 2: Value incremented to 10
Process 2: Value incremented to 11
Process 0: Array[1] updated to 3.5
Process 2: Value incremented to 12
Process 0: Array[2] updated to 4.0
Process 1: Array[0] updated to 4.0
Process 1: Array[1] updated to 5.5
Process 1: Array[2] updated to 6.0

Final shared_int: 12
Final shared_float_array: [4.0, 5.5, 6.0]
```

### mp.shared_memory (Python 3.8+)

The multiprocessing.shared_memory module (introduced in Python 3.8) provides a way to create shared memory regions that can be directly accessed by multiple processes. This offers much lower overhead than pickling (used by Queue, Pipe, and Manager), especially for large numerical arrays.

#### Purpose

Efficiently sharing raw bytes of memory between processes. Ideal for NumPy arrays.

#### Key Features

- **Direct Memory Access:** Processes can directly read and write to the shared memory region without pickling/unpickling.
- **SharedMemory Class:** Provides the interface for creating and accessing shared memory blocks.
- **ShareableList:** Similar to a list, but stored in a shared memory region.

#### Methods

- `SharedMemory(name=None, create=False, size=0)`: Creates or connects to a shared memory block.
- `name`: A unique name for the shared memory block (optional if creating).
- `create`: True to create a new block, False to connect to an existing one.
- `size`: The size of the shared memory block in bytes (when creating).
- `ShareableList(sequence=None, *, name=None)`: Creates a mutable list in shared memory.
- `buf`: A memoryview object that provides access to the raw bytes of the shared memory.
- `close()`: Closes access to the shared memory block from the current process.
- `unlink()`: Releases the shared memory block (should only be called once by a single process, usually the creator).

### Shared Memory Example 

```python
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

    print(f"Main process: {shared_array}")

    shm.close()
    shm.unlink()  # Release the shared memory (important!)
```

Program Output:

```text
Worker: [2 3 4 5 6]
Main process: [2 3 4 5 6]
```

### mp.Value and mp.Array

`mp.Value` and `mp.Array` provide simpler (but less flexible) ways to create shared memory objects for single values and arrays of a specific type, respectively. They are older than shared_memory but are still useful in some cases.  They use ctypes under the hood.

#### mp.Value(typecode, initial_value, lock=True)

Creates a shared object to hold a single value of a specified type.

- typecode is a character code indicating the data type (e.g., 'i' for integer, 'd' for double-precision float, 'b' for boolean). See the ctypes documentation for a full list.
- The initial value of the shared object.
- lock, If set to True (default), creates a recursive lock to synchronize access.


#### mp.Array(typecode, size_or_initializer, lock=True)

Creates a shared array of a specified type.

- **typecode:** The data type (same as for Value).
- **size_or_initializer:** Either an integer specifying the size of the array, or a sequence (e.g., a list) to initialize the array's contents.
- **lock:** If set to true, creates a recursive lock to syncronize access.


### mp.Value() Example 

```python
import multiprocessing as mp

def worker_value(shared_int, shared_float):
    shared_int.value += 1
    shared_float.value *= 2.0

if __name__ == '__main__':
    shared_int = mp.Value('i', 10)      # Shared integer
    shared_float = mp.Value('d', 3.14)  # Shared double

    p = mp.Process(target=worker_value, args=(shared_int, shared_float))
    p.start()
    p.join()

    print(f"Shared integer: {shared_int.value}")
    print(f"Shared float: {shared_float.value}")
```

Program Output:

```text
Shared integer: 11
Shared float: 6.28
```

### mp.Array() Example 

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

Program Output:

```text
3.1415927
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

Here is a break down of the above example:

We need to import **Value** and/or **Array**. There are other methods of sharing data, but will wait later in the course to talk about them.

```python
from multiprocessing import Process, Value, Array
```

Next, we can use **Value** and/or **Array** to create the shared variables that will be used between processes. For both Value and Array, they take two arguments. 

- The first one is the data type. `d` indicates a double precision float and `i` indicates a signed integer.
- The second is the initial value for `Value()` or the list of values for `Array`.

```python
num = Value('d', 0.0)
arr = Array('i', range(10))
```

For other examples:

```python
count = Value('i', 0)   			   # create a shared integer count
counts = Array('i', [0, 0, 0, 0, 0])   # Create shared array of 5 values
```

Here we just pass them to the process using the `args` argument.

```python
p = Process(target=f, args=(num, arr))
```

Using these shared variables is a little different. For shared `Value()` variables, you need to use `.value` to use them. For the shared `Array()` variable, you access them normally using square brackets (`[]`).

```python
def f(n, a):
	n.value = 3.1415927
	for i in range(len(a)):
	    a[i] = -a[i]
```

When using shared variables, remember that if there are processes writing to and reading from them, then you need to stop a potential race condition by using a shared lock.

## 5.4 Process Pools

Process pools provide a convenient way to manage a fixed number of worker processes and distribute tasks among them. They are particularly useful for parallelizing independent computations across multiple CPU cores. Python offers two main classes for creating process pools: multiprocessing.Pool (older, more established) and concurrent.futures.ProcessPoolExecutor (newer, more consistent interface with thread pools).

### Process Pool and Map() Function

Please review the [Python documentation](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool) on the multiprocessing module for in-depth information.

The pool feature of the multiprocessing package allows you to indicate the number of processes that you want to use for a parallel section of your program.  The map function takes in a reference to a function that you want to apply to the process pool. The function that you place in the first argument can only have 1 argument. 

The second argument is a list of items that you want the processes to use. The Pool will divide up the list for the processes in the pool to use. In this case, `'John'` was used by one process where the process called `func('John')`. Then 'Mary' was used by the other process (or the same one for 'John'), etc. until all of the items in the list are used.

In the output, you can see that process 1 called func() with two names from the list and the other process handled the other three. (The function func() required a sleep() call because all of the names in the list would have been processed by just one of the processes).

```python
import os
import time
import multiprocessing as mp

def func(name):
    time.sleep(0.5)
    print(f'{name}, {os.getpid()}')

if __name__ == '__main__':

    names = ['John', 'Mary', 'April', 'Murry', 'George']

    # Create a pool of 2 processes
    with mp.Pool(2) as p:
        # map those 2 process to the function func()
        # Python will call the function func() alternating items in the names list.
        # the two processes will run in parallel
        p.map(func, names)
```

output:

```
Mary, 23316
Murry, 23316
John, 3672
April, 3672
George, 3672
```

Here is an example of using tuples for the argument to the function used for a process pool. Notice the output order from the program. The first tuple in the list was `(1, 2)`. However, it wasn't the first tuple processed by the pool. You can't depend on any order of processing while using a pool - you just know that it will be all processed.

```Python
import os
import time
import multiprocessing as mp

def add_two_numbers(values):
	# The sleep is here to slow down the program
    time.sleep(0.5)
    number1 = values[0]
    number2 = values[1]
    print(f'PID = {os.getpid()}: {number1} + {number2} = {number1 + number2}')

if __name__ == '__main__':

	# create argument list for the pool
    numbers = []
    numbers.append((1, 2))
    numbers.append((11, 52))
    numbers.append((12, 62))
    numbers.append((13, 72))
    numbers.append((1312, 2272))
    numbers.append((1332, 732))
    numbers.append((13434, -23272))

    print(f'Numbers list: {numbers}')

    # Create a pool of 2 processes
    with mp.Pool(2) as p:
        p.map(add_two_numbers, numbers)
```

output:

```
Numbers list: [(1, 2), (11, 52), (12, 62), (13, 72), (1312, 2272), (1332, 732), (13434, -23272)]
PID = 27284: 1 + 2 = 3
PID = 27284: 12 + 62 = 74
PID = 27284: 1332 + 732 = 2064
PID = 6132: 11 + 52 = 63
PID = 6132: 13 + 72 = 85
PID = 6132: 1312 + 2272 = 3584
PID = 6132: 13434 + -23272 = -9838
```

Here is the output of the same program above using a pool size of 4. Notice that the list of numbers was spread over the processes. (ie., load balancing).

```
PID = 26204: 13 + 72 = 85
PID = 4520: 1 + 2 = 3
PID = 4520: 1332 + 732 = 2064
PID = 27168: 11 + 52 = 63
PID = 27168: 1312 + 2272 = 3584
PID = 14268: 12 + 62 = 74
PID = 14268: 13434 + -23272 = -9838
```

Finally, the size of your process pool should not be greater than the number of CPUs on your computer.

### Asynchronous vs Synchronous Programming

In programming, synchronous operations block instructions until the task is completed, while asynchronous operations can execute without blocking. Asynchronous operations are generally completed by firing an event or by calling a provided callback function.

**Asynchronous != Parallelism**

It is important to understand that asynchronous program is not parallelism, it is concurrency.

### Coding Examples Using Process Pools

#### Example 1

In this first example, we are using the `map()` function to map a list to a function. Note that we need to get all of the data in a list before the call to the `map()` function and that the `map()` call is synchronous meaning that it doesn't return until the function is finished.

We will be using the function `apply_async()` with process pools for this week's assignment. Review the coding example below and the linked articles above in this document.

```python
# Example using a pool map

import multiprocessing as mp 

from cse251 import *

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

if __name__ == "__main__":
    log = Log(filename_log='map.log', show_terminal=True)
    log.start_timer()
    pool = mp.Pool(4)
    results = pool.map(sum_all_values, range(100000000, 100000000 + 100))
    log.stop_timer('Finished: ')
    print(results)
```

Output:

```
12:13:39| Finished:  = 234.72213530
```

#### Example 2

This second example is using the function `apply_async()`. It is asynchronous meaning that the function will return before the processes are finished processes the data.

```python
# Example using pool apply_asyc()

import multiprocessing as mp 

from cse251 import *

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total
    
if __name__ == "__main__":
    log = Log(filename_log='apply_async.log', show_terminal=True)
    log.start_timer()
    pool = mp.Pool(4)
    results = [pool.apply_async(sum_all_values, args=(x,)) for x in range(10000, 10000 + 10)]

    # do something else

    # collect all of the results into a list
    output = [p.get() for p in results]
    log.stop_timer('Finished: ')
    print(output)

```

output:

```
11:54:15| Finished:  = 0.98407470
[50005000, 50015001, 50025003, 50035006, 50045010, 50055015, 50065021, 50075028, 50085036, 50095045]
```

Here is a breakdown of the previous example:

---

The `results` variable is a list of *future* work by the process pool. This statement is quick to run as once the list is complete, Python will run the next line in your program. At this point, some of the processes in the pool has been started and is processing the data.

```python
results = [pool.apply_async(sum_all_values, args=(x,)) for x in range(10000, 10000 + 10)]
```

With this next statement, the program is now collecting the results of the process pool. If the pool is finished processing all of the data, then this statement is quick. However, if any process in the pool is still doing work, then this statement is synchronous (ie., waits for the pool to finish)

```python
output = [p.get() for p in results]
```

#### Example 3

Here is the same program from example 2 processing a larger range of values.

```python
# Example using pool apply_asyc()

import multiprocessing as mp 

from cse251 import *

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total
    
if __name__ == "__main__":
    log = Log(filename_log='apply_async.log', show_terminal=True)
    log.start_timer()
    pool = mp.Pool(4)
    results = [pool.apply_async(sum_all_values, args=(x,)) for x in range(100000000, 100000000 + 100)]
    output = [p.get() for p in results]
    log.stop_timer('Finished: ')
    print(output)
```

Output:

```
 Finished:  = 183.79569150
[5000000050000000, 5000000150000001, 5000000250000003, 5000000350000006, 5000000450000010, 5000000550000015, 5000000650000021, 5000000750000028, 5000000850000036, 5000000950000045, 5000001050000055, 5000001150000066, 5000001250000078, 5000001350000091, 5000001450000105, 5000001550000120, 5000001650000136, 5000001750000153, 5000001850000171, 5000001950000190, 5000002050000210, 5000002150000231, 5000002250000253, 5000002350000276, 5000002450000300, 5000002550000325, 5000002650000351, 5000002750000378, 5000002850000406, 5000002950000435, 5000003050000465, 5000003150000496, 5000003250000528, 5000003350000561, 5000003450000595, 5000003550000630, 5000003650000666, 5000003750000703, 5000003850000741, 5000003950000780, 5000004050000820, 5000004150000861, 5000004250000903, 5000004350000946, 5000004450000990, 5000004550001035, 5000004650001081, 5000004750001128, 5000004850001176, 5000004950001225, 5000005050001275, 5000005150001326, 5000005250001378, 5000005350001431, 5000005450001485, 5000005550001540, 5000005650001596, 5000005750001653, 5000005850001711, 5000005950001770, 5000006050001830, 5000006150001891, 5000006250001953, 5000006350002016, 5000006450002080, 5000006550002145, 5000006650002211, 5000006750002278, 5000006850002346, 5000006950002415, 5000007050002485, 5000007150002556, 5000007250002628, 5000007350002701, 5000007450002775, 5000007550002850, 5000007650002926, 5000007750003003, 5000007850003081, 5000007950003160, 5000008050003240, 5000008150003321, 5000008250003403, 5000008350003486, 5000008450003570, 5000008550003655, 5000008650003741, 5000008750003828, 5000008850003916, 5000008950004005, 5000009050004095, 5000009150004186, 5000009250004278, 5000009350004371, 5000009450004465, 5000009550004560, 5000009650004656, 5000009750004753, 5000009850004851, 5000009950004950] 
```

#### Example 4

In this example, the `pool()` using the method `apply_async()`. The way that this works is that instead of having all of the tasks in a list and the results in a list, as each process finishes their job with the data, the callback function is called. In this callback function, you can collect the results - one at a time for the process pool.

When we have processes, global variables can't be used because they each have their own version of the GIL. When using the callback function feature, that callback function is running in the main thread of the program where it can use any global variables of the program. This means that there is no issue with shared data between processes.

In order to know when the pool is finished, you need to have the statements `pool.close()` and `pool.join()`.

```python
# Example using pool apply_asyc() and callback function

import multiprocessing as mp
import time

from cse251 import *

result_list = []

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

def log_result(result):
    # This is called whenever sum_all_values(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def apply_async_with_callback():
    log = Log(filename_log='callback.log', show_terminal=True)
    log.start_timer()
    pool = mp.Pool(4)

    log.step_timer('Before For loop')
    for i in range(100000000, 100000000 + 100):
        pool.apply_async(sum_all_values, args = (i, ), callback = log_result)
    log.step_timer('After For loop')

    # Do something while the processes are doing their work

    # Need to know when the pool is finished
    pool.close()
    pool.join()

    log.stop_timer('Finished: ')

    # display the global variable of the results from the pool
    print(result_list)

if __name__ == '__main__':
    apply_async_with_callback()
```

Output:

Notice that the `for` loop was quick to get the data to the process pool.

```
12:18:57| Before For loop = 0.10709840
12:18:57| After For loop = 0.11021600
12:22:12| Finished:  = 195.08828210
```

#### Example 5

Once a process pool is created, you are free to add jobs to the pool any time in your program as long as it's before calling `pool.close()` and `pool.join()`. Here is an example where the program adds a job to the pool after sleeping a little while.

The advantage of using a call back function with the process pool is that the program doesn't need to have all of the data collected in order for the pool to start doing something.

```python
# Example using pool apply_asyc() and callback function

import multiprocessing as mp
import time

from cse251 import *

result_list = []

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

def log_result(result):
    # This is called whenever sum_all_values(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def apply_async_with_callback():
    log = Log(filename_log='callback.log', show_terminal=True)
    log.start_timer()
    pool = mp.Pool(4)

    # Add job to the pool
    pool.apply_async(sum_all_values, args = (100000000, ), callback = log_result)
    
    time.sleep(1)       # Do something - this is the main thread sleeping

    pool.apply_async(sum_all_values, args = (100000001, ), callback = log_result)

    time.sleep(1)       # Do something

    pool.apply_async(sum_all_values, args = (100000002, ), callback = log_result)

    time.sleep(1)       # Do something

    pool.apply_async(sum_all_values, args = (100000003, ), callback = log_result)

    # Do something while the processes are doing their work

    # Need to know when the pool is finished
    pool.close()
    pool.join()

    log.stop_timer('Finished: ')

    # display the global variable of the results from the pool
    print(result_list)

if __name__ == '__main__':
    apply_async_with_callback()
```

Output:

```
12:29:59| Finished:  = 8.19670030
[5000000050000000, 5000000150000001, 5000000250000003, 5000000350000006]
```

## 5.5 When to Use Processes

Choosing between processes and threads depends on the specific characteristics of your application and the goals you're trying to achieve. Processes offer distinct advantages in certain scenarios, particularly when dealing with CPU-bound tasks, requiring increased reliability, or aiming for scalability across multiple CPU cores.

1. CPU-bound Tasks (Overcoming the GIL)

    The most significant reason to choose processes over threads in Python is to overcome the limitations of the Global Interpreter Lock (GIL) for CPU-bound tasks.

2. Increased Reliability (Process Isolation)

    Processes provide process isolation, meaning that each process runs in its own separate memory space.  This isolation has significant implications for reliability:

3. Scalability (Utilizing Multiple Cores)

    Processes allow you to scale your application to utilize multiple CPU cores effectively.  This is crucial for achieving maximum performance on modern multi-core processors.

### When `Not` to Use Processes:

While processes offer significant advantages, they also have some drawbacks:

1. Creating and managing processes is more resource-intensive than creating and managing threads. There's more overhead in terms of memory usage and context switching time.
1. Inter-process communication (IPC) is more complex than inter-thread communication. Data needs to be serialized (pickled) for transmission between processes, which adds overhead.
1. Sharing data between processes requires explicit IPC mechanisms (queues, pipes, shared memory), which can be more challenging to implement correctly than simply sharing variables between threads.


## 5.6 Process Synchronization

When multiple processes share resources (e.g., shared memory, files, or even conceptual resources like a counter), you need synchronization mechanisms to prevent race conditions and ensure data consistency.  Python's multiprocessing module provides several synchronization primitives that are process-safe, mirroring the primitives available for threads in the threading module. The difference is these are designed to work across process boundaries.

The following synchronization tools are the same as the ones we read about when learning threads.  The main difference is that they must be created from the `multiprocessing` module.

### mp.Lock()

provides a mutual exclusion lock, often simply called a "mutex". It ensures that only one process can hold the lock at a time, providing exclusive access to a shared resource.

### mp.Semaphore()

`mp.Semaphore()` is a more general synchronization primitive than a lock.  It maintains an internal counter and allows a specified number of processes to access a resource concurrently.

### mp.Condition()

`mp.Condition()` is used for more complex synchronization scenarios where processes need to wait for a specific condition to become true and be notified by other processes when that condition changes.  It combines a lock with wait/notify capabilities.

