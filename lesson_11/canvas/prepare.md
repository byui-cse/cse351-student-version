# Lesson 11: Review of C#, C# Threads, and Tasks 

TODO - place all C# readin material in this week.  This will
be the last reading material for the course.  Students will be 
working on assignments for the rest of the course.  Maybe 2 assignments.

1) basic threads
2) advanced assignment

Overall Module Goals:

- Provide a solid foundation in C# syntax, object-oriented concepts, and concurrency.
- Introduce the Thread class and asynchronous programming with async/await.
- Explore concurrent collections and lambda functions in C#.
- Familiarize students with IDE shortcuts for efficient C# development.
- Reading Material Outline:

----
----
----
----
----
----
----
----


**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
11.1 | [C# Language Basics](#C#-Language-Basics)
11.2 | [Threading in C#](#Threading-in-C#)
11.3 | [The Task Parallel Library](#The-Task-Parallel-Library)
11.4 | [Thread Pools in C#](#Thread-Pools-in-C#)
11.5 | [Comparing C# and Python Parallelism](#Comparing-C#-and-Python-Parallelism)

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

## Software requirements for this section of the course

The development environment for this section of the course will be using C#.  Your development environment must be functional to successfully submit assignments. We will use .NET Core, Rider or VS Code. Please install these tools on your laptops as we will require them this week.

1. .NET Core - C#

    We will be using the platform independent version of C# called .NET Core. You will need to use version 9 of .NET core. Please download the version for your operating system and install it so that you’re ready for class to begin.

1. VS Code or JetBrains Rider

    JetBrains Rider is a cross-platform Integrated Development Environment (IDE) that will speed up development and give you experience that will prepare you for coding in the workplace. Using this tool will give you many advantages over Visual Studio Code (which you probably have used in the past). If you live in an area of the world with limited Internet bandwidth, you may use Visual Studio Code to work on the assignments; however, it is highly encouraged to use JetBrains Rider if you can. Rider supplies better coding helps, a working run button, and help with debugging errors.

1. Running with VS Code

    In order to run code using VS Code, you will need to use the terminal and the command `dotnet run` in the folder containing your project in order to produce results.

1. Setting up JetBrains Rider (Preferred IDE)

    You will need to activate a [student license](https://www.jetbrains.com/community/education/#students) which involves creating an account and supplying your BYU-Idaho email address. You will need to download [JetBrains Rider](https://www.jetbrains.com/rider/) or the [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/) (which then allows you to install Rider).


### Review of C#

This section of the course requires that you already know how to write software in C#. If you’d like a review of C#, you should look at the following links.  We will not be spending time in class to review C#.

- [W3Schools C# Basic Tutorials](https://www.w3schools.com/cs/index.php). Focus should be given to the following modules: variables, data types, strings, methods, and loops.
- [C# Classes](https://www.w3schools.com/cs/cs_oop.php)
- [C# Interfaces](https://www.w3schools.com/cs/cs_interface.php)
- [C# Encapsulation](https://www.w3schools.com/cs/cs_abstract.php)
- [C# Inheritance](https://www.w3schools.com/cs/cs_inheritance.php)
- [C# Polymorphism](https://www.w3schools.com/cs/cs_polymorphism.php)
- [C# Files](https://www.w3schools.com/cs/cs_files.php)
- [C# Lambda Functions](https://www.programiz.com/csharp-programming/lambda-expression)


## Key Differences: Threading in Python vs. C#

While the fundamental concepts of threading and concurrency – managing shared resources, avoiding race conditions, preventing deadlocks – apply across languages, the specific implementation details and capabilities differ significantly between Python and C#/.NET. Understanding these differences is crucial as you transition from using Python's threading model to C#'s.

### The Global Interpreter Lock (GIL)

- **Python**: Python employs a Global Interpreter Lock (GIL). This is a mutex that allows only one thread to execute Python bytecode at any given time within a single process, even on multi-core processors. While effective for simplifying memory management in Python, it fundamentally limits the ability of threads to achieve true parallelism for CPU-bound tasks. To achieve CPU-bound parallelism in Python, one typically resorts to the multiprocessing module, using separate processes instead of threads.   

- **C# (.NET)**: C# and the .NET runtime do not have a GIL. This is arguably the most significant difference. C# threads managed by the .NET runtime can execute truly in parallel on multiple CPU cores. This means that for CPU-bound tasks (e.g., complex calculations, data processing), using multiple threads in C# can lead to substantial performance improvements proportional to the number of available cores, a benefit largely unrealized with threads in Python. For I/O-bound tasks, both Python and C# threads can provide concurrency benefits by allowing threads to overlap waiting periods.   


### Core Libraries and Abstractions

- **Python**: You primarily worked with the threading module for thread-based concurrency (often I/O-bound focus due to GIL), the multiprocessing module for process-based parallelism (bypassing the GIL for CPU-bound tasks), and potentially concurrent.futures which provides a common interface over both.

- **C#**: C# offers a richer, more layered set of built-in libraries within the System.Threading and System.Threading.Tasks namespaces:

    - System.Threading.Thread: Represents a low-level OS thread, offering direct control but generally less used for common tasks now.

    - System.Threading.ThreadPool: Provides a pool of managed worker threads, reducing the overhead of thread creation/destruction for short tasks.

    - Task Parallel Library (TPL - System.Threading.Tasks): This is the cornerstone of modern C# concurrency. It introduces the Task and Task<TResult> abstractions, representing asynchronous operations. TPL includes high-level constructs like `Task.Run`, `Parallel.For`, and `Parallel.ForEach`, which often utilize the ThreadPool efficiently behind the scenes.   
    async / await Keywords: Built upon the TPL, these keywords provide a vastly simplified syntax for writing asynchronous (especially I/O-bound) code that is non-blocking and highly readable.   

### Memory Model

- **Python**: While Python manages memory, the details of its memory model regarding visibility and reordering across threads are less formally specified than in C#.

- **C#**: C# and .NET adhere to a more formally defined memory model (ECMA/ISO standards). This provides stronger guarantees about how memory operations (reads and writes) become visible to other threads and how instruction reordering might occur, leading to potentially more predictable behavior in complex concurrent scenarios across different hardware architectures. (Note: Deep understanding requires delving into memory barriers and volatile semantics, often handled implicitly by higher-level C# constructs).


### Type System

- **Python**: Python's dynamic typing offers flexibility but means type-related errors (e.g., passing incorrect data types to threads) might only surface at runtime.   

- **C#**: C#'s static typing allows the compiler to catch many type errors before runtime. In concurrent programming, this can help prevent certain classes of bugs related to data sharing and communication between threads or tasks, as type mismatches are detected early.   

## Creating and Using Threads in C#

While modern C# often favors higher-level abstractions like the Task Parallel Library (TPL), understanding the fundamental System.Threading.Thread class is essential. It provides direct control over operating system threads and forms the basis upon which other abstractions are built. Using Thread directly gives you fine-grained control but requires more manual management.

1. The System.Threading.Thread Class

This class, located in the System.Threading namespace, represents a managed thread within your .NET application. Each instance of Thread corresponds to an underlying operating system thread.

2. Creating Threads

You create a thread by instantiating the Thread class, passing it a delegate that represents the method the thread will execute. There are a few ways to specify this method:

Using ThreadStart Delegate: For methods that take no parameters and return void.

C#

using System;
using System.Threading;

public class BasicThreading
{
    public static void DoWork()
    {
        Console.WriteLine($"Worker thread {Thread.CurrentThread.ManagedThreadId}: Starting work.");
        Thread.Sleep(1000); // Simulate work
        Console.WriteLine($"Worker thread {Thread.CurrentThread.ManagedThreadId}: Finished work.");
    }

    public static void Main_Example1() // Renamed Main for clarity
    {
        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Creating worker thread.");

        // Create a Thread object, passing the method to execute via ThreadStart delegate
        Thread workerThread = new Thread(new ThreadStart(DoWork));
        // Or more concisely: Thread workerThread = new Thread(DoWork);

        // Start the thread's execution
        workerThread.Start();

        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Worker thread started. Waiting for it to finish...");

        // Wait for the worker thread to complete before the main thread continues
        workerThread.Join();

        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Worker thread finished. Exiting.");
    }
}
Using ParameterizedThreadStart Delegate: For methods that take a single parameter of type object and return void. This is how you pass data directly via the Start method.

C#

using System;
using System.Threading;

public class ParameterizedThreading
{
    public static void DoWorkWithParameter(object data)
    {
        // Parameter is always object, needs casting
        if (data is string message) // Use pattern matching for safe casting
        {
            Console.WriteLine($"Worker thread {Thread.CurrentThread.ManagedThreadId}: Received '{message}'. Starting work.");
            Thread.Sleep(1500); // Simulate work
            Console.WriteLine($"Worker thread {Thread.CurrentThread.ManagedThreadId}: Finished work with '{message}'.");
        }
        else
        {
             Console.WriteLine($"Worker thread {Thread.CurrentThread.ManagedThreadId}: Received invalid data type.");
        }
    }

    public static void Main_Example2()
    {
        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Creating parameterized worker thread.");

        Thread workerThread = new Thread(new ParameterizedThreadStart(DoWorkWithParameter));
        // Or more concisely: Thread workerThread = new Thread(DoWorkWithParameter);

        string messageToSend = "Hello from Main!";
        // Start the thread and pass data via the Start method
        workerThread.Start(messageToSend); // The argument here is passed as 'object'

        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Worker thread started. Waiting...");
        workerThread.Join();
        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Exiting.");
    }
}
Note: Using object sacrifices type safety. You must cast the parameter within the thread method, which can lead to runtime errors if the wrong type is passed.

Using Lambda Expressions (Recommended for Simplicity): Often the cleanest way, especially for short tasks or when capturing local variables.

C#

using System;
using System.Threading;

public class LambdaThreading
{
    public static void Main_Example3()
    {
        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Creating worker thread using lambda.");

        string dataToPass = "Some Data";
        int iterations = 5;

        // Create thread using a lambda expression
        Thread workerThread = new Thread(() =>
        {
            Console.WriteLine($"Worker thread {Thread.CurrentThread.ManagedThreadId}: Started with data '{dataToPass}'.");
            for (int i = 0; i < iterations; i++)
            {
                Console.WriteLine($"Worker thread {Thread.CurrentThread.ManagedThreadId}: Working... ({i + 1}/{iterations})");
                Thread.Sleep(200);
            }
            Console.WriteLine($"Worker thread {Thread.CurrentThread.ManagedThreadId}: Finished.");
        });

        // Optionally name the thread for easier debugging
        workerThread.Name = "MyLambdaWorker";

        workerThread.Start();

        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Worker thread '{workerThread.Name}' started. Waiting...");
        workerThread.Join();
        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Exiting.");
    }
}
Lambda Capture: Be mindful of variable lifetimes when capturing variables (like dataToPass and iterations) inside a lambda. If the variable's value changes in the outer scope after the thread starts but before the thread uses it, the thread might see the changed value (depending on timing).

3. Starting Threads

Once a Thread object is created, you start its execution by calling the thread.Start() method.

If using ParameterizedThreadStart, you pass the data object to the Start(object parameter) overload.
If using ThreadStart or a parameterless lambda, you call the parameterless Start().
4. Joining Threads (thread.Join())

Often, the main thread needs to wait for a worker thread to complete its task before proceeding (e.g., before using the results or exiting the application). The thread.Join() method blocks the calling thread until the thread on which Join() was called terminates.

5. Foreground vs. Background Threads

Foreground Threads (Default): A .NET application will not exit as long as any foreground threads are still running. They keep the process alive.
Background Threads: The application will exit even if background threads are still running. They are automatically terminated when all foreground threads have completed.
You can control this using the IsBackground property: thread.IsBackground = true;
Set IsBackground before calling Start().
C#

using System;
using System.Threading;

public class BackgroundThreading
{
    public static void BackgroundWorker()
    {
        Console.WriteLine("Background thread: Starting work...");
        Thread.Sleep(3000); // Simulate long work
        Console.WriteLine("Background thread: Finishing work. (May not be printed if main exits first)");
    }

    public static void Main_Example4()
    {
        Console.WriteLine("Main thread: Creating background worker.");
        Thread worker = new Thread(BackgroundWorker);

        // Set the thread to be a background thread
        worker.IsBackground = true;

        worker.Start();

        Console.WriteLine("Main thread: Background worker started. Main thread is exiting NOW.");
        // Note: We DO NOT call worker.Join() here.
        // Because the worker is a background thread, the application
        // will exit immediately after this line, potentially terminating
        // the background thread before it finishes its Sleep.
    }
}
(Run Example 4, and you'll likely see the application exit before the "Background thread: Finishing work" message prints). If you comment out worker.IsBackground = true;, the application will wait for the worker to finish.

6. Naming Threads

For debugging purposes, it's helpful to give threads meaningful names using the Name property:

C#

Thread workerThread = new Thread(DoWork);
workerThread.Name = "MyDataProcessor";
workerThread.Start();
The thread name will appear in debugging tools like Visual Studio's Threads window.


























































## Synchronization Primitives in C#

Purpose: Implementing mutual exclusion and coordination mechanisms (assuming concepts are known).
The lock Keyword:
Provides exclusive locking on a reference object (syntactic sugar for Monitor).
Ensures only one thread enters the code block at a time.
Usage: lock (lockObject) { /* critical section */ }.
System.Threading.Monitor:
Underlying mechanism for lock.
Methods: Enter, Exit, Wait, Pulse, PulseAll (for building complex condition variable logic).
System.Threading.Mutex:
Similar functionality to lock/Monitor but can be system-wide (named).
Used for cross-process synchronization.
System.Threading.Semaphore / SemaphoreSlim:
Limits the number of threads that can access a resource or code section concurrently.
WaitOne()/Wait(), Release().
SemaphoreSlim is a lightweight version recommended for intra-process use.
Event Wait Handles:
AutoResetEvent: Signals one waiting thread, then automatically resets.
ManualResetEvent / ManualResetEventSlim: Signals all waiting threads, stays signaled until manually reset. Slim is lightweight version.
System.Threading.ReaderWriterLockSlim:
Optimizes scenarios with many readers and infrequent writers. Allows multiple readers concurrently but only one writer exclusively.
System.Threading.Interlocked:
Provides atomic operations (e.g., Increment, Add, CompareExchange) for simple types without needing explicit locks.


## The ThreadPool (System.Threading.ThreadPool)

Concept: A pool of managed worker threads maintained by the .NET runtime.
Purpose: Efficiently executes short background tasks without the overhead of creating/destroying threads manually.
Usage: ThreadPool.QueueUserWorkItem(WaitCallback, [state object]).
Advantages: Reduced overhead, resource management.
Context: Often used implicitly by higher-level abstractions like TPL and async/await. Direct use is less common now but good to understand.


## Task Parallel Library (TPL)

The Preferred Abstraction: System.Threading.Tasks namespace.
Task & Task<TResult>: Represent units of asynchronous work (potentially, but not necessarily, running on a separate thread).
Creating and Running:
Task.Run(() => {...}): Easiest way to run CPU-bound work on the ThreadPool.
Task.Factory.StartNew(...): More complex configuration.
Working with Results:
task.Result (blocks if task not complete, returns value for Task<TResult>).
await task (used with async methods - see next section).
Waiting: task.Wait(), Task.WaitAll(), Task.WaitAny().
Data Parallelism:
Parallel.For(): Parallel execution of a loop with a counter.
Parallel.ForEach(): Parallel execution over an IEnumerable collection.


## Asynchronous Programming with async and await

Building on TPL: Keywords async and await simplify writing asynchronous code, especially for I/O-bound operations.
Goal: Free up threads while waiting for operations (network, disk I/O, database calls) to complete, improving responsiveness and scalability.
async Modifier: Indicates a method can use await.
await Operator: Asynchronously waits for a Task (or other awaitable) to complete without blocking the current thread. Control returns to the caller.
Return Types: async Task, async Task<TResult>, async void (avoid async void except for event handlers).
Common Pattern: Chaining async operations naturally.


## Concurrent Collections (System.Collections.Concurrent)

Problem: Standard .NET collections (List<T>, Dictionary<TKey, TValue>, etc.) are not thread-safe for modification.
Solution: The System.Collections.Concurrent namespace provides thread-safe alternatives.
Key Collections:
ConcurrentQueue<T>: Thread-safe FIFO queue.
ConcurrentStack<T>: Thread-safe LIFO stack.
ConcurrentBag<T>: Thread-safe unordered collection (optimized for producers/consumers on same thread).
ConcurrentDictionary<TKey, TValue>: Thread-safe dictionary/hash map.
BlockingCollection<T>: Wraps a concurrent collection (like ConcurrentQueue) to provide blocking Add and Take operations, ideal for producer-consumer patterns.
Benefit: Simplifies concurrent code by handling internal locking.


