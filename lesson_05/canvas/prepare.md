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


5.1 Introduction to Processes
What are Processes? (Independent Execution Units)
Process vs. Thread (Key Differences)
Process Creation and Management (in Python's multiprocessing module)
Process IDs (PIDs)

5.2 Process Communication
multiprocessing.Queue
multiprocessing.Pipe
multiprocessing.Manager (Shared Objects, Proxies)
multiprocessing.shared_memory (Python 3.8+)

5.3 Process Pools
multiprocessing.Pool
concurrent.futures.ProcessPoolExecutor
Mapping Functions to Processes (Parallel Mapping)

5.4 When to Use Processes
CPU-bound Tasks (Overcoming the GIL)
Increased Reliability (Process Isolation)
Scalability (Utilizing Multiple Cores)

5.5 Process Synchronization
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
