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
1.8 | [Critical Section](#Critical-Section)  :key:
1.9 | [Locks](#Locks)  :key:

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

## 1.1 Course Overview

### Learning Objectives

### Course Structure and Modules

### Assessment Methods (Assignments, Exams, Projects)

### Prerequisites (Data Structures, Algorithms, Basic Operating System Concepts)

### Required Software and Tools (Python, C#, IDEs, etc.)

### Intro to the computing resources used in the course.


## 1.2 What is Parallelism?
### Definition of Parallelism vs. Concurrency
Flynn's Taxonomy (SISD, SIMD, MISD, MIMD)
### Types of Parallelism: Data Parallelism, Task Parallelism, Pipeline Parallelism
### Granularity of Parallelism (Coarse-grained, Fine-grained)

## 1.3 Why Parallelism?
### Performance Benefits (Speedup, Throughput)
### Amdahl's Law (Theoretical Speedup Limits)
### Gustafson's Law (Scaled Speedup)
### Real-world Applications (Scientific Computing, Machine Learning, Data Processing, Graphics, etc.)
### The "Free Lunch is Over" - Why Multi-core is the Present and Future

## 1.4 Basic Python Syntax and Data Structures
### Data Types (Integers, Floats, Strings, Booleans, Lists, Tuples, Dictionaries, Sets)
### Control Flow (if-else, for, while loops)
### Functions (Definition, Arguments, Return Values, Scope)
### Classes and Objects (Object-Oriented Programming Basics)

## 1.5 Essential Libraries for Parallelism
### threading Module (Overview)
### multiprocessing Module (Overview)
### time Module (for performance measurement)
### Brief introduction to libraries like NumPy and SciPy (for data parallelism if relevant)

## 1.6 Python Memory Model
### Global Interpreter Lock (GIL) 
- Crucial for understanding Python's limitations with true CPU-bound parallelism.
### Implications for Threading vs. Multiprocessing
### I/O vs. CPU bound:
### Introduce the fundamental distinction between these two types of tasks. This is crucial for understanding when and why parallelism is beneficial.
### Explain how I/O-bound tasks spend most of their time waiting for external operations (disk, network), while CPU-bound tasks are limited by processing power.
### Give examples of each type of task.


## 1.7 Introduction to Threads
### What are Threads? (Lightweight Processes)
### User-Level vs. Kernel-Level Threads
### Thread Creation and Management (in Python's threading module)
### Thread Lifecycle (States: New, Runnable, Running, Blocked, Terminated)

## 1.8 Critical Section:
### Define the concept of a critical section and the potential for race conditions.
### Explain how concurrent access to shared resources can lead to unexpected and incorrect results.
### Illustrate race conditions with simple examples.

## 1.9 Locks
### Introduce locks as a mechanism for synchronizing access to critical sections.
### Demonstrate how locks can prevent race conditions and ensure data integrity.
### Show examples of using locks to protect shared resources in Python.
### Discuss potential problems with locks, such as deadlocks.
### Why this order?


