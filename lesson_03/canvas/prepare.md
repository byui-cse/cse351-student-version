# Lesson 3: Threads, Inter-Process Communication & Synchronization Primitives

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
3.1 | [Best Practices and Limitations](#Best-Practices-and-Limitations)
3.2 | [Thread Pools](#Thread-Pools)
3.3 | [Thread Communication](#Thread-Communication)
3.4 | [Introduction to Inter-Process Communication](#Introduction-to-Inter-Process-Communication)
3.5 | [IPC Mechanisms](#IPC-Mechanisms)
3.6 | [Synchronization Primitives](#Synchronization-Primitives)
3.7 | [Deadlock Prevention and Avoidance](#Deadlock-Prevention-and-Avoidance)


:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

3.1 Best Practices and Limitations
When to Use Threads (I/O-bound tasks)
The GIL's Impact on CPU-bound Tasks
Debugging Multithreaded Programs (Challenges and Techniques)
Thread Safety and Data Integrity

3.2 Thread Pools
Why Thread Pools? (Resource Management)
concurrent.futures.ThreadPoolExecutor (in Python)
Submitting Tasks to a Thread Pool
Managing Results (Futures)

3.3 Thread Communication
Shared Memory (and its challenges)
Race Conditions
Deadlocks, Livelocks, Starvation
queue Module (for inter-thread/process communication)
threading.Lock (Mutex)
threading.RLock (Reentrant Lock)
threading.Semaphore
threading.Condition (Wait/Notify Mechanisms)
threading.Event

3.4 Introduction to Inter-Process Communication
Why IPC? (Data Sharing, Coordination between Processes)
Challenges of IPC (Data Consistency, Synchronization)

3.5 IPC Mechanisms
Pipes (Unidirectional, Bidirectional)
Message Queues
Shared Memory (OS-level, not just within a single process)
System V Shared Memory
POSIX Shared Memory
Signals

3.6 Synchronization Primitives
Mutexes (Mutual Exclusion Locks)
Semaphores (Counting and Binary)
Condition Variables (Wait/Notify)
Barriers
Monitors (Higher-level Synchronization Construct)

3.7 Deadlock Prevention and Avoidance
Deadlock Conditions (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait)
Strategies for Deadlock Prevention (Resource Ordering, etc.)
Deadlock Avoidance (Banker's Algorithm - Conceptual)
Deadlock Detection and Recovery








### Topic 1

### Topic 1


States of a Process in an OS:
Start by establishing the foundation: how operating systems manage processes.
Introduce the common process states: New, Ready, Running, Waiting (Blocked), Terminated.
Explain the transitions between these states and the events that trigger them (e.g., I/O requests, scheduling).
Discuss the role of the process control block (PCB).

Pipes:
Introduce pipes as a basic mechanism for inter-process communication (IPC).
Explain the concept of unidirectional data flow between related processes (parent-child).
Demonstrate how to create and use pipes in Python (using the multiprocessing.Pipe module).
Provide examples of simple data transfer between processes.

Queues:
Introduce queues as a more versatile IPC mechanism.
Explain the concept of a first-in, first-out (FIFO) data structure for communication between processes.
Demonstrate how to create and use queues in Python (using the multiprocessing.Queue module).
Highlight the advantages of queues over pipes (e.g., bidirectional communication, easier handling of multiple processes).
Provide examples of Producer/Consumer problems.

Semaphores:
Introduce semaphores as a fundamental synchronization primitive.
Explain the concept of a semaphore as a counter that controls access to shared resources.
Distinguish between binary semaphores (locks) and counting semaphores.
Demonstrate how to create and use semaphores in Python (using the multiprocessing.Semaphore module).
Show examples of how to use semaphores to control access to limited resources.

Barriers:
Introduce barriers as a synchronization mechanism for coordinating multiple processes.
Explain how barriers ensure that all processes reach a certain point before any can proceed.
Demonstrate how to create and use barriers in Python (using the multiprocessing.Barrier module).
Provide examples of scenarios where barriers are useful (e.g., parallel computations with dependencies).

Conditions:
Introduce multiprocessing.Condition for more complex synchronization scenarios.
Explain how conditions allow processes to wait for specific events or states.
Demonstrate how to use conditions to coordinate processes in producer-consumer or other complex scenarios.
Show the relationship between conditions and locks.


Advanced Semaphore Usage/Problems:
Discuss common problems that arise when using semaphores.
Deadlock revisited, with specific examples using semaphores.
Starvation.
Introduce more complex uses of counting semaphores.
Discuss solutions to common semaphore problems.

Process Management Recap/Discussion:
Review the concepts of process states, IPC, and synchronization.
Discuss the trade-offs between different IPC and synchronization mechanisms.
Discuss the performance implications of process creation and communication.
Discuss how the OS handles scheduling of multiple processes.

Practical Project Introduction/Discussion:
Introduce a practical project that utilizes the concepts covered in the previous weeks.
Discuss project requirements, design considerations, and implementation strategies.
Example project ideas:
A parallel data processing pipeline using pipes or queues.
A multi-process simulation using semaphores and barriers.
A project that uses shared memory, if that topic is in your scope later on.


Key Considerations:

Hands-on Exercises: Emphasize practical exercises to reinforce the concepts.
Visualizations: Use diagrams and visualizations to illustrate process states, IPC, and synchronization.
Real-World Examples: Connect the concepts to real-world applications and scenarios.
Error Handling: Discuss the importance of error handling in concurrent programs.
Debugging: Provide guidance on debugging concurrent programs, which can be challenging.
Multiprocessing Module Focus: because of the GIL, the multiprocessing module will be the primary tool used.

