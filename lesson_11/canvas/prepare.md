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


### Topic 1

### Topic 1

Overall Module Goals:

- Provide a solid foundation in C# syntax, object-oriented concepts, and concurrency.
- Introduce the Thread class and asynchronous programming with async/await.
- Explore concurrent collections and lambda functions in C#.
- Familiarize students with IDE shortcuts for efficient C# development.
- Reading Material Outline:

Day 1: C# Basics and Syntax Review

Reading:
- software requirements
    - Rider
    - DotNet 9.0
"C# Syntax and Data Types":
Variables, data types (primitive and reference), and operators.
Basic C# syntax and code structure.
"Control Flow in C#":
Conditional statements (if, switch).
Looping constructs (for, while, do-while).
Concepts:
C# language syntax.
Data type differences from Python.
Basic program structure.


Day 2: Object-Oriented Programming in C#

Reading:
"Classes and Objects":
Creating classes, defining members (fields, methods).
Object instantiation and usage.
"Inheritance, Polymorphism, and Encapsulation":
Understanding OOP principles in C#.
Abstract classes and interfaces.
Concepts:
Class design.
OOP paradigms.
Code reusability.


Day 3: UML Review and C# Integration

Reading:
"Review of UML Diagrams":
Class diagrams, sequence diagrams, and use case diagrams.
Mapping UML to C# code.
"Designing C# Classes with UML":
Translating UML diagrams into C# class structures.
Concepts:
UML modeling.
C# design patterns.
Software design principles.


Day 4: The Thread Class and Thread Methods

Reading:
"Introduction to the Thread Class":
Creating and starting threads in C#.
Understanding thread lifecycle.
"Methods of the Thread Class":
Start(), Join(), Sleep(), Abort(), etc.
Thread states and properties.
Thread creation and management.
Thread synchronization basics.
Thread safety.
Thread pools


Day 5: How Threads Work in C# (Sim Commands to Python)

Reading:
"C# Thread Execution Model":
Understanding how the CLR manages threads.
Comparing C# thread behavior to Python's threading and multiprocessing.
"Thread Synchronization Mechanisms":
Basic locking using lock keyword.
Understanding thread context switching.
Concepts:
CLR thread management.
Synchronization primitives.
Thread scheduling.
Week 2: Advanced C# Concurrency and Development

Day 6: Asynchronous Programming with async and await
Reading:
"Introduction to async and await":
Writing asynchronous methods.
Handling asynchronous operations.
"Task-Based Asynchronous Pattern (TAP)":
Understanding Task and Task<T> classes.
Performing asynchronous I/O operations.
Concepts:
Asynchronous programming model.
Non-blocking operations.
Task parallelism.

11.5 Comparing C# and Python Parallelism
GIL vs. no-GIL.
Performance Implications
Ease of Use
Different Paradigms (e.g., async/await in C#)



Day 3: The Task Class
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



Day 7: Concurrent Collections

Reading:
"Introduction to Concurrent Collections":
ConcurrentBag<T>, ConcurrentDictionary<TKey, TValue>, ConcurrentQueue<T>.
Thread-safe data structures.
"Using Concurrent Collections in Multi-threaded Applications":
Efficient data sharing and manipulation.
Avoiding race conditions.
Concepts:
Thread-safe data structures.
Concurrent access patterns.
Data consistency.


Day 8: Lambda Functions and Delegates

Reading:
"Lambda Expressions in C#":
Writing anonymous functions.
Using lambda expressions with delegates.
"Delegates and Events":
Understanding function pointers and event handling.
Using lambda expressions with events.
Concepts:
Functional programming in C#.
Event-driven programming.
Code conciseness.


Day 9: IDE Shortcuts and Efficient Development

Reading:
"IDE Shortcuts for C# Development":
Creating classes, methods, and properties quickly.
Code refactoring and navigation shortcuts.
"Debugging and Testing in the IDE":
Setting breakpoints and inspecting variables.
Unit testing with built-in tools.
Concepts:
Productivity tools.
Efficient coding practices.
Debugging techniques.


Day 10: Review and Project Introduction

Reading:
Comprehensive review of all topics covered.
Introduction to the C# concurrency project.
Q&A session.
Concepts:
Application of learned concepts.
Project planning and execution.






















































































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

