# Lesson 3: Threads, Inter-Process Communication & Synchronization Primitives

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
3.1 | [Threads Best Practices and Limitations](#threads-best-practices-and-limitations)
3.2 | [Thread Safety](#thread-safety) :key:
3.3 | [Context Switching](#context-switching)
3.4 | [Thread Pools](#thread-pools) :key:
3.5 | [Thread Communication](#thread-communication) :key:

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

 








# Threads Best Practices and Limitations

While threads offer a way to achieve concurrency within a single Python process, they come with specific strengths and weaknesses. Understanding these is crucial for writing efficient and correct multithreaded programs.

## When to Use Threads (I/O-bound tasks)

Threads in Python are best suited for I/O-bound tasks.  These are tasks where the program spends a significant amount of time waiting for external operations to complete, such as:

- **Network requests:** Fetching data from a website, interacting with an API, or communicating with a database server.
- **Disk I/O:** Reading from or writing to files on the hard drive.
- **User input:** Waiting for the user to type something or click a button.
- **Interacting with external devices:** Communicating with hardware like printers or sensors.

In these scenarios, a thread can perform a blocking operation (like waiting for a network response) without halting the entire program.  While one thread is blocked, the Python interpreter can switch to another thread that's ready to run.  This context switching allows the program to remain responsive and utilize resources more effectively.


## The GIL's Impact on CPU-bound Tasks

The Global Interpreter Lock (GIL) is a significant limitation of CPython (the standard Python implementation written in the C language) when it comes to achieving true parallelism with threads for CPU-bound tasks.

What is the GIL? The GIL is a mutex (mutual exclusion lock) that allows only one thread to hold control of the Python interpreter at any given time.  This means that even on a multi-core processor, only one thread can execute Python at a time.

What is the impact on CPU-bound tasks?  CPU-bound tasks are those that spend most of their time performing computations, such as:

- Complex mathematical calculations.
- Image processing.
- Large-scale data analysis.

For these tasks, using threads in Python will **not result in a speedup proportional to the number of cores**.  In fact, it can sometimes even slow down the program due to the overhead of thread management and context switching. The GIL serializes the execution of Python, preventing true parallel execution.

Why does the GIL exist? The GIL simplifies CPython's implementation, particularly memory management. It makes it easier to integrate C extensions and ensures thread safety for the interpreter's internal data structures. Removing the GIL is a complex undertaking that has been explored but poses significant challenges to maintaining compatibility and performance.


## Debugging Multithreaded Programs (Challenges and Techniques)

Debugging multithreaded programs can be significantly more challenging than debugging single-threaded code due to:

- **Non-determinism:** The order in which threads execute can vary, making it difficult to reproduce bugs consistently. Race conditions (discussed below) can appear intermittently.
*Deadlocks:** Threads can get stuck waiting for each other indefinitely, leading to a program freeze.
- **Heisenbugs:** Bugs that disappear or change their behavior when you try to observe them (e.g., Using a debugger, or print() statements). This can happen because the act of debugging can alter the timing and execution order of threads.

Logging (writing print statements to a file), can help track the flow of execution and the state of assignments and programs.










# Thread Safety

Building upon the previous introduction of synchronization primitives, we now delve deeper into the core concept of thread safety. Thread safety is paramount in concurrent programming, and understanding it is crucial for writing reliable multithreaded applications.


## Critical Sections and Thread Safety

In the context of multithreaded programming, a critical section is a part of the code that accesses shared resources (like variables, files, or data structures) that can be modified by multiple threads.  The critical section is where race conditions can occur if not properly protected.  Thread safety, in essence, revolves around managing access to these critical sections.

## Defining Thread Safety

Code is considered thread-safe if it functions correctly when executed concurrently by multiple threads, without any unexpected or incorrect behavior.  More formally:

- **Correctness:** Thread-safe code produces the same, predictable results regardless of the interleaving of thread executions. The order in which threads execute portions of the critical section does not affect the final outcome or the integrity of the shared data.
-  **No Data Races:** Thread-safe code avoids data races. A data race happens when at least two threads access the same shared memory location, at least one of them is writing, and there's no explicit synchronization mechanism to order those accesses.
- **No Deadlocks, Livelocks, or Starvation:** A thread-safe design avoids situations where threads become permanently blocked (deadlock), repeatedly attempt an operation that always fails (livelock), or are perpetually denied access to a resource (starvation).

## Why is Thread Safety Essential?

Thread safety is essential for several reasons:

- **Data Integrity:** Without thread safety, concurrent access to shared data can lead to corruption. Incorrect updates can occur, leaving data in an inconsistent or invalid state.
- **Program Correctness:** Race conditions and other thread-safety issues can lead to unpredictable program behavior, making it difficult to reason about the program's logic and debug errors. The program may produce correct results sometimes and incorrect results at other times, seemingly at random.
- **Reliability and Stability:** Applications that are not thread-safe are prone to crashes, hangs, and other unexpected failures, especially under heavy load or when running on multi-core processors.
- **Security:** In some cases, thread-safety issues can even be exploited to create security vulnerabilities.

## Common Sources of Thread Safety Issues

The most common source of thread safety problems is shared mutable state.  This refers to data that can be modified (mutable) and is accessible by multiple threads (shared).  Some key scenarios:

### Shared Variables

Global variables, instance variables of shared objects, and elements within shared data structures (lists, dictionaries, etc.) are all examples of shared mutable state.  If multiple threads can read from and write to these variables, it can lead to unpredictable behavior unless properly synchronized.

### Non-Atomic Operations

Even seemingly simple operations like incrementing a variable (counter += 1) are often not atomic at the bytecode level. They involve multiple steps (read, modify, write), creating opportunities for race conditions if accessed by multiple threads simultaneously without proper synchronization.

### Shared Resources (Files, Databases, etc.)

Accessing external resources like files or databases from multiple threads requires careful coordination.  Multiple threads writing to the same file simultaneously without proper locking can lead to data corruption or loss.  Database connections often need to be managed carefully to avoid conflicts and ensure data consistency.

### Incorrect Use of Synchronization Primitives

Even when using synchronization primitives (locks, semaphores, etc.), incorrect usage can lead to problems.  For example:

- **Deadlock**: Two or more threads are blocked indefinitely, waiting for each other to release resources. This often occurs when locks are acquired in different orders by different threads.

- **Forgotten Locks**: Failing to acquire a lock before accessing a shared resource.
**Releasing Locks Too Early/Late**: Holding a lock for too short or too long a time can either lead to race conditions or reduce concurrency unnecessarily.

- **Nested Locks**: Acquiring the same lock multiple times without using an RLock (reentrant lock) can cause deadlocks.

- **Livelock**: Similar to deadlock.  Threads are not blocked, but they keep retrying an action that will always fail because of another thread.










# Context Switching

Context switching is a fundamental concept in operating systems and concurrency, and it's essential for understanding how threads are managed and how they share CPU time. It's the mechanism that allows multiple threads to appear to run simultaneously, even on a single-core processor.

## Basic Overview of Context Switching

Context switching is the process of saving the state of one thread and restoring the state of another, allowing the CPU to switch between different threads of execution.  It's like pausing one task and resuming another, ensuring that each task can continue from where it left off.

Steps Involved in a Context Switch:

1. Triggering the Switch: A context switch can be triggered by several events:

    - **Time Slice Expiration:** The operating system's scheduler allocates a certain amount of time (a "time slice" or "quantum") to each thread. When a thread's time slice expires, the scheduler triggers a context switch.
    - **Blocking System Call:** When a thread makes a system call that blocks (e.g., waiting for I/O), the operating system immediately switches to another runnable thread. This prevents the CPU from being idle while waiting.
    - **Voluntary Yield:** A thread can voluntarily relinquish control of the CPU (e.g., using time.sleep(0) in Python, although this relies on the GIL's behavior and is not a true yield in all cases).
    - **Interrupt:** A hardware interrupt (e.g., from a timer or I/O device) can interrupt the currently running thread and trigger a context switch.
    - **Higher-Priority Thread becomes Ready:** When a thread that has a higher scheduling priority than the current thread becomes ready, it may trigger an immediate context switch.
    
1. Saving the Context of the Current Thread. The operating system saves the current state of the running thread. This "context" includes:

    - **Program Counter (PC):** The address of the next instruction to be executed.
    - **Registers:** The values stored in the CPU's registers (general-purpose registers, stack pointer, etc.).
    - **Stack Pointer:** The memory address representing the current top of the thread's stack.
    - **Thread State:** Information about the thread's status (e.g., running, blocked, ready).
    - **Memory Management Information:** Pointers to the thread's memory space.

1. The operating system's scheduler chooses the next thread to run based on its scheduling algorithm.

1. The operating system loads the saved context of the selected thread into the CPU. This includes restoring the program counter, registers, stack pointer, and other relevant information.

1. The CPU begins executing instructions from where the newly loaded thread left off (using the restored program counter).

## Operating System Management of Threads

The operating system (OS) plays a crucial role in managing threads

- The OS provides system calls for **creating and terminating threads**. When a thread is created, the OS scheduler is responsible for **deciding which thread to run and for how long**. Different scheduling algorithms have different priorities (e.g., fairness, responsiveness, throughput).

- The OS provides mechanisms for **thread synchronization** (e.g., mutexes, semaphores, condition).  

- The OS may provide mechanisms for **threads to communicate with each other** (e.g., pipes, shared memory, message queues), although these are often used more directly in multiprocessing than in threading within a single Python process (due to the GIL).


## Overhead of Context Switching

Context switching is not free.  It introduces overhead, which can impact the performance of multithreaded programs.  The two main issues are CPU time and memory usage. Context switching is still very fast.  However, the goal of any programmer is to limit the number of Context switches.

### Implications for Python Threads

- As discussed earlier, the overhead of context switching is less significant for I/O-bound tasks because the threads spend much of their time waiting anyway. The context switch allows other threads to form useful work during these waiting periods. For CPU-bound tasks, the overhead of context switching (combined with the GIL's limitations) often outweighs the benefits of threading in CPython.
- Excessive context switching can degrade performance. If you have too many threads competing for CPU time, the system may spend more time switching between them than actually executing their code. This is known as "thrashing".
- Thread pools help manage the overhead by reusing a limited number of threads instead of creating and destroying them repeatedly. This reduces the frequency of thread creation and destruction, and can improve efficiency.










# Thread Pools

Thread pools provide a powerful and efficient way to manage threads in concurrent applications. They address many of the challenges associated with creating and destroying threads on demand.

## Why Thread Pools

Creating and destroying threads is a relatively expensive operation. Each thread consumes system resources, including memory for its stack and kernel resources for managing the thread. If an application creates and destroys many short-lived threads, the overhead of these operations can become significant, degrading performance.

Thread pools solve this problem by creating a pool of worker threads when the application starts. These threads are then reused to execute multiple tasks, amortizing the cost of thread creation and destruction.

- **Thread creation and destruction are minimized**. Threads are created once and reused, reducing the overhead associated with these operations.
- The number of **threads in the pool is typically limited**. This prevents the application from creating an excessive number of threads, which could lead to resource exhaustion (e.g., running out of memory or overwhelming the scheduler).
- Thread pools provide a **convenient interface for submitting tasks** and managing their execution. You don't have to manually create, start, and join threads.
- **Improved Responsiveness**: Tasks can be executed immediately if a thread is available in the pool, without waiting for a new thread to be created.

## Thread Pool Example 1

```python
import concurrent.futures           # Required for Thread Pools
import requests
import time

def download_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.status_code, len(response.content)
    except requests.exceptions.RequestException as e:
        return None, str(e)

urls = [
    "https://www.github.com",
    "https://code.visualstudio.com",
    "https://www.lds.com",
    "https://www.python.org",
    "https://docs.python.org",
    "https://pypi.org",
    "https://www.wikipedia.org",
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://creativecommons.org",
    "https://www.gnu.org",
    "https://www.eff.org",
    "https://www.w3.org",
    "https://www.ietf.org",
    "https://example.com",
    "https://example.net",
    "https://example.org",
    "https://www.rfc-editor.org",
    "https://www.iana.org",
    "https://www.internet.org",
    "https://www.sqlite.org/index.html",
    "https://pandas.pydata.org",
    "https://numpy.org",
    "https://scipy.org",
]

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

    # map all the urls to the download_page function
    # This will use all 10 threads in the pool.  This means that 10 URLS
    # will be downloaded concurrently.
    results = executor.map(download_page, urls)

    for url, result in zip(urls, results):
        status_code, content_length = result
        if status_code:
            print(f"Downloaded {url}: Status {status_code}, Length: {content_length}")
        else:
            print(f"Error downloading {url}: {content_length}")

end_time = time.time()

# --- Sequential Version (for comparison) ---
print()
start_time_sequential = time.time()
for url in urls:
    status, length = download_page(url)
    if status:
        print(f"Downloaded {url}: Status {status}, Length: {length}")
    else:
        print(f"Error downloading {url}: {length}")

end_time_sequential = time.time()

print()
print(f"Total time taken (with thread pool): {end_time - start_time:.2f} seconds")
print(f"Total time taken (sequential): {end_time_sequential - start_time_sequential:.2f} seconds")

```

Program Output:

Output for 10 threads in the pool:

```text
# Just the timing details
Total time taken (with thread pool): 1.58 seconds
Total time taken (sequential): 6.03 seconds
```

Output for 2 threads in the pool:

```text
Total time taken (with thread pool): 3.53 seconds
Total time taken (sequential): 6.11 seconds
```


## Thread Pool Example 2

Here is another example of the thread pool.  However, in this example, the work that each thread is doing is CPU-bound.  Therefore, it will not be faster.  This example is here to show that it is important to select threads only for I/O-bound tasks

```python
import concurrent.futures
import time
import math

def calculate_factorial(n):
    return math.factorial(n)

# Create a large array of values
numbers = [5, 10, 15, 20, 25, 30, 35, 40] * 10000

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Need to convert results to a list
    results = list(executor.map(calculate_factorial, numbers))

end_time = time.time()

# Sequential version for comparison
start_time_sequential = time.time()
results_sequential = [calculate_factorial(n) for n in numbers]
end_time_sequential = time.time()

print()
print(f"Time taken (with thread pool): {end_time - start_time:.4f} seconds")
print(f"Time taken (sequential): {end_time_sequential - start_time_sequential:.4f} seconds")
```

Program Output:

Here, you will notice that the time for the thread pool was a lot slower.  The slow down is caused by the overhead of managing the pool where the OS needs to schedule the threads.  The sequential version of this program doesn't have this overhead.

```text
Time taken (with thread pool): 0.5908 seconds
Time taken (sequential): 0.0097 seconds
```









# Thread Communication

Threads within a single process share the same memory space. This shared memory can be used for communication, but it also introduces significant challenges related to data integrity and synchronization. This section explores various mechanisms for thread communication, from the pitfalls of shared memory to robust synchronization primitives.

## Shared Memory

Shared memory is the most direct form of inter-thread communication.  Threads can directly access and modify the same variables and data structures in memory. While seemingly simple, this approach is fraught with danger if not managed carefully.

Challenges for shared memory:

- As discussed earlier, **race conditions** occur when multiple threads access and modify shared data concurrently, leading to unpredictable and incorrect results. The order of operations becomes non-deterministic.   
- **Without proper synchronization**, data can become corrupted or inconsistent due to partial updates or interleaved operations.
- Shared memory issues can be **extremely difficult to debug** due to their non-deterministic nature and the potential for subtle timing-dependent errors.  For example, adding a `print()` statement will change the timing of your threads and cause a different result.

### Race Conditions

Race conditions are a fundamental problem in concurrent programming. A race condition occurs when the behavior of a program depends on the relative timing or interleaving of multiple threads (or processes). In essence, multiple threads are "racing" to access or modify shared resources.   

The outcome of a program with a race condition can vary unpredictably from one run to the next, making it difficult to debug.  Race conditions can lead to data corruption, inconsistent state, and program crashes.

The main solution to race conditions is to use a lock.

## Queues for Threads

Queues are a fundamental and versatile mechanism for inter-thread communication.  They provide a thread-safe way to exchange data between threads, simplifying synchronization and reducing the risk of race conditions and deadlocks. This section focuses on the `queue.Queue` class from Python's queue module, which is specifically designed for use with threads.

### Concept of First-In, First-Out (FIFO)

A queue, in the context of computer science, is a data structure that follows the First-In, First-Out (FIFO) principle. This means that the first element added to the queue is the first element removed.  Think of it like a line at a store – the first person in line is the first person served.   

In the context of inter-thread communication, this means that messages or data items are processed in the order they are added to the queue. This ordering guarantee is crucial for many concurrent programming patterns.

## Advantages of Queues for Thread Communication:

- `queue.Queue` is designed to be **thread-safe**. All the necessary locking and synchronization are handled internally, eliminating the need for manual lock management and reducing the risk of race conditions.
- Queues provide a **higher-level abstraction for communication**, making code easier to read, write, and reason about. You don't have to deal directly with low-level synchronization primitives like locks.
- The **blocking behavior of `put()` and `get()`** (when `block=True`) simplifies coordination between threads. Threads can wait for data to become available or for space to become free without busy-waiting (repeatedly checking a condition).
- The `maxsize` parameter allows you to create **bounded queues**, preventing producers from overwhelming consumers and potentially running out of memory.
- **FIFO queues** guarantee that items are processed in the order they are added, which is essential for many applications.


### Creating and Using Queues in Python (queue.Queue)

Python's queue module provides the Queue class for creating thread-safe queues:

```python
import queue

# Create a queue for threads to communicate with each other
q = queue.Queue()
```

Click on [Main Methods of queue.Queue](https://docs.python.org/3/library/queue.html) to review the methods of a queue.  Note, that `qsize()`, `empty()`, `full()` are approximate in their return values.  See the documentation to learn more.

### Queue Example

Note that in this example, the thread receiving items from the queue uses a `while True:` loop. This works because the thread waits for a special signal (a sentinel value) in the queue to know when processing is finished. In this case, the producer thread places `None` into the queue as the sentinel, indicating to the consumer thread that it should stop.


```python
import threading
import queue
import time
import random

def producer(q, num_items):
    for i in range(num_items):
        item = random.randint(1, 100)  # Generate a random item

        q.put(item)  # Put the item in the queue

        print(f"Producer: Produced {item}")

        time.sleep(random.random() * 0.1) #simulate delay

    # Add a sentinel.  This is how the consumer() function knows
    # that there are no more items coming down the queue.
    q.put(None) 

def consumer(q):
    while True:
        item = q.get()  # Get an item from the queue (blocks if empty)
        if item is None:
            break
        print(f"Consumer: Consumed {item}")
        time.sleep(random.random() * 0.2) #simulate delay

if __name__ == '__main__':
    q = queue.Queue()
    num_items = 10

    producer_thread = threading.Thread(target=producer, args=(q, num_items))
    consumer_thread = threading.Thread(target=consumer, args=(q,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()  # Wait for the producer to finish
    consumer_thread.join()  # wait for the consumer to finish

    print("Producer-consumer example finished.")
```

Program Output:

```text
Producer: Produced 83
Consumer: Consumed 83
Producer: Produced 10
Producer: Produced 67
Consumer: Consumed 10
Producer: Produced 64
Producer: Produced 24
Consumer: Consumed 67
Producer: Produced 4
Producer: Produced 14
Producer: Produced 27
Producer: Produced 87
Producer: Produced 3
Consumer: Consumed 64
Consumer: Consumed 24
Consumer: Consumed 4
Consumer: Consumed 14
Consumer: Consumed 27
Consumer: Consumed 87
Consumer: Consumed 3
Producer-consumer example finished.
```

## Queue Example 2

Here, there are 3 threads adding to the queue and 3 threads reading from it.  Note, that the `producer()` MUST place a `None` item on the queue for **each consumer thread**.  Also, the number of producer threads to not need to match the number of consumer threads.

```python
import threading
import queue
import time
import random

THREAD_COUNT = 3

def producer(thread_index, q, num_items):
    for i in range(num_items):
        item = random.randint(1, 100) * (thread_index + 1) ** 10

        q.put(item)  # Put the item in the queue

        print(f"Producer: Produced {item}")

        time.sleep(random.random() * 0.1)

    # Add a sentinel.  This is how the consumer() function knows
    # that there are no more items coming down the queue.
    # ALL consumers() MUST receive a None so that they can stop
    for i in range(THREAD_COUNT):
        q.put(None) 

def consumer(q):
    while True:
        item = q.get()  # Get an item from the queue (blocks if empty)
        if item is None:
            break
        print(f"Consumer: Consumed {item}")
        time.sleep(random.random() * 0.2)

if __name__ == '__main__':
    q = queue.Queue()
    num_items = 5

    producers = []
    consumers = []

    for i in range(THREAD_COUNT):
        producers.append(threading.Thread(target=producer, args=(i, q, num_items)))
        consumers.append(threading.Thread(target=consumer, args=(q,)))

    for p in producers + consumers:
        p.start()

    for p in producers + consumers:
        p.join()

    print("Producer-consumer example finished.")
```

Program Output:

```text 
Producer: Produced 67
Producer: Produced 2048
Producer: Produced 3483891
Consumer: Consumed 67
Consumer: Consumed 2048
Consumer: Consumed 3483891
Producer: Produced 2302911
Producer: Produced 2
Producer: Produced 77
Producer: Produced 23
Producer: Produced 47104
Producer: Produced 19456
Consumer: Consumed 2302911
Producer: Produced 102400
Consumer: Consumed 2
Producer: Produced 2834352
Producer: Produced 34
Consumer: Consumed 77
Producer: Produced 5314410
Producer: Produced 73728
Consumer: Consumed 23
Producer: Produced 3070548
Consumer: Consumed 47104
Consumer: Consumed 19456
Consumer: Consumed 102400
Consumer: Consumed 2834352
Consumer: Consumed 34
Consumer: Consumed 5314410
Consumer: Consumed 73728
Producer-consumer example finished.
```


## Semaphores for Threads

Semaphores are a fundamental synchronization primitive used to control access to shared resources in concurrent programming. They are a more general mechanism than mutexes (locks) and can be used to manage situations where a limited number of threads (or processes) can access a resource concurrently. This section focuses on using semaphores within a single process, using Python's threading module.

### Concept of a Semaphore as a Counter

A semaphore maintains an internal counter. This counter represents the number of available "permits" or "slots" for accessing a shared resource.  I always like to think of a semaphore as just an integer with 2 operations:

- **acquire():** When a thread wants to access the resource, it attempts to acquire the semaphore. If the counter is greater than zero, the counter is decremented, and the thread is allowed to proceed. If the counter is zero, the thread blocks until another thread releases the semaphore.
- **release():** When a thread is finished with the resource, it releases the semaphore, incrementing the counter. This potentially unblocks a waiting thread.


### Binary Semaphore

A semaphore whose counter can only take the values 0 and 1. It's functionally equivalent to a mutex (lock). It's used to provide exclusive access to a single resource.

### Counting Semaphore

A semaphore whose counter can take any non-negative integer value. It's used to control access to a resource that has multiple instances or a limited capacity (e.g., a pool of database connections, a limited number of file handles).


### Semaphore Example

Here is an example of using a semaphore of value 3.  The program will only allow 3 threads to "access" the resource at a time.  You can use Python's `with` statement with a semaphore.  The `with` will acquire() and release() the semaphore for you.

```python
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
    print()
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
```

Program Output:

Notice that the program will allow 3 threads access to the resource, then the others must wait until a `release()` is called.

```text
----------------------------------------
Using with statement
----------------------------------------
Thread 0: Acquired resource.
Thread 1: Acquired resource.
Thread 2: Acquired resource.
Thread 1: Releasing resource.
Thread 3: Acquired resource.
Thread 0: Releasing resource.
Thread 4: Acquired resource.
Thread 2: Releasing resource.
Thread 3: Releasing resource.
Thread 4: Releasing resource.

----------------------------------------
Using acquire() and release()
----------------------------------------
Thread 0: Acquired resource.
Thread 1: Acquired resource.
Thread 2: Acquired resource.
Thread 1: Releasing resource.
Thread 3: Acquired resource.
Thread 0: Releasing resource.
Thread 4: Acquired resource.
Thread 3: Releasing resource.
Thread 4: Releasing resource.
Thread 2: Releasing resource.
```

## Semaphore VS Lock

Key differences and when to use a semaphore VS a lock

- Mutexes are used for exclusive access to a single resource. Only one thread can hold the lock at a time.
- Binary Semaphores are functionally equivalent to a mutex. Use interchangeably with `threading.Lock`.
- Counting Semaphores are used when you have a limited number of resources or want to allow a specific number of threads to access a resource concurrently.

Semaphores are a powerful tool for managing concurrency and controlling access to shared resources in multithreaded applications. They provide a flexible mechanism for both exclusive access (binary semaphores) and controlled concurrent access (counting semaphores). Understanding their behavior and proper usage is essential for writing robust and efficient concurrent code. Using the `with` statement is crucial for correct semaphore management, preventing deadlocks and resource leaks.


## Barriers for Threads

A barrier is a synchronization primitive that allows a group of threads to wait until all of them have reached a specific point in their execution before any of them can proceed. It acts like a checkpoint or rendezvous point for threads. Barriers are particularly useful in parallel computations where tasks have dependencies or need to be synchronized at certain stages. This section focuses on using barriers within a single process, using the threading module.

### Concept of a Barrier

Imagine a group of runners participating in a relay race. Each runner must wait at a designated point (the barrier) until all other runners in their team have also reached that point. Only when all runners are present can the next leg of the race begin. A barrier in concurrent programming works similarly.

- **Parties:** A barrier is initialized with a specific number of "parties" (threads in this case) that must reach the barrier.
- **Waiting:** When a thread calls `wait()` on the barrier, it blocks until all participating threads have also called `wait()`.
- **Release:** Once the required number of threads have called `wait()`, the barrier is "broken," and all waiting threads are released simultaneously (or as close to simultaneously as the operating system scheduler allows).
- **Reset:** After being broken, some barrier implementations can be reset for reuse. Python's `threading.Barrier` can be reused.

### Barrier Example

In this Python example, it is very important that the value of the barrier be a factor of the number of threads.  For example, you can have a barrier of 3 and 9 threads, but **not** a barrier of 4 and 9 threads.  Also, a barrier of value 1 serves no purpose.

```python
import threading
import time
import random

THREADS = 4

def worker(barrier, thread_id):
    print(f"Thread {thread_id}: Performing initialization...")
    time.sleep(random.uniform(0.1, 0.5))

    print(f"Thread {thread_id}: Waiting at the barrier...")
    worker_id = barrier.wait()

    print(f"Thread {thread_id}: Passed the barrier! (worker id: {worker_id})")

    # Perform the next stage of the computation, now synchronized
    time.sleep(random.uniform(0.1, 0.5))

    print(f"Thread {thread_id}: Finishing.")

if __name__ == '__main__':
    barrier = threading.Barrier(THREADS)

    threads = []
    for i in range(THREADS):
        thread = threading.Thread(target=worker, args=(barrier, i))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
```

Program Output:

Notice in the output that the threads hit the barrier in the order of 2, 3, 1, 0.  However, after the barrier was released, the order was 3, 1, 2, 0.  Remember that you don't control the scheduling of threads on the CPU, the OS does.

```text
Thread 0: Performing initialization...
Thread 1: Performing initialization...
Thread 2: Performing initialization...
Thread 3: Performing initialization...
Thread 2: Waiting at the barrier...
Thread 3: Waiting at the barrier...
Thread 1: Waiting at the barrier...
Thread 0: Waiting at the barrier...
Thread 0: Passed the barrier! (worker id: 3)
Thread 3: Passed the barrier! (worker id: 1)
Thread 1: Passed the barrier! (worker id: 2)
Thread 2: Passed the barrier! (worker id: 0)
Thread 0: Finishing.
Thread 3: Finishing.
Thread 2: Finishing.
Thread 1: Finishing.
```

