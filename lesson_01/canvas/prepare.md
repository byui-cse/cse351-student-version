# Lesson 1: Course Introduction, Review of Python, Threads

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
1.1 | [Course Overview](#Course-Overview)
1.2 | [What is Parallelism?](#What-is-Parallelism?)
1.3 | [Why Parallelism?](#Why-Parallelism?)
1.4 | [Python Memory Model](#Python-Memory-Model)
1.5 | [Introduction to Threads](#Introduction-to-Threads) :key:
1.6 | [Critical Section](#Critical-Section)  :key:
1.7 | [Locks](#Locks)  :key:

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.




# 1.1 Course Overview

## Learning Objectives

Successful graduates for CSE 351 will:

1. List and explain the main concepts of parallelism and concurrency.
2. Enhance code to take advantage of multiple functional units.
3. Design threaded code that takes advantage of multicore processors.
4. Use a variety of higher-level parallelization tools.

## Course Structure and Modules

The course is divided into 2 week blocks.  For each block, students will be required to read the topic material with an assignment.

## Assessment Methods (Assignments, Exams, Projects)

See syllabus.

## Required Software and Tools (Python, C#, IDEs, etc.)

We will be using Python 3 in this course.  We highly requirement that you install the latest version of Python from [python.org](https://www.python.org).  This is version 3.13.x. 

If any of the concepts or topics in the list below seem unfamiliar to you, `it is your responsibility to review these topics`. The basic data structures used in this course are: 
- Lists
- Dictionaries
- Python Classes (OOP)


## Python Topics with Videos

- [Introducing Python](https://www.youtube.com/watch?v=7XOhibxgBlQ&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=2)
- [Getting Started](https://www.youtube.com/watch?v=CXZYvNRIAKM&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=3)
- [Configuring VS Code](https://www.youtube.com/watch?v=EU8eayHWoZg&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=4)
- [Input and print functions](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=5)
- [Demo of print function](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=6)
- [Comments](https://www.youtube.com/watch?v=kEuVvUc1Zec&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=7)
- [String data type](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=9)
- [Numeric data types](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=13)
- [Date data types](https://www.youtube.com/watch?v=o1dlxoHxdHU&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=15)
- [Collections](https://www.youtube.com/watch?v=beA8IsY3mQs&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=25)
- [Loops](https://www.youtube.com/watch?v=LrOAl8vUFHY&[list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=27)
- [Python dictionaries: realpython](https://realpython.com/lessons/dictionary-python/)
- [Python slicing](https://www.youtube.com/watch?v=ajrtAuDg3yw)
- [List Comprehensions](https://www.w3schools.com/python/python_lists_comprehension.asp)

## Links to Python Articles

- [Python.org](https://www.python.org/)
- [Python lists](https://www.w3schools.com/python/python_lists.asp)
- [Lists and Tuples in Python](https://realpython.com/courses/lists-tuples-python/)
- [Python Dictionaries: w3 school](https://www.w3schools.com/python/python_dictionaries.asp) 
- [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- [To learn more about installing modules using the **pip** command](https://docs.python.org/3/installing/index.html#basic-usage)

## C# Language Requirements

The last part of the course will be in C# where reading materials and assignments will be in that language.  Please review C# and OOP if required.  We will be using JetBrains Rider IDE.

## UML Class Diagrams

UML class diagrams were introduced in CSE 210.  Please review these diagrams.

[Video on UML Class Diagrams](https://www.youtube.com/watch?v=6XrL5jXmTwM)















# 1.2 What is Parallelism?

This section introduces the core concept of parallelism in computing, contrasting it with concurrency, classifying different types of parallel architectures, and exploring various forms and granularities of parallel execution.

## Definition of Parallelism vs. Concurrency

**Concurrency** and **parallelism** are related but distinct concepts. Understanding the difference is crucial for designing and analyzing parallel systems.

**Concurrency:** A property of a system in which multiple tasks *can be in progress* at the same time. This *doesn't* necessarily mean they are executing simultaneously. It means that tasks can start, run, and complete in overlapping time periods.  Think of a single chef juggling multiple dishes – they might be working on the sauce for one dish, then chopping vegetables for another, then checking the oven for a third, all seemingly "at the same time."  They are making progress on multiple tasks, but only one task is actively being worked on at any given instant. 

**Parallelism:** A property of a system where multiple tasks, or parts of a task, *literally execute at the same time*. This requires multiple processing units (e.g., multiple CPU cores, multiple processors, multiple machines).  Imagine multiple chefs, each with their own set of ingredients and tools, working on different dishes simultaneously. 

**Key Differences Summarized:**

- Concurrency is about *dealing* with lots of things at once.
- Parallelism is about *doing* lots of things at once.

| Feature          | Concurrency                                 | Parallelism                                    |
| ---------------- | ------------------------------------------- | ---------------------------------------------- |
| Execution        | Overlapping time periods, potentially sequential | Simultaneous execution                           |
| Hardware         | Can occur on a single processor             | Requires multiple processing units               |
| Primary Goal     | Improve responsiveness, manage multiple tasks | Improve performance (speedup, throughput)      |
| Analogy          | Single chef juggling multiple dishes         | Multiple chefs working on different dishes     |

**Relationship:** Parallelism is a *form* of concurrency, but not all concurrency is parallel. A system can be concurrent without being parallel (e.g., a single-core processor using time-slicing). A parallel system is inherently concurrent.


## Types of Parallelism: Data Parallelism, Task Parallelism, Pipeline Parallelism

These describe different approaches to breaking down a computational problem into smaller parts that can be executed concurrently:

1. **Data Parallelism:** The same operation is performed on different subsets of the data concurrently.  This is often associated with SIMD architectures but can also be implemented on MIMD systems.

    **Example:** Processing a large image by dividing it into smaller blocks and applying the same filter to each block simultaneously. Another example would be calculating the sum of a large array by dividing it into chunks and having each processor sum a chunk.

1. **Task Parallelism:** Different tasks (or functions) are executed concurrently. These tasks may operate on the same or different data. This is typically associated with MIMD architectures.

    **Example:** A web server handling multiple client requests simultaneously. Each request is a separate task, handled by a different thread or process.  Another example would be a compiler, where lexical analysis, parsing, and code generation could be performed concurrently on different parts of the source code.

1. **Pipeline Parallelism:** A task is broken down into a sequence of stages, and different stages are executed concurrently on different data items.  This is like an assembly line, where each stage performs a specific operation, and multiple items are processed in an overlapping fashion.

    **Example:**  Instruction pipelining in a CPU, where the fetch, decode, execute, memory access, and write-back stages of instruction processing are performed concurrently on different instructions.  Another example could be a video processing pipeline, where different frames are undergoing different stages of processing (e.g., decoding, color correction, encoding) simultaneously.


## Granularity of Parallelism (Coarse-grained, Fine-grained)

Granularity refers to the size of the computational units that are executed concurrently.  It's a measure of the ratio of computation to communication/synchronization overhead.

**Coarse-grained Parallelism:** 

Large tasks are executed concurrently, with relatively infrequent communication or synchronization between them. The amount of computation performed by each task is significantly larger than the overhead of communication.

## Characteristics
-   Lower communication overhead.
-   Easier to implement.
-   Less potential for speedup (limited by the number of large tasks).
-   Suitable for loosely coupled systems (e.g., distributed computing).

**Example:**  Distributing the simulation of different physical systems to different nodes in a cluster. Each node performs a large amount of independent computation.

## Fine-grained Parallelism
Small tasks are executed concurrently, with frequent communication and synchronization. The amount of computation performed by each task is small, and the overhead of communication can be significant.

**Characteristics:**
-   Higher communication overhead.
-   More complex to implement.
-   Greater potential for speedup (can exploit a higher degree of parallelism).
-   Suitable for tightly coupled systems (e.g., multi-core processors, GPUs).

**Example:**  Parallelizing the individual iterations of a loop within a program, where each iteration performs a small amount of work.  GPU computations often exhibit fine-grained parallelism.

## Relationship between Granularity and Parallelism Type

- Data parallelism often lends itself to fine-grained parallelism (e.g., operating on individual pixels in an image).
- Task parallelism can be either coarse-grained (e.g., running different applications on different cores) or fine-grained (e.g., breaking down a complex algorithm into many small, interdependent tasks).
- Pipeline parallelism is generally considered fine-grained, as the stages of the pipeline are typically small and data flows between them rapidly.

Choosing the appropriate granularity is a key design decision in parallel programming.  It depends on the characteristics of the problem, the hardware architecture, and the desired balance between speedup and overhead.














# 1.3 Why Parallelism?

## Performance Benefits (Speedup, Throughput)

Parallelism offers two primary performance benefits: **speedup** and **throughput**.

### Speedup

This measures how much faster a parallel program is compared to its sequential counterpart.  It's defined as the ratio of the execution time of the sequential program (T<sub>s</sub>) to the execution time of the parallel program (T<sub>p</sub>) on *p* processors:

Speedup (S<sub>p</sub>) = T<sub>s</sub> / T<sub>p</sub>

Ideally, we want linear speedup, where S<sub>p</sub> = *p*.  In practice, this is rarely achievable due to overheads like communication, synchronization, and the inherently sequential parts of the program.  A speedup less than *p* is called *sublinear speedup*.  In some rare cases, *superlinear speedup* (S<sub>p</sub> > *p*) can be observed due to factors like improved cache utilization in parallel execution.

### Throughput

This measures the amount of work completed per unit of time.  In parallel systems, higher throughput means that more tasks can be processed in a given time period. For example, a web server handling multiple requests concurrently has higher throughput than a server handling requests one at a time.  Throughput is often more relevant for systems that handle many independent tasks (e.g., transaction processing, web servers) rather than for speeding up a single, large task.

## Amdahl's Law (Theoretical Speedup Limits)

Amdahl's Law, formulated by Gene Amdahl in 1967, provides a theoretical upper bound on the speedup achievable by parallelizing a program. It highlights the impact of the *inherently sequential portion* of a program.

Amdahl's Law states that the maximum speedup (S<sub>p</sub>) is:

![](./assets/formula.png)

**where**

- S<sub>latency</sub> is the theoretical speedup of the execution of the whole task.
- `s` is the speedup of the part of the task that benefits from improved system resources.
- `p` is the proportion of execution time that the part benefiting from improved resources originally occupied.

Followings are implications of Amdahl's law:

1. **Diminishing Returns:** Adding more processors gives diminishing returns. Beyond a certain point, adding more processors doesn't significantly increase speedup.
1. **Limited Speedup:** Even with many processors, there's a limit to how much faster a task can be completed due to parts of the task that cannot be parallelized.

### Example 1

Amdahl's law is often used in parallel computing to predict the theoretical speedup when using multiple processors. For example, if a program needs 20 hours to complete using a single thread, but a one-hour portion of the program cannot be parallelized, therefore only the remaining 19 hours (p = 0.95) of execution time can be parallelized, then regardless of how many threads are devoted to a parallelized execution of this program, the minimum execution time cannot be less than one hour. Hence, the theoretical speedup is limited to at most 20 times the single thread performance,

![](./assets/AmdahlsLaw.svg)

The theoretical speedup of the latency of the execution of a program as a function of the number of processors executing it, according to Amdahl's law. The speedup is limited by the serial part of the program. For example, if 95% of the program can be parallelized, the theoretical maximum speedup using parallel computing would be 20 times.

### Example 2

![](./assets/example.png)


## Real-world Applications

Parallelism is ubiquitous in modern computing, enabling applications that would be impossible to run on a single processor in a reasonable amount of time. Here are some key areas:

*   **Scientific Computing:** Simulating complex physical systems (weather forecasting, climate modeling, molecular dynamics, astrophysics, computational fluid dynamics). These simulations often involve solving large systems of equations or processing vast amounts of data.
*   **Machine Learning:** Training large machine learning models (deep neural networks) requires massive computational power.  Parallelism is used to distribute the training process across multiple GPUs or CPUs, significantly reducing training time. Data parallelism is heavily used in training, while model parallelism is also used for very large models.
*   **Data Processing:**  Analyzing large datasets ("big data") requires parallel processing techniques. Frameworks like Apache Hadoop and Spark use distributed computing to process data across clusters of machines.
*   **Graphics and Gaming:** Rendering realistic 3D graphics requires enormous computational power. GPUs, with their highly parallel architecture, are essential for modern gaming and computer-aided design (CAD).
*   **Databases:**  Database management systems (DBMS) use parallelism to handle concurrent queries, process large transactions, and perform data warehousing operations.
*   **Web Servers:**  Web servers use parallelism to handle thousands or millions of concurrent user requests.  Each request can be handled by a separate thread or process.
*   **Financial Modeling:**  Simulating financial markets, pricing derivatives, and managing risk often involve computationally intensive Monte Carlo simulations, which can be parallelized.
*   **Bioinformatics:**  Analyzing genomic data, protein folding, and drug discovery require significant computational resources, often leveraging parallel computing techniques.

## The "Free Lunch is Over" - Why Multi-core is the Present and Future

For decades, software developers enjoyed a "free lunch" from [Moore's Law](https://en.wikipedia.org/wiki/Moore%27s_law).  The exponential increase in transistor density and clock speeds meant that software automatically ran faster on newer processors without any code changes.  However, around the mid-2000s, this trend hit physical limits (power consumption, heat dissipation).

**The "Free Lunch is Over"** refers to the end of this era of automatic performance gains.  Instead of increasing clock speeds further, processor manufacturers shifted to **multi-core architectures**, placing multiple processing cores on a single chip.

**Why Multi-core is the Present and Future:**

- **Physical Limits of Clock Speed:**  Increasing clock speed significantly increases power consumption and heat generation.  We've reached a point where further increases are impractical and unsustainable.
- **Power Efficiency:**  Multi-core processors can provide increased performance at lower power consumption compared to a single, high-clock-speed core.
- **Parallelism is the Key to Performance:** To continue improving performance, software *must* be designed to take advantage of multiple cores.  This means embracing parallel programming techniques.
- **Ubiquitous Multi-core:**  Multi-core processors are now standard in everything from smartphones and laptops to servers and supercomputers.
- **Software Must Adapt:**  Software developers can no longer rely on hardware to automatically speed up their applications.  They must explicitly write parallel code to utilize the available cores.

















# 1.4 Python Memory Model

## Global Interpreter Lock (GIL)

The Global Interpreter Lock (GIL) is a mechanism used in CPython (the standard and most widely used implementation of Python) that allows only *one native thread* to hold control of the Python interpreter at any given time. This means that even on a multi-core processor, only one thread can be executing Python at a time.

The GIL effectively prevents true parallelism for CPU-bound tasks when using the `threading` module in CPython. While you can create multiple threads, they won't truly run in parallel on multiple cores; they'll be time-sliced on a single core, with the GIL switching between them.

**Why does the GIL exist?**

- **Simplified Memory Management:** The GIL simplifies CPython's internal memory management (specifically, reference counting for garbage collection).  It makes it easier to integrate with C extensions that are not thread-safe.  Without the GIL, complex locking mechanisms would be needed throughout the interpreter, potentially slowing down single-threaded programs.
- **Historical Reasons:** The GIL was introduced early in Python's development when multi-core processors were not prevalent.  Removing it now is a complex undertaking due to the extensive reliance on the GIL within CPython and its extensions.

**Consequences of the GIL:**

- **Limited CPU-Bound Parallelism:**  For CPU-bound tasks (tasks that spend most of their time performing computations), using multiple threads in CPython will *not* result in true parallelism.  The threads will contend for the GIL, and the overall performance may even be *worse* than a single-threaded implementation due to the overhead of thread switching.
- **I/O-Bound Parallelism Still Possible:** The GIL is *released* during I/O operations (e.g., reading from a file, network socket).  This means that for I/O-bound tasks, threads can still provide concurrency and improve responsiveness, as one thread can perform I/O while another thread holds the GIL and executes Python code.

## Implications for Threading vs. Multiprocessing

The GIL has a profound impact on the choice between using the two main packages for parallel programming: `threading` and `multiprocessing`.

### threading

*   **Suitable for I/O-bound tasks:** Threads are useful for tasks that spend a significant amount of time waiting for external operations.  Because the GIL is released during I/O, multiple threads can run concurrently, improving responsiveness.
*   **Limited by the GIL for CPU-bound tasks:**  Threads will *not* provide true parallelism for CPU-bound tasks due to the GIL.
*   **Lower Overhead:** Creating and managing threads is generally less resource-intensive than creating and managing processes.
*   **Shared Memory:** Threads share the same memory space, making communication relatively easy (but requiring careful synchronization to avoid race conditions).

### multiprocessing

*   **Suitable for CPU-bound tasks:**  Processes bypass the GIL limitation because each process has its own independent interpreter and memory space. This allows for true parallelism on multi-core CPUs.
*   **Also works for I/O-bound tasks:** Processes can also be used for I/O-bound tasks, although the overhead is generally higher than using threads.
*   **Higher Overhead:** Creating and managing processes is more resource-intensive than creating and managing threads.
*   **Inter-Process Communication (IPC):** Processes have separate memory spaces, so communication requires explicit IPC mechanisms (e.g., Queues, Pipes, shared memory).

### In Summary

*   Use `threading` for I/O-bound tasks where concurrency and responsiveness are important.
*   Use `multiprocessing` for CPU-bound tasks where true parallelism is needed to improve performance.

## I/O vs. CPU bound

Tasks in computer programs, written in any programming language, can be broadly categorized as either **I/O-bound** or **CPU-bound**. This distinction is fundamental to understanding when and how parallelism can improve performance.

### I/O-bound Tasks 

These tasks spend most of their time waiting for *Input/Output (I/O)* operations to complete. I/O operations involve interacting with external resources, such as:
- **Disk I/O:** Reading from or writing to a hard drive or SSD.
- **Network I/O:** Sending or receiving data over a network (e.g., making HTTP requests, downloading files).
- **User Input:** Waiting for input from a keyboard, mouse, or other input device.

During I/O operations, the CPU is often idle, waiting for the external device to respond. The speed of I/O-bound tasks is primarily limited by the speed of the external devices and the network, *not* by the CPU's processing power.

#### Examples of I/O-bound Tasks

1.  **Downloading a file from the internet:** The program spends most of its time waiting for data to arrive over the network.
2.  **Reading a large file from disk:** The program waits for the hard drive or SSD to read the data.
3.  **Making a request to a web server:**  The program sends a request and waits for the server to respond.
4.  **Waiting for user input:**  A program that prompts the user for input and waits for them to type something.
5.  **Database queries (often):**  Many database operations involve reading data from disk or waiting for results from a remote database server.

### CPU-bound Tasks

These tasks spend most of their time performing computations. They are limited by the speed of the CPU (and, to a lesser extent, memory access speed).  For CPU-bound tasks, a faster CPU (or more CPU cores) will directly lead to faster execution.

#### Examples of CPU-bound Tasks

1.  **Calculating the Mandelbrot set:** This involves performing many complex number calculations.
2.  **Resizing a large image:** Applying image processing algorithms to a large image requires significant CPU power.
3.  **Compressing a video file:**  Video encoding is a computationally intensive process.
4.  **Training a neural network:**  The training process involves many matrix multiplications and other mathematical operations.
5.   **Running a physics simulation:** Simulating the behavior of physical systems often requires solving complex equations.

Understanding whether a task is I/O-bound or CPU-bound is essential for choosing the right approach to parallelism.  I/O-bound tasks benefit from concurrency (e.g., using threads or asynchronous programming), while CPU-bound tasks benefit from true parallelism (e.g., using multiple processes). The GIL in Python significantly affects how CPU-bound tasks can be parallelized.














# 1.5 Introduction to Threads

## What are Python Threads?

In Python, a thread is a concurrent unit of execution *within a single process*. Threads are often called "lightweight processes" because they share the same memory space and resources (e.g., file handles, global variables) of the parent process, making them more efficient to create and manage than separate processes.  In the previous Python program that you wrote, there was always one thread running in your program. This is called the `main thread`.

> In computer science, a thread of execution is the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is typically a part of the operating system. The implementation of threads and processes differs between operating systems, but in most cases a thread is a component of a process. Multiple threads can exist within one process, executing concurrently and sharing resources such as memory, while different processes do not share these resources. In particular, the threads of a process share its executable code and the values of its dynamically allocated variables and non-thread-local global variables at any given time.
>
>[Quote Source](https://en.wikipedia.org/wiki/Thread_(computing))

## Key Characteristics of Threads

- **Shared Memory:** Threads within the same process share the same memory space. This makes communication between threads relatively easy (they can directly access and modify the same data), but it also introduces the risk of race conditions and data corruption if access to shared resources is not carefully synchronized.
- **Lightweight:** Threads are generally more lightweight than processes. Creating and switching between threads typically has lower overhead than creating and switching between processes.
- **Concurrency, Not True Parallelism (in CPython):**  Due to the Global Interpreter Lock (GIL) in CPython, threads cannot achieve true parallelism for CPU-bound tasks.  However, they can still provide concurrency for I/O-bound tasks, allowing a program to remain responsive while waiting for external operations.
- **Pre-emptive multitasking.** The operating system can interupt a thread at any time to let another thread run.

## User-Level vs. Kernel-Level Threads

There are two fundamental models for implementing threads: user-level threads and kernel-level threads. Python's `threading` module, in most common implementations (including CPython), utilizes a combination of approaches, often leveraging kernel-level threads under the hood but presenting a user-level API.

### User-Level Threads

*   **Managed by a user-space library:** Thread creation, scheduling, and management are all handled by a library within the user process, *without* direct involvement of the operating system kernel.
*   **Fast Context Switching:** Switching between user-level threads is typically very fast because it doesn't require a system call (a transition to kernel mode).
*   **Blocking System Calls are Problematic:** If one user-level thread makes a blocking system call (e.g., reading from a file), the *entire process* blocks, including all other threads within that process. This is because the kernel is unaware of the individual threads; it only sees the process as a whole.
*   **Cannot Utilize Multiple Cores:** User-level threads, on their own, cannot take advantage of multiple CPU cores because the kernel only schedules the process, not the individual threads within it.
* **Example:** Early implementations of threading libraries often used this approach.

### Kernel-Level Threads

*   **Managed by the OS Kernel:** The operating system kernel is directly aware of and manages the threads. Thread creation, scheduling, and synchronization are handled by the kernel.
*   **Blocking System Calls Do Not Block Other Threads:** If one kernel-level thread makes a blocking system call, the kernel can schedule another thread from the same process (or a different process) to run. This is a major advantage.
*   **Can Utilize Multiple Cores:** The kernel's scheduler can assign different threads to different CPU cores, enabling true parallelism.
*   **Slower Context Switching:** Switching between kernel-level threads is generally slower than switching between user-level threads because it requires a system call.
* **Example:** Most modern operating systems (Windows, Linux, macOS) provide kernel-level thread support.

### Hybrid Approaches

* **Many-to-one:** Many user threads map to a single kernel thread (suffers from the blocking problem).
* **One-to-one:** Each user thread maps to a kernel thread (what most modern Python setups utilize).
* **Many-to-many:** Maps many user threads to many kernel threads.

**Python's Threading Model:**

CPython's `threading` module typically uses a **one-to-one model**, where each Python thread corresponds to a kernel-level thread.  This allows Python threads to benefit from kernel-level scheduling and the ability to utilize multiple cores (for I/O-bound operations). However, the GIL *still* limits true parallelism for CPU-bound tasks within a single process. The Python API is presented in a user-friendly way, abstracting away the complexities of the underlying kernel threads.

## Using Global Variables in Python Programs

We will be using a few global variables in this course, however, this will only happen if we can't pass values to a thread when it's created.  Using global variables when they is a solution with using arguments will cause points to be taken off from assignments.

## Thread Creation and Management (in Python's `threading` module)

The `threading` module provides a high-level interface for creating and managing threads.

## Using `Thread` Functions

The first method of using threads in Python is to use functions.

## Example 1 - Simple Threading Example

Here is an example of creating, starting and ending a function thread.  The function that will be run as a thread takes in 2 arguments.  These values are passed to the function using `args=('Sleep Function', 2)`


```python
import logging
import threading
import time

def thread_function(name, sleep_time):
    """This is the function the thread will run"""
    print(f'Thread "{name}": starting')
    time.sleep(sleep_time)
    print(f'Thread "{name}": finishing')

if __name__ == '__main__':
    print('Main : before creating thread')

    # Create a thread. This doesn't start it, just it's creation
    # The args argument allow the main code to pass arguments to the thread.
    t = threading.Thread(target=thread_function, args=('Sleep Function', 2))

    print('Main : before running thread')
    # Start the thread and then keep executing. 
    # It will not wait for the thread to finish.
    t.start()

    print('Main : wait for the thread to finish')
    # Joining a thead back to the main thread.
    # The main thread will wait for this until the thread is finished
    t.join()

    print('Main : all done')
```

Program output

```text
Main                   : before creating thread
Main                   : before running thread
Thread "Sleep Function": starting
Main                   : wait for the thread to finish
Thread "Sleep Function": finishing
Main                   : all done
```

### Starting and waiting on Threads

There are two methods used for starting and waiting for class threads.

**start()**

This is a non-blocking function call. Start() will start the thread running and will return to the caller. It doesn't wait for the thread to execute. In designing programs that use threads, there are a few guiding principles:

1. Don't use sleep() to control the order of when threads run. The course uses `sleep()` in some assignments and team activities just to slow execution down to simulate the thread doing meaningful work.
2. When you start a group of threads, you as a programmer should not assume any order of execution of these threads. For example: if you create two threads (t1 and t2), and start them in the order of `t1.start()` then `t2.start()`. You should not assume that `t1` is going to run first before `t2`.

**join()**

This is a blocking function call. Join() will wait until that thread is finished executing before allowing the program to proceed further. If the thread is still busy doing something, then join() will not return until it's finished. If the thread never finishes, then your program will hang (deadlock) on `join()`. Some common reasons to use join() are:


## Example 2

Example where the threaded function only has one argument.

```python
import threading
import time

def thread_function(name):
    """This is the function the thread will run"""
    print(f'Thread "{name}": starting')
    time.sleep(2)
    print(f'Thread "{name}": finishing')

if __name__ == '__main__':
    print('Main  : before creating thread')

    t = threading.Thread(target=thread_function, args=('Bob',))

    print('Main  : before running thread')
    t.start()

    print('Main  : wait for the thread to finish')
    t.join()

    print('Main  : all done')
```

Let's look again at the coding example above. There are three main steps:

1. Create a thread and give the thread a function to execute.

Creation of a thread is handled by called the `Thread()` function in the `threading` module. The created thread is called the child thread and the thread that creates it is called the parent. (In the example below, it's the main thread creating the thread `t`)

```python
t = threading.Thread(target=thread_function, args=('Bob',))
```

**target** is used to pass the reference of the function you want to thread to execute.

**args** is used to pass information to the threaded function. Note that this is a Python tuple. **Tuples that only contain one item in them need to be created with the extra `,`. The number of arguments in your threaded function needs to match the count of the tuple.**

2. Start the thread.

A thread doesn't start to execute until you call the start() method. This allows you to create all of the threads required for your task and then start them when needed.

```python
t.start()
```

3. Wait for the thread to finish.

The parent thread has full control of any child threads that are created and can wait for the child threads to finish. The function `join()` is used for this purpose. Think of the parent thread waiting for the child threads to "re-join" the parent.

```python
t.join()
```

Program output

```text
Main        : before creating thread
Main        : before running thread
Thread "Bob": starting
Main        : wait for the thread to finish
Thread "Bob": finishing
Main        : all done
```

## Example 3

Here is an example of creating 3 threads all using the same function.

```python
import threading
import time

def thread_function(name, sleep_time):
    """This is the function the thread will run"""
    print(f'Thread "{name}": starting')
    time.sleep(sleep_time)
    print(f'Thread "{name}": finishing')

if __name__ == '__main__':
    print('Main  : before creating thread')

    # Create a threads
    t1 = threading.Thread(target=thread_function, args=('Bob', 3))
    t2 = threading.Thread(target=thread_function, args=('Jim', 2))
    t3 = threading.Thread(target=thread_function, args=('Mary', 1))

    print('Main  : before running thread')

    t1.start()
    t2.start()
    t3.start()

    print('Main  : wait for the thread to finish')

    t1.join()
    t2.join()
    t3.join()

    print('Main  : all done')
```

Output

```
Main  : before creating thread
Main  : before running thread
Thread "Bob": starting
Thread "Jim": starting
Thread "Mary": starting
Main  : wait for the thread to finish
Thread "Mary": finishing
Thread "Jim": finishing
Thread "Bob": finishing
Main  : all done
```

## Bad Example of Using Threads

In the following threading example, the code starts each thread and then calls `join()` on that thread.  This causes the program to `NOT` be concurrent but instead serially executed.  In this case, having threads serves no purpose.

```python
import threading
import time

def thread_function(name, sleep_time):
    """This is the function the thread will run"""
    print(f'Thread "{name}": starting')
    time.sleep(sleep_time)
    print(f'Thread "{name}": finishing')

if __name__ == '__main__':
    print('Main  : before creating thread')

    # Create a threads
    t1 = threading.Thread(target=thread_function, args=('Bob', 3))
    t2 = threading.Thread(target=thread_function, args=('Jim', 2))
    t3 = threading.Thread(target=thread_function, args=('Mary', 1))

    print('Main  : before running thread')

    t1.start()
    t1.join()
   
    t2.start()
    t2.join()
   
    t3.start()
    t3.join()
    
    print('Main  : all done')
```

You want to do 3 steps with threads:

1. Create as many threads as you can, then
1. Start them all with `start()`, then
1. Join them all with `Join()`


## Timer() function in the threading package

The `timer()` function allows you to run a function in the future by indicating the amount of time in seconds. The following code will create a timer that will call the function `display_hello()` in 3 seconds when the thread is started.

In the statement `thread = threading.Timer(3.0, display_hello)`, the function `display_hello` is passed to the Timer. There are no `()` used for a function that is passed as an argument to a function.

```python
import threading

def display_hello():
    print ("Hello, World!")

print('Before the thread')
thread = threading.Timer(3.0, display_hello)
thread.start()
print('After the thread - End of program')
```

Here is the output of the above program. Notice that the text `Hello World` was displayed after the text `After the thread - End of program`. The reason for this is that the main thread will continue to run after it starts the timer (ie., `thread.start()`) The program ends when the main thread and the timer are finished.

```
Before the thread
After the thread - End of program
Hello, World!
```

## Using `Thread` Classes

The primary class for creating threads. You can create a thread in two main ways:

*   Create a class that inherits from `threading.Thread`.
*   Override the `run()` method to define the code that the thread will execute.

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        # Code to be executed in the thread
        print(f"Thread {self.name} is running")

thread1 = MyThread(name="Thread-1")
thread1.start()
thread1.join()

print("Main all done")
```

**Note:** Never call the method run() yourself.  it is called when `start()` is used.


**`start()` Method:** 

Starts the thread's execution by calling the `run()` method (or the target function) in a separate thread of control.  You *must* call `start()` to begin the thread's execution.

**`join()` Method:** 

Blocks the calling thread until the thread whose `join()` method is called terminates (either normally or through an unhandled exception).  This is important for:
- Ensuring that a thread has completed before the main program exits.
- Coordinating the execution of multiple threads (e.g., waiting for a worker thread to finish processing data before using the results).
- `join()` can take an optional `timeout` argument (in seconds) to specify a maximum time to wait.

**Other Useful Methods and Attributes:**
* `is_alive()`: Returns True if the thread is still running, False otherwise.
* `name`: The thread's name (a string).
* `daemon`: A boolean value indicating whether the thread is a daemon thread.
* `ident`: thread identifier.
* `native_id`: thread native integral thread ID of the current thread.

## Thread Lifecycle (States: New, Runnable, Running, Blocked, Terminated)

![](./assets/life-cycle.png)

A thread goes through various states during its lifetime:

1.  **New:** The thread object has been created, but the `start()` method has not yet been called.  The thread is not yet executing.

2.  **Runnable (or Ready):** The `start()` method has been called, and the thread is eligible to be run by the operating system's scheduler. It is waiting for its turn to be assigned to a CPU.

3.  **Running:** The thread is currently executing its code.  The operating system's scheduler has allocated CPU time to the thread.

4.  **Blocked (or Waiting):** The thread is temporarily not eligible to run because it is waiting for some external event to occur.  This can happen for several reasons:
    *   **`sleep()`:** The thread has called `time.sleep()`, causing it to pause for a specified duration.
    *   **I/O Operation:** The thread is waiting for an I/O operation (e.g., reading from a file or network socket) to complete.
    *   **Synchronization Primitive:** The thread is waiting to acquire a lock (e.g., `threading.Lock`), waiting on a condition variable (`threading.Condition`), or waiting at a barrier (`threading.Barrier`).
    * **`join()`:** The thread is called `join()` of another thread.

5.  **Terminated (or Dead):** The thread has finished executing its `run()` method (or the target function), or it has terminated due to an unhandled exception. Once a thread is terminated, it cannot be restarted.

**Transitions between States:**

*   New → Runnable:  `start()` method is called.
*   Runnable → Running: The OS scheduler selects the thread to run.
*   Running → Runnable:  The thread's time slice expires, or it voluntarily yields the CPU (rare in Python).
*   Running → Blocked:  The thread performs a blocking operation (sleep, I/O, synchronization).
*   Blocked → Runnable:  The event the thread was waiting for occurs (I/O completes, lock becomes available, etc.).
*   Running → Terminated:  The `run()` method completes or an unhandled exception occurs.

Understanding the thread lifecycle is essential for designing and debugging multithreaded programs. You need to consider how threads will transition between states, especially when using synchronization primitives, to avoid deadlocks and ensure proper coordination.












# 1.6 Critical Sections

## Define the concept of a critical section and the potential for race conditions.

### Critical Section

A critical section is a segment of code where a shared resource (like a variable, file, or data structure) is accessed and potentially modified.  Critically, the correct operation of the program depends on *exclusive access* to this shared resource during the execution of the critical section. Only one thread or process should be allowed inside the critical section at any given time.

### Race Condition
A race condition occurs when multiple threads or processes access and modify a shared resource concurrently, and the final outcome of the program depends on the unpredictable order in which these accesses and modifications happen.  The "race" is between the threads/processes to access the shared resource, and the winner (the thread/process that executes a particular operation first) can affect the final result.  Race conditions lead to non-deterministic behavior, making bugs difficult to reproduce and debug.

A race condition is the *problem* that arises when multiple threads/processes try to access a shared resource without proper synchronization, and the critical section is the *part of the code* where this problem can manifest.

## Explain how concurrent access to shared resources can lead to unexpected and incorrect results.

Without proper synchronization mechanisms, concurrent access to shared resources can lead to incorrect results due to the interleaving of operations from different threads/processes. Here's why:

1. **Non-Atomic Operations:** Many seemingly simple operations (like incrementing a variable) are not atomic at the machine level. They often involve multiple steps:
    *   Read the current value from memory.
    *   Modify the value (e.g., add 1).
    *   Write the new value back to memory.

2. **Interleaving:** The operating system's scheduler can switch between threads/processes at any point, even in the middle of a non-atomic operation. This is called *context switching*.  The interleaving of instructions from different threads can lead to unexpected results.

3. **Lost Updates:**  One thread might read a value, modify it, and then be interrupted *before* it can write the updated value back. Another thread might then read the *original* value (which is now stale), modify it, and write it back. Finally, the first thread resumes and writes *its* modified value, overwriting the changes made by the second thread.  The update from the second thread is lost.

4. **Inconsistent Reads:** A thread might read a value that is in an inconsistent state because another thread is in the middle of modifying it.

### Illustrate race conditions with simple examples.

### Example: Incrementing a Shared Counter (Lost Update)

The following program should output 2,000,000 for the totals for both variables.  In running this program in version 3.9.6 of Python, the program had the output of:

```
Final counter value: 1,411,017, expected: 2,000,000
```

In this example program, each thread is being switched before it can update the variable "value" and then change the "counter".  Note, that versions of Python 3.10+ do not have this problem.  Although this is the case, we should always consider it as a critical section.

```python
import threading
import time

TIMES = 1000000

counter = 0  # Shared resource

def increment_counter():
    global counter
    for _ in range(TIMES):
        # Critical Section (but not protected!)
        value = counter  # Read
        value += 1       # Modify
        counter = value  # Write

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter:,}, expected: {2 * TIMES:,}")
```









# 1.7 Locks

## Introduce locks as a mechanism for synchronizing access to critical sections.

A **lock**, also known as a **mutex** (short for mutual exclusion), is a fundamental synchronization primitive used to control access to shared resources in a concurrent environment (threads or processes).  Locks provide a mechanism to enforce *mutual exclusion*, ensuring that only one thread or process can access a critical section of code at a time. This prevents race conditions and ensures data integrity.

## What are Atomic Operations

Atomic operations are fundamental synchronization primitives that execute as a single, indivisible unit, guaranteed to complete without interruption from other threads. This is crucial for preventing race conditions in simple read-modify-write sequences (like incrementing a counter), where multiple underlying steps could otherwise be interleaved incorrectly by concurrent access. Typically implemented using special hardware instructions (like Compare-and-Swap), atomic operations ensure thread safety for specific actions like incrementing or exchanging values, often providing better performance than traditional locks for these simple cases by avoiding locking overhead and potential thread blocking. While highly efficient for these targeted operations on primitive types, atomicity doesn't extend to complex, multi-step procedures, which still require locks or other synchronization mechanisms for overall safety.

In standard Python threading, particularly within the common CPython implementation, there isn't direct access to guaranteed, low-level atomic hardware operations like C#'s Interlocked. While CPython's Global Interpreter Lock (GIL) can incidentally make some individual bytecode instructions effectively atomic relative to other Python threads in the same process, this is an implementation detail and doesn't reliably prevent race conditions for compound operations like incrementing (`counter += 1`). Therefore, to ensure such multi-step operations are effectively atomic—completing indivisibly without interference from concurrent threads—the standard and necessary Python approach is to explicitly protect the critical code section using a `threading.Lock`. This lock guarantees mutual exclusion, achieving the required thread safety for the operation, albeit through a locking mechanism rather than relying on direct hardware atomic primitives.

## How Locks Work

### acquire()
Before entering a critical section, a thread attempts to *acquire* the lock.
*   If the lock is *unlocked* (not held by any other thread), the requesting thread acquires the lock and proceeds into the critical section.  The lock is now considered *locked*.
*   If the lock is *locked* (already held by another thread), the requesting thread *blocks* (waits) until the lock becomes available.

### release()
- After completing the critical section, the thread that holds the lock *releases* it. This makes the lock available for other waiting threads to acquire.

Think of a lock like a single-occupancy restroom. Only one person (thread) can be inside (critical section) at a time.  The person locks the door (acquires the lock) when they enter and unlocks the door (releases the lock) when they leave. Anyone else who wants to use the restroom must wait until the door is unlocked.

Locks **ALWAYS** protect data and **NOT** threads.  In the above restroom example, if 10 people were waiting to use the restroom, there would still only be one lock required.  A thread is never a critical section.  A critical section is something that a thread executes.

## Demonstrate how locks can prevent race conditions and ensure data integrity.

Locks prevent race conditions by ensuring that only one thread can execute the critical section at a time.  This serializes access to the shared resource, preventing the interleaving of operations that can lead to data corruption.

### Example (Corrected Counter Example)

Let's revisit the counter example from the previous section and fix it using a lock:

```python
import threading

TIMES = 1000000

counter = 0
lock = threading.Lock()  # Create a lock object

def increment_counter():
    global counter
    for _ in range(TIMES):
        # Acquire the lock before entering the critical section
        lock.acquire()
        try:
            # Critical Section (now protected by the lock)
            value = counter
            value += 1
            counter = value
        finally:
            # Release the lock after leaving the critical section
            lock.release()

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter:,}, expected: {2 * TIMES:,}")
```

1.  `lock = threading.Lock()`:  A `Lock` object is created.
2.  `lock.acquire()`:  Before accessing the shared `counter` variable, each thread *must* acquire the lock. If the lock is already held by another thread, the calling thread will block until the lock is released.
3.  `try...finally`: This ensures that the lock is *always* released, even if an exception occurs within the critical section.  This is crucial to prevent deadlocks.
4.  `lock.release()`: After modifying the `counter`, the thread releases the lock, allowing another waiting thread (if any) to acquire it and enter the critical section.

Result: With the lock in place, the race condition is eliminated. The final value of counter will consistently be 2,000,000, as expected. The acquire() and release() calls guarantee that only one thread can modify counter at a time. The try...finally block is a best practice to ensure the lock is always released.

You can also use `wait lock:` instead of `acquire()` and `release()`

```python
import threading

TIMES = 1000000

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(TIMES):
        with lock:  # Acquire the lock at the beginning of the 'with' block
            # Critical Section
            value = counter
            value += 1
            counter = value
        # Lock is automatically released at the end of the 'with' block

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter:,}, expected: {2 * TIMES:,}")
```

## Deadlock

A deadlock occurs when two or more threads are blocked indefinitely, waiting for each other to release resources (in this case, locks) that they need.

### Example of deallock

```python
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        print("Task 1 acquired lock1")
        time.sleep(0.1)  # Simulate some work
        with lock2:
            print("Task 1 acquired lock2")

def task2():
    with lock2:
        print("Task 2 acquired lock2")
        time.sleep(0.1)
        with lock1:
            print("Task 2 acquired lock1")

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Finished (but will likely deadlock before this)")
```

steps:

1.  `thread1` acquires `lock1`.
2.  `thread2` acquires `lock2`.
3.  `thread1` tries to acquire `lock2`, but it's held by `thread2`, so `thread1` blocks.
4.  `thread2` tries to acquire `lock1`, but it's held by `thread1`, so `thread2` blocks.

Other types of deadlocks:

- **Livelock:** Similar to a deadlock, but instead of blocking, threads keep retrying an operation that always fails because of another threads actions, without making any progress.

- **Starvation:** One or more threads may repeatedly lose the race for a lock and become blocked for long periods, even if there are other runnable threads, potentially indefinitely.

- **Performance Overhead:** Acquiring and releasing locks has some overhead.  Excessive locking (especially fine-grained locking) can reduce performance.

- **Complexity:** Using locks correctly requires careful design and can make code more complex and harder to reason about.


## Avoiding Deadlocks

- **Lock Ordering:** Establish a consistent order in which locks are acquired. If all threads acquire locks in the same order, circular dependencies (like the one in the deadlock example) can be avoided.
- **Lock Timeout:** Use timeouts when acquiring locks. If a thread cannot acquire a lock within a specified time, it can back off and try again later, potentially breaking the deadlock. The lock.acquire(timeout=...) method supports this.
- **Avoid Nested Locks:** Minimize the use of nested locks (acquiring a lock while already holding another lock) whenever possible.
- **Use Higher-Level Abstractions:** Consider using higher-level synchronization primitives (like queues or condition variables) that handle locking internally, reducing the risk of manual errors.
- **Deadlock Detection Tools:** Tools exist that analyze your program to detect deadlock situations.

