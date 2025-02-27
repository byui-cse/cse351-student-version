# Lesson 1: Course Introduction, Review of Python, Threads

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
1.1 | [Course Overview](#Course-Overview)
1.2 | [What is Parallelism?](#What-is-Parallelism?)
1.3 | [Why Parallelism?](#Why-Parallelism?)
1.4 | [Basic Python Syntax and Data Structures](#Basic-Python-Syntax-and-Data-Structures)
1.5 | [Essential Libraries for Parallelism](#Essential-Libraries-for-Parallelism)
1.6 | [Python Memory Model](#Python-Memory-Model)
1.7 | [Introduction to Threads](#Introduction-to-Threads) :key:

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

### 1.1 Course Overview
Learning Objectives
Course Structure and Modules
Assessment Methods (Assignments, Exams, Projects)
Prerequisites (Data Structures, Algorithms, Basic Operating System Concepts)
Required Software and Tools (Python, C#, IDEs, etc.)
Intro to the computing resources used in the course.

### 1.2 What is Parallelism?
Definition of Parallelism vs. Concurrency
Flynn's Taxonomy (SISD, SIMD, MISD, MIMD)
Types of Parallelism: Data Parallelism, Task Parallelism, Pipeline Parallelism
Granularity of Parallelism (Coarse-grained, Fine-grained)

### 1.3 Why Parallelism?
Performance Benefits (Speedup, Throughput)
Amdahl's Law (Theoretical Speedup Limits)
Gustafson's Law (Scaled Speedup)
Real-world Applications (Scientific Computing, Machine Learning, Data Processing, Graphics, etc.)
The "Free Lunch is Over" - Why Multi-core is the Present and Future

### 1.4 Basic Python Syntax and Data Structures
Data Types (Integers, Floats, Strings, Booleans, Lists, Tuples, Dictionaries, Sets)
Control Flow (if-else, for, while loops)
Functions (Definition, Arguments, Return Values, Scope)
Classes and Objects (Object-Oriented Programming Basics)

### 1.5 Essential Libraries for Parallelism
threading Module (Overview)
multiprocessing Module (Overview)
time Module (for performance measurement)
Brief introduction to libraries like NumPy and SciPy (for data parallelism if relevant)

### 1.6 Python Memory Model
Global Interpreter Lock (GIL) - Crucial for understanding Python's limitations with true CPU-bound parallelism.
Implications for Threading vs. Multiprocessing

### 1.7 Introduction to Threads
What are Threads? (Lightweight Processes)
User-Level vs. Kernel-Level Threads
Thread Creation and Management (in Python's threading module)
Thread Lifecycle (States: New, Runnable, Running, Blocked, Terminated)
critical sections
locks













### Course Introduction

I'm creating an university course on computer science parallelism. 
Here are the main topics for the course.  Each topic will be given
2 weeks during the course. Please add sub-topics for each topic.  You
are free to add any missing topics that you feel should be taught.
Topics:
- Course Introduction, Review of Python, Threads
- Inter-Process Communication & Synchronization Primitives
- Python Processes, pools
- Operating System Features and Hardware
- Classic Concurrency Problems
- Review of C#, Threads, and Tasks 



Week 1: Foundations & Python Review

Review of Python:
Start with a refresher on core Python concepts. This ensures everyone is on the same page, especially if students have varying backgrounds. Focus on:
Data structures (lists, dictionaries, etc.)
Functions and modules
Basic object-oriented programming (if relevant)
Memory management basics.

I/O vs. CPU bound:
Introduce the fundamental distinction between these two types of tasks. This is crucial for understanding when and why parallelism is beneficial.
Explain how I/O-bound tasks spend most of their time waiting for external operations (disk, network), while CPU-bound tasks are limited by processing power.
Give examples of each type of task.

What is the GIL (Global Interpreter Lock):
Immediately follow with the GIL explanation. This sets the stage for the limitations of Python's threading model and why it's essential to understand.
Explain that the GIL prevents multiple native threads from executing Python bytecode at the same time.
Highlight the implications for CPU-bound tasks and how it affects true parallelism in Python.
Mention that the GIL has less of an impact on I/O bound tasks.

Threads:
Introduce the concept of threads as a way to achieve concurrency.
Explain how threads allow multiple sequences of instructions to run concurrently within a single process.
Demonstrate basic thread creation and execution in Python using the threading module.
Show examples of threads working with I/O bound tasks.

Critical Section:
Define the concept of a critical section and the potential for race conditions.
Explain how concurrent access to shared resources can lead to unexpected and incorrect results.
Illustrate race conditions with simple examples.

Lock:
Introduce locks as a mechanism for synchronizing access to critical sections.
Demonstrate how locks can prevent race conditions and ensure data integrity.
Show examples of using locks to protect shared resources in Python.
Discuss potential problems with locks, such as deadlocks.
Why this order?

Concurrency vs. Parallelism (More Explicitly):
While you mentioned it as a tip, consider making this a dedicated topic. It's a fundamental distinction that often confuses beginners.
Clearly define each term and provide examples to illustrate the difference.
Discuss how threads in Python primarily provide concurrency due to the GIL, and how other approaches are needed for true parallelism.

Thread Safety:
Expand on the concept of critical sections by explicitly discussing thread safety.
Define what it means for code to be thread-safe and why it's essential for concurrent programs.
Discuss common sources of thread safety issues (e.g., shared mutable state).

Deadlocks and Livelocks (Introduction):
While you mentioned deadlocks, consider providing a more detailed introduction to deadlocks and livelocks.
Explain the conditions that lead to deadlocks and livelocks.
Provide simple examples of how these problems can occur.
Even if you don't go into deep solutions, alerting students to these problems early is very helpful.

Race Conditions (More Examples):
Expand on race conditions with more diverse and illustrative examples.
Consider examples that involve different data structures or operations.
Demonstrate how subtle race conditions can be difficult to detect.

Context Switching:
Give a basic overview of context switching.
Explain how the operating system manages threads and switches between them.
This helps students understand the overhead associated with threads.

Atomic Operations (Introduction):
If you have time, a brief introduction to atomic operations can be useful.
Explain that some operations can be performed indivisibly, even in concurrent environments.
This can provide a glimpse into more advanced synchronization techniques.
