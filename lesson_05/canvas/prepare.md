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
What are Processes? (Independent Execution Units)
Process vs. Thread (Key Differences)
Process Creation and Management (in Python's multiprocessing module)
Process IDs (PIDs)

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
