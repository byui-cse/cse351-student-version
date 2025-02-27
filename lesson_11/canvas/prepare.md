# Lesson 11: Review of C#, C# Threads, and Tasks 

TODO - place all C# readin material in this week.  This will
be the last reading material for the course.  Students will be 
working on assignments for the rest of the course.  Maybe 2 assignments.
1) basic threads
2) advanced assignment

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
11.1 | [C# Language Basics](#C#-Language-Basics)
11.2 | [Threading in C#](#Threading-in-C#)
11.3 | [The Task Parallel Library](#The-Task-Parallel-Library)
11.4 | [Thread Pools in C#](#Thread-Pools-in-C#)
11.5 | [Comparing C# and Python Parallelism](#Comparing-C#-and-Python-Parallelism)

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.


11.1 C# Language Basics
UML Diagrams
Data Types, Control Flow, Classes, Objects
Relevant C# Features 
Delegates, 
Events

11.2 Threading in C#
System.Threading.Thread Class
Thread Creation and Management
Thread Synchronization (Locks, Monitors, Mutexes, Semaphores, etc.)
[ThreadStatic] Attribute

11.3 The Task Parallel Library
System.Threading.Tasks.Task
Task.Run, Task.Factory.StartNew
async and await Keywords (Asynchronous Programming)
How async/await relates to Tasks (Important distinction)
Task Continuations (ContinueWith)
Task Cancellation
Data Parallelism with Parallel.For and Parallel.ForEach

11.4 Thread Pools in C#
ThreadPool Class
Managing Tasks with the Thread Pool

11.5 Comparing C# and Python Parallelism
GIL vs. no-GIL.
Performance Implications
Ease of Use
Different Paradigms (e.g., async/await in C#)



























### Topic 1

### Topic 1

Overall Module Goals:

- Gain a deep understanding of the Task Parallel Library (TPL) in C#.
- Learn to effectively use Task, TaskFactory, and task continuations.
- Master advanced synchronization techniques with ReaderWriterLock and slim versions of synchronization primitives.
- Understand blocking mechanisms and their implications in concurrent applications.

TODO: The course expects students to use online documentation to understand the following in C#:
    - locks, semaphores, barriers, queues
    - Inter-Process Communication & Synchronization Primitives

Thgese concepts are the same in Python as in C#, just different syntacs.


Reading Material Outline:


Day 1: Introduction to the Task Parallel Library (TPL)

Reading:
"Overview of the TPL":
Motivation for the TPL and its benefits.
Namespaces: System.Threading.Tasks.
"Benefits of Using Tasks":
Abstraction of thread management.
Scalability and responsiveness.
Concepts:
Task-based parallelism.
Thread pool usage.
TPL architecture.


Day 2: .NET Framework and Common Libraries

Reading:
".NET Framework Overview":
Understanding the CLR, BCL, and framework components.
Namespaces relevant to concurrency.
"Common Libraries for Concurrency":
System.Threading, System.Collections.Concurrent.
Overview of relevant classes and interfaces.
Concepts:
.NET runtime environment.
Framework libraries.
Dependency management.


Day 3: The Task Class

Reading:
"Creating and Starting Tasks":
Using Task.Run(), Task.Factory.StartNew().
Task states and properties.
"Working with Task<TResult>":
Returning values from tasks.
Handling exceptions in tasks.
Concepts:
Task lifecycle.
Asynchronous operations with tasks.
Result handling.


Day 4: TaskFactory

Reading:
"Using TaskFactory for Advanced Task Creation":
Configuring task creation options.
Specifying task schedulers.
"Creating Child Tasks":
Parent-child task relationships.
Task hierarchies.
Concepts:
Task creation customization.
Task scheduling.
Task relationships.


Day 5: Task Continuation

Reading:
"Chaining Tasks with ContinueWith()":
Executing tasks sequentially.
Handling task completion and faults.
"Continuation Options":
Specifying continuation conditions.
Configuring continuation behavior.
Concepts:
Task dependencies.
Asynchronous workflows.
Error handling.
Week 2: Advanced Synchronization and Blocking



Day 6: Blocking Mechanisms: Sleep(), Join(), Task.Wait()

Reading:
"Thread Blocking with Thread.Sleep()":
Pausing thread execution.
Use cases and limitations.
"Thread Synchronization with Thread.Join()":
Waiting for thread completion.
Blocking the calling thread.
"Task Blocking with Task.Wait()":
Waiting for task completion.
Handling timeouts.
Concepts:
Thread and task blocking.
Synchronization vs. blocking.
Performance implications.


Day 7: ReaderWriterLock Class

Reading:
"Introduction to ReaderWriterLock":
Allowing multiple readers and exclusive writers.
Implementing read-write locks.
"Using ReaderWriterLock for Shared Resources":
Optimizing access to shared data.
Avoiding writer starvation.
Concepts:
Read-write synchronization.
Shared resource management.
Lock contention.


Day 8: Slim Versions of Semaphore and ReaderWriterLock

Reading:
"Introduction to SemaphoreSlim":
Lightweight semaphore implementation.
Asynchronous semaphore operations.
"Introduction to ReaderWriterLockSlim":
Optimized read-write lock.
Recursive lock acquisition.
Concepts:
Lightweight synchronization primitives.
Asynchronous synchronization.
Performance optimization.


Day 9: Advanced Synchronization Patterns and Best Practices

Reading:
"Implementing Advanced Synchronization Patterns":
Using CountdownEvent, Barrier, ManualResetEventSlim.
Building complex concurrent applications.
"Best Practices for Concurrent Programming":
Avoiding deadlocks and race conditions.
Optimizing performance and scalability.
Concepts:
Advanced synchronization primitives.
Concurrent design patterns.
Performance tuning.


Day 10: Review and Project Discussion

Reading:
Comprehensive review of all topics covered.
Discussion of advanced concurrency project requirements.
Q&A session.
Concepts:
Application of advanced concurrency concepts.
Project planning and implementation.5


Additional Notes:
- Provide detailed coding examples and exercises for each topic.
- Emphasize the performance implications of different synchronization techniques.
- Encourage students to experiment with different TPL patterns and synchronization primitives.
- Include practical examples of how to use these concepts in real-world applications.
- Consider a project that implements a complex concurrent application using the TPL and advanced synchronization techniques.



Overall Module Goals:

Gain a deep understanding of the Task Parallel Library (TPL) in C#.
Learn to effectively use Task, TaskFactory, and task continuations.
Master advanced synchronization techniques with ReaderWriterLock and slim versions of synchronization primitives.
Understand blocking mechanisms and their implications in concurrent applications.
Reading Material Outline:

Week 1: Task Parallel Library and Basic Concurrency



Day 1: Introduction to the Task Parallel Library (TPL)

Reading:
"Overview of the TPL":
Motivation for the TPL and its benefits.
Namespaces: System.Threading.Tasks.
"Benefits of Using Tasks":
Abstraction of thread management.
Scalability and responsiveness.
Concepts:
Task-based parallelism.
Thread pool usage.
TPL architecture.


Day 2: .NET Framework and Common Libraries

Reading:
".NET Framework Overview":
Understanding the CLR, BCL, and framework components.
Namespaces relevant to concurrency.
"Common Libraries for Concurrency":
System.Threading, System.Collections.Concurrent.
Overview of relevant classes and interfaces.
Concepts:
.NET runtime environment.
Framework libraries.
Dependency management.


Day 3: The Task Class

Reading:
"Creating and Starting Tasks":
Using Task.Run(), Task.Factory.StartNew().
Task states and properties.
"Working with Task<TResult>":
Returning values from tasks.
Handling exceptions in tasks.
Concepts:
Task lifecycle.
Asynchronous operations with tasks.
Result handling.


Day 4: TaskFactory

Reading:
"Using TaskFactory for Advanced Task Creation":
Configuring task creation options.
Specifying task schedulers.
"Creating Child Tasks":
Parent-child task relationships.
Task hierarchies.
Concepts:
Task creation customization.
Task scheduling.
Task relationships.


Day 5: Task Continuation

Reading:
"Chaining Tasks with ContinueWith()":
Executing tasks sequentially.
Handling task completion and faults.
"Continuation Options":
Specifying continuation conditions.
Configuring continuation behavior.
Concepts:
Task dependencies.
Asynchronous workflows.
Error handling.
Week 2: Advanced Synchronization and Blocking



Day 6: Blocking Mechanisms: Sleep(), Join(), Task.Wait()

Reading:
"Thread Blocking with Thread.Sleep()":
Pausing thread execution.
Use cases and limitations.
"Thread Synchronization with Thread.Join()":
Waiting for thread completion.
Blocking the calling thread.
"Task Blocking with Task.Wait()":
Waiting for task completion.
Handling timeouts.
Concepts:
Thread and task blocking.
Synchronization vs. blocking.
Performance implications.


Day 7: ReaderWriterLock Class

Reading:
"Introduction to ReaderWriterLock":
Allowing multiple readers and exclusive writers.
Implementing read-write locks.
"Using ReaderWriterLock for Shared Resources":
Optimizing access to shared data.
Avoiding writer starvation.
Concepts:
Read-write synchronization.
Shared resource management.
Lock contention.


Day 8: Slim Versions of Semaphore and ReaderWriterLock

Reading:
"Introduction to SemaphoreSlim":
Lightweight semaphore implementation.
Asynchronous semaphore operations.
"Introduction to ReaderWriterLockSlim":
Optimized read-write lock.
Recursive lock acquisition.
Concepts:
Lightweight synchronization primitives.
Asynchronous synchronization.
Performance optimization.


Day 9: Advanced Synchronization Patterns and Best Practices

Reading:
"Implementing Advanced Synchronization Patterns":
Using CountdownEvent, Barrier, ManualResetEventSlim.
Building complex concurrent applications.
"Best Practices for Concurrent Programming":
Avoiding deadlocks and race conditions.
Optimizing performance and scalability.
Concepts:
Advanced synchronization primitives.
Concurrent design patterns.
Performance tuning.


Day 10: Review and Project Discussion

Reading:
Comprehensive review of all topics covered.
Discussion of advanced concurrency project requirements.
Q&A session.
Concepts:
Application of advanced concurrency concepts.
Project planning and implementation.5


Additional Notes:
- Provide detailed coding examples and exercises for each topic.
- Emphasize the performance implications of different synchronization techniques.
- Encourage students to experiment with different TPL patterns and synchronization primitives.
- Include practical examples of how to use these concepts in real-world applications.
- Consider a project that implements a complex concurrent application using the TPL and advanced synchronization techniques.

