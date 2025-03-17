# Lesson 5: Python Processes

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
5.1 | [Introduction to Processes](#Introduction-to-Processes)
5.2 | [Process Communication](#Process-Communication)
5.3 | [Process Pools](#Process-Pools)
5.4 | [When to Use Processes](#When-to-Use-Processes)
5.5 | [Process Synchronization](#Process-Synchronization)

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






















## Inter-Process Communication

Inter-Process Communication (IPC) refers to the mechanisms provided by an operating system that allow different processes to exchange data and synchronize their execution. Unlike threads, which share the same memory space within a single process, processes have their own independent memory spaces. This isolation provides robustness (a crash in one process won't necessarily bring down others), but it also necessitates specific mechanisms for communication and coordination.

### Why IPC? (Data Sharing, Coordination between Processes)

IPC is essential for a variety of reasons:

Data Sharing: Processes often need to share data. For example:

A web server might have multiple worker processes handling client requests, and they might need to share a cache of frequently accessed data.
A data processing pipeline might have separate processes for reading data, transforming it, and writing results.
A scientific simulation might distribute calculations across multiple processes to leverage multiple CPU cores.
Coordination and Synchronization: Processes may need to coordinate their activities. Examples include:

A producer process generating data and a consumer process consuming it.
Multiple processes accessing a shared resource (like a file or database) in a controlled manner.
A process launching and controlling other processes (e.g., a shell executing commands).
Signaling between processes. One process might need to notify another process that an event has occurred.
Resource Sharing:  IPC can be used to share resources that are not directly shareable, such as hardware devices or network connections. A single process might manage access to the resource and communicate with other processes via IPC.

Modularity and Fault Isolation:  Dividing a large application into multiple processes can improve modularity and fault isolation.  If one process crashes, it's less likely to affect other processes.  This is particularly important for long-running applications or systems that require high reliability.

Overcoming the GIL (in Python): As discussed in the threading section, CPython's Global Interpreter Lock (GIL) limits true parallelism for CPU-bound tasks within a single process.  Using multiple processes bypasses the GIL, allowing you to fully utilize multiple CPU cores for CPU-bound computations. This is the primary reason to use multiprocessing in Python.

### Challenges of IPC (Data Consistency, Synchronization)

While IPC is powerful, it introduces its own set of challenges, many of which are analogous to the challenges of multithreading, but often more complex due to the lack of shared memory:

Data Consistency:  Since processes don't share memory directly, ensuring data consistency requires careful design.  Data must be serialized (converted to a byte stream) for transmission between processes and then deserialized.  This process can introduce overhead and potential errors.

Synchronization:  Just like with threads, processes need mechanisms to synchronize their access to shared resources (even if those resources are managed through IPC).  Race conditions can occur if multiple processes try to modify the same data simultaneously without proper coordination.  IPC mechanisms often provide synchronization primitives similar to those used in threading (e.g., locks, semaphores, queues).

Overhead:  IPC is generally more expensive (in terms of performance) than inter-thread communication.  Data needs to be copied between processes, and the operating system kernel is involved in managing the communication channels. This overhead can be significant, especially for frequent or large data transfers.

Complexity:  IPC can be more complex to implement than threading.  You need to choose an appropriate IPC mechanism, handle serialization/deserialization, and manage the communication channels.

Deadlocks and Livelocks:  Similar to threading, improper use of synchronization primitives in IPC can lead to deadlocks (where processes are blocked indefinitely waiting for each other) or livelocks (where processes repeatedly change their state without making progress).

Security: When processes communicate across machine boundaries (e.g., over a network), security becomes a critical concern.  IPC mechanisms need to provide secure ways to authenticate processes and encrypt data.

Data Marshalling/Serialization:  Data passed between processes often needs to be converted into a format suitable for transmission. This process, called marshalling or serialization, can be complex, especially for custom data structures. Common serialization formats include JSON, XML, and Pickle (in Python).  However, Pickle is generally not recommended for untrusted data due to security risks.

Despite these challenges, IPC is a fundamental and essential technique for building robust, scalable, and parallel applications.  Python's multiprocessing module provides a high-level interface for working with processes and various IPC mechanisms, simplifying many of these complexities. The next sections will delve into specific IPC mechanisms available in Python.


## IPC Mechanisms
Pipes (Unidirectional, Bidirectional)
Message Queues
Shared Memory (OS-level, not just within a single process)
System V Shared Memory
POSIX Shared Memory
Signals

## 5.2 Process Communication
multiprocessing.Queue
multiprocessing.Pipe
multiprocessing.Manager (Shared Objects, Proxies)
multiprocessing.shared_memory (Python 3.8+)
multiprocessing.Value()
multiprocessing.Array()

## 5.3 Process Pools
multiprocessing.Pool
concurrent.futures.ProcessPoolExecutor
Mapping Functions to Processes (Parallel Mapping)
apply_async()

## 5.4 When to Use Processes
CPU-bound Tasks (Overcoming the GIL)
Increased Reliability (Process Isolation)
Scalability (Utilizing Multiple Cores)

## 5.5 Process Synchronization
multiprocessing.Lock, 
multiprocessing.Semaphore, 
multiprocessing.Condition, 
multiprocessing.Event (Process-safe versions)











Overall Module Goals:

Gain a deep understanding of processes in Python and their role in parallel programming.

Learn to effectively use the multiprocessing module for process management and inter-process communication.

Understand the concepts of synchronous and asynchronous programming, and their relevance to processes.

Explore different types of parallelism and the limitations imposed by Amdahl's Law.

Address practical considerations like thread safety and data serialization (pickling).


### Topic 1

### Topic 1

Day 1: Introduction to Processes and Parallelism

Reading:
"What are Processes?" (Conceptual overview of OS processes)
"Introduction to Parallelism":
Types of Parallelism: Data parallelism, task parallelism.
Benefits and challenges of parallel programming.
"Amdahl's Law":
Understanding the limitations of parallel speedup.
Calculating potential speedup.
Concepts:
Process vs. Thread
Concurrency vs. Parallelism
Speedup and Efficiency


Day 2: The multiprocessing Module: Process Creation and Management

Reading:
"Creating Processes in Python":
Using the multiprocessing.Process class.
Starting and joining processes.
"Process Managers":
Understanding the role of process managers.
Using multiprocessing.Manager for shared data.
Concepts:
Process lifecycle
Process isolation
Shared resources


Day 3: Inter-Process Communication (IPC)

Reading:
"Pipes and Queues":
Using multiprocessing.Pipe for duplex communication.
Using multiprocessing.Queue for thread-safe data transfer.
"Pickling":
Serializing and deserializing data for IPC.
Understanding pickling limitations and security concerns.
Concepts:
Data sharing between processes
Serialization and data integrity


Day 4: Synchronous vs. Asynchronous Programming with Processes

Reading:
"Synchronous vs. Asynchronous Programming":
Understanding blocking vs. non-blocking operations.
Applying asynchronous concepts to process-based workloads.
Review of previous days topics.
Concepts:
Event-driven programming
Blocking I/O and CPU-bound tasks


Day 5: map(), filter(), and multiprocessing.Pool

Reading:
"Parallel Data Processing with map() and filter()":
Applying built-in functions to parallelize data transformations.
"Using multiprocessing.Pool":
Distributing tasks across a pool of worker processes.
Asynchronous results with apply_async().
Concepts:
Task distribution
Result aggregation
different usages of mp.pool() (map(), apply_async())
Thread pools:


Day 6: Conditions and Synchronization

Reading:
"Conditions in multiprocessing":
Using multiprocessing.Condition for complex synchronization.
Implementing producer-consumer patterns.
Review of IPC methods.
Concepts:
Thread safety in a multiprocessing context.
Avoiding race conditions.
Signaling and waiting.


Day 7: Thread Safety and Process Interactions

Reading:
"Thread Safety in Multiprocessing":
Understanding the implications of shared resources.
Best practices for avoiding data corruption.
Review of Pickling.
Concepts:
Data consistency
Critical sections


Day 8: Other Parallel Packages and Libraries

Reading:
"Introduction to Alternative Parallel Packages":
Brief overview of joblib for parallel computing.
Introduction to Dask for parallel analytics.
When to use different parallel packages.
Concepts:
Scalability
Specialized parallel libraries


Day 9: Practical Applications and Case Studies

Reading:
"Case Studies in Process-Based Parallelism":
Examples of using multiprocessing for CPU-intensive tasks.
Parallelizing data processing pipelines.
Review of Amdahl's Law with practical examples.
Concepts:
Real-world parallel programming challenges.
Performance optimization.


Day 10: Review and Project Introduction

Reading:
Comprehensive review of all topics covered.
Project introduction and guidelines.
Q&A session.
Concepts:
Consolidation of knowledge.
Application of learned concepts in a practical project.
