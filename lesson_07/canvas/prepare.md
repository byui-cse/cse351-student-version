# Lesson 7: Operating System Features and Hardware

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
7.1 | [Process and Thread Scheduling](#Process-and-Thread-Scheduling)
7.2 | [Memory Management](#Memory-Management)
7.3 | [Hardware Considerations](#Hardware-Considerations)



:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

7.1 Process and Thread Scheduling
Scheduling Algorithms (FIFO, Round Robin, Priority Scheduling, Multilevel Queues, etc.)
Context Switching
Preemptive vs. Non-Preemptive Multitasking

7.2 Memory Management
Virtual Memory
Paging and Segmentation
Memory Allocation (for Processes and Threads)

7.3 Hardware Considerations
Multi-core Processors (Architecture, Cache Coherence)
Hyperthreading (Simultaneous Multithreading - SMT)
NUMA (Non-Uniform Memory Access) Architectures
GPUs (Graphics Processing Units) and their Role in Parallelism (Brief Overview)
Clusters and Distributed Systems (Brief Overview)















Overall Module Goals:

- Understand the fundamental interactions between operating systems and hardware in the context of parallel programming.
- Gain insights into memory management, scheduling, and file systems.
- Learn about cache coherence, user/kernel threads, monitors, and mutexes.
- Explore the relationship between recursion and system resources.
- Reading Material Outline:
 
### Topic 1

### Topic 1

Day 1: Introduction to Operating Systems and Parallelism

Reading:
"Overview of Operating System Concepts":
Role of the OS in resource management.
Introduction to kernel and user space.
"OS Support for Parallelism":
How the OS facilitates parallel execution.
The relationship between hardware and OS parallelism.
Concepts:
Kernel vs. User mode.
Resource allocation.
Process management.
Day 2: Memory Management

Reading:
"Memory Hierarchy and Virtual Memory":
Understanding RAM, cache, and disk.
Paging and segmentation.
"Memory Allocation and Deallocation":
How the OS manages memory for processes.
Impact of memory access patterns on performance.
Concepts:
Memory locality.
Page faults.
Memory fragmentation.
Day 3: CPU Scheduling

Reading:
"Scheduling Algorithms":
First-Come, First-Served (FCFS), Shortest Job Next (SJN), Round Robin (RR).
Priority scheduling and real-time scheduling.
"Context Switching":
The overhead of switching between processes/threads.
Impact of scheduling on parallel performance.
Concepts:
Scheduling policies.
Preemption.
Scheduling overhead.
Day 4: File Systems

Reading:
"File System Architecture":
File organization and storage.
File system operations (read, write, seek).
"I/O Performance":
Impact of file system operations on parallel I/O.
Buffering and caching.
Concepts:
File system caching.
Disk I/O latency.
Parallel file access.
Day 5: User and Kernel Threads

Reading:
"User Threads vs. Kernel Threads":
Differences in implementation and management.
Advantages and disadvantages of each.
"Thread Scheduling":
How the OS schedules kernel threads.
User-level thread management.
Concepts:
Thread context.
Thread synchronization.
Many-to-one, one-to-one, and many-to-many threading models.
Week 2: Advanced Concepts and Synchronization

Day 6: Cache Coherence

Reading:
"Cache Coherence Protocols":
Understanding MESI (Modified, Exclusive, Shared, Invalid) protocol.
Maintaining data consistency in multi-core systems.
"False Sharing":
Performance impact of false sharing.
Strategies for minimizing false sharing.
Concepts:
Cache lines.
Memory barriers.
Multi-core architecture.


Day 7: Mutexes: Application and System Level

Reading:
"Mutex Implementation":
Application-level mutexes (e.g., threading.Lock).
System-level mutexes (kernel-provided).
"Mutex Overhead and Contention":
Performance impact of mutex usage.
Strategies for minimizing contention.
Concepts:
Mutual exclusion.
Locking mechanisms.
Deadlocks.


Day 8: Monitors

Reading:
"Monitors and Condition Variables":
Implementing synchronized access to shared data.
Using condition variables for signaling.
"Monitor Implementation in Python":
Using threading.Condition and threading.Lock.
Concepts:
Encapsulation of shared data.
Conditional synchronization.
Producer-consumer problem.


Day 9: Recursion and System Resources  ????????????????
- if used in a assignment, add the reading material in the assignment

Reading:
"Recursion and Stack Overflow":
Understanding the relationship between recursion depth and stack usage.
Tail recursion and optimization.
"Resource Consumption of Recursive Algorithms":
Memory and CPU usage of recursive functions.
Parallelizing recursive algorithms.
Concepts:
Stack frames.
Recursive depth.
Resource limitations.


Day 10: Review and Project Discussion

Reading:
Comprehensive review of all topics covered.
Discussion of how OS and hardware concepts relate to parallel programming projects.
Q&A session.
Concepts:
Integration of OS and hardware knowledge.
Practical implications for parallel application development.


Additional Notes:
Include diagrams and illustrations to explain complex concepts.
Provide practical examples and case studies.
Encourage students to experiment with OS and hardware settings (where safe).
Include example code that demonstrates mutexes, monitors, and threading.
Consider including small coding challenges that are effected by cache coherency, and have the students fix the code.
