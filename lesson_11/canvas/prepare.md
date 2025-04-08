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

TODO

### System.Threading.Thread Class

This class, located in the System.Threading namespace, represents a managed thread within your .NET application. Each instance of Thread corresponds to an underlying operating system thread.

### Creating Threads

You create a thread by instantiating the Thread class, passing it a delegate that represents the method the thread will execute. There are a few ways to specify this method:

### 1) Using ThreadStart Delegate

For methods that take no parameters and return void.

```C#
using System;
using System.Threading;

public class BasicThreading
{
    public static void DoWork()
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($"Worker thread {id}: Starting work.");
        Thread.Sleep(1000); // Simulate work
        Console.WriteLine($"Worker thread {id}: Finished work.");
    }

    public static void Main() // Renamed Main for clarity
    {
        var id = Thread.CurrentThread.ManagedThreadId;

        Console.WriteLine($"Main thread {id}: Creating worker thread.");

        // Create a Thread object, passing the method to execute
        Thread workerThread = new Thread(DoWork);

        // Start the thread's execution
        workerThread.Start();

        Console.WriteLine($"Main thread {id}: Worker thread started. Waiting for it to finish...");

        // Wait for the worker thread to complete before the main thread continues
        workerThread.Join();

        Console.WriteLine($"Main thread {id}: Worker thread finished. Exiting.");
    }
}
```

Output:

```
Main thread 1: Creating worker thread.
Main thread 1: Worker thread started. Waiting for it to finish...
Worker thread 9: Starting work.
Worker thread 9: Finished work.
Main thread 1: Worker thread finished. Exiting.
```


### 2) Passing arguments to a thread

For methods that take a single parameter of type object and return void. This is how you pass data directly via the Start method.

```C#
using System;
using System.Threading;

public class ParameterizedThreading
{
    public static void DoWorkWithParameter(object data)
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        // Parameter is always object, needs casting
        if (data is string message) // Use pattern matching for safe casting
        {
            Console.WriteLine($"Worker thread {id}: Received '{message}'. Starting work.");
            Thread.Sleep(1500); // Simulate work
            Console.WriteLine($"Worker thread {id}: Finished work with '{message}'.");
        }
        else
        {
             Console.WriteLine($"Worker thread {id}: Received invalid data type.");
        }
    }

    public static void Main()
    {
        var id = Thread.CurrentThread.ManagedThreadId;

        Console.WriteLine($"Main thread {id}: Creating parameterized worker thread.");

        Thread workerThread = new Thread(DoWorkWithParameter);

        string messageToSend = "Hello from Main!";

        // Start the thread and pass data via the Start method
        workerThread.Start(messageToSend); // The argument here is passed as 'object'

        Console.WriteLine($"Main thread {id}: Worker thread started. Waiting...");
        workerThread.Join();
        Console.WriteLine($"Main thread {id}: Exiting.");
    }
}
```

Output:

```
Main thread 1: Creating parameterized worker thread.
Main thread 1: Worker thread started. Waiting...
Worker thread 9: Received 'Hello from Main!'. Starting work.
Worker thread 9: Finished work with 'Hello from Main!'.
Main thread 1: Exiting.
```

Note: Using object sacrifices type safety. You must cast the parameter within the thread method, which can lead to runtime errors if the wrong type is passed.

### 3) Using Lambda Expressions (Recommended for Simplicity) 

Often the cleanest way, especially for short tasks or when capturing local variables.

```C#
using System;
using System.Threading;

public class LambdaThreading
{
    public static void Main()
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($"Main thread {id}: Creating worker thread using lambda.");

        string dataToPass = "Some Data";
        int iterations = 5;

        // Create thread using a lambda expression
        Thread workerThread = new Thread(() =>
        {
            var id = Thread.CurrentThread.ManagedThreadId;
            Console.WriteLine($"Thread name: {Thread.CurrentThread.Name}");
            Console.WriteLine($"Worker thread {id}: Started with data '{dataToPass}'.");
            for (int i = 0; i < iterations; i++)
            {
                Console.WriteLine($"Worker thread {id}: Working... ({i + 1}/{iterations})");
                Thread.Sleep(200);
            }
            Console.WriteLine($"Worker thread {id}: Finished.");
        });

        // Optionally name the thread for easier debugging
        workerThread.Name = "MyLambdaWorker";

        workerThread.Start();

        Console.WriteLine($"Main thread {id}: Worker thread '{workerThread.Name}' started. Waiting...");
        workerThread.Join();
        Console.WriteLine($"Main thread {id}: Exiting.");
    }
}
```

Output:

```
Main thread 1: Creating worker thread using lambda.
Main thread 1: Worker thread 'MyLambdaWorker' started. Waiting...
Thread name: MyLambdaWorker
Worker thread 11: Started with data 'Some Data'.
Worker thread 11: Working... (1/5)
Worker thread 11: Working... (2/5)
Worker thread 11: Working... (3/5)
Worker thread 11: Working... (4/5)
Worker thread 11: Working... (5/5)
Worker thread 11: Finished.
Main thread 1: Exiting.
```

Lambda Capture: Be mindful of variable lifetimes when capturing variables (like dataToPass and iterations) inside a lambda. If the variable's value changes in the outer scope after the thread starts but before the thread uses it, the thread might see the changed value (depending on timing).

### Starting Threads

Once a Thread object is created, you start its execution by calling the `thread.Start()` method.  You pass the data object to the Start(object parameter) overload.  If using ThreadStart or a parameterless lambda, you call the parameterless Start().


### Joining Threads (thread.Join())

Often, the main thread needs to wait for a worker thread to complete its task before proceeding (e.g., before using the results or exiting the application). The `thread.Join()` method blocks the calling thread until the thread on which Join() was called terminates.

### Foreground vs. Background Threads

- **Foreground Threads (Default)**: A .NET application will not exit as long as any foreground threads are still running. They keep the process alive.

- **Background Threads**: The application will exit even if background threads are still running. They are automatically terminated when all foreground threads have completed.
You can control this using the IsBackground property: thread.IsBackground = true;
Set IsBackground before calling Start().

Example of a background thread

```C#
using System;
using System.Threading;

public class BackgroundThreading
{
    public static void BackgroundWorker()
    {
        Console.WriteLine("Background thread: Starting work...");
        Thread.Sleep(3000); // Simulate long work
        Console.WriteLine("Background thread: Finishing work.");
    }

    public static void Main()
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
```

Output:

```
Main thread: Creating background worker.
Main thread: Background worker started. Main thread is exiting NOW.
Background thread: Starting work...
```

Note: If you comment out `worker.IsBackground = true;`, the application will wait for the worker to finish.

### Naming Threads

For debugging purposes, it's helpful to give threads meaningful names using the Name property:

```C#
Thread workerThread = new Thread(DoWork);
workerThread.Name = "MyDataProcessor";
workerThread.Start();
```

## Synchronization Primitives in C#

Having understood the fundamental need for synchronization from our earlier discussions (preventing race conditions, ensuring data integrity, coordinating actions between concurrent operations), let's explore the specific tools C# provides to achieve this. Unlike Python's GIL which implicitly handles some low-level interpreter locking, C# requires explicit synchronization when multiple threads access shared, mutable state. Fortunately, the .NET Framework offers a rich set of primitives.

1. The lock Keyword (Monitor)

The lock statement is the most commonly used synchronization primitive in C#. It provides a simple way to acquire a mutual-exclusion lock for a given object, ensuring that only one thread can enter the locked block of code (critical section) at a time.

Mechanism: lock(obj) is syntactic sugar for `System.Threading.Monitor.Enter(obj)` followed by a try...finally block containing System.Threading.Monitor.Exit(obj).

Usage: Always lock on a dedicated private readonly object instance field to avoid unintended consequences of locking on public objects or types (this, typeof(MyClass)).
Purpose: Simple mutual exclusion for protecting shared data access.

```C#
using System;
using System.Threading;
using System.Threading.Tasks; // Using Task for easy thread management

public class LockExample
{
    // This is a global variable shared by all threads - race condition!!!!
    private static int _sharedCounter = 0;

    private static readonly object _lockObject = new object(); // Dedicated lock object

    public static void IncrementCounter()
    {
        for (int i = 0; i < 10000000; i++)
        {
            // Acquire lock before accessing sharedCounter
            lock (_lockObject)
            {
                _sharedCounter++;
            }
            // Lock is automatically released when exiting the block
        }
    }

    public static void Main()
    {
        _sharedCounter = 0; // Reset for demo
        Console.WriteLine("Running Lock Example...");

        // Use Task.Run which uses the ThreadPool for convenience
        Task t1 = Task.Run(IncrementCounter);
        Task t2 = Task.Run(IncrementCounter);

        Task.WaitAll(t1, t2); // Wait for both tasks to complete

        Console.WriteLine($"Expected counter: 20000000");
        Console.WriteLine($"Actual counter  : {_sharedCounter}"); // Should be 200000
    }
}
```

Output:

```
Running Lock Example...
Expected counter: 20000000
Actual counter  : 20000000
```

Here is the same program example without a lock

```C#
using System;
using System.Threading;
using System.Threading.Tasks; // Using Task for easy thread management

public class LockExample
{
    // This is a global variable shared by all threads - race condition!!!!
    private static int _sharedCounter = 0;

    public static void IncrementCounter()
    {
        for (int i = 0; i < 10000000; i++)
        {
            _sharedCounter++;
        }
    }

    public static void Main()
    {
        _sharedCounter = 0; // Reset for demo
        Console.WriteLine("Running Lock Example...");

        // Use Task.Run which uses the ThreadPool for convenience
        Task t1 = Task.Run(IncrementCounter);
        Task t2 = Task.Run(IncrementCounter);

        Task.WaitAll(t1, t2); // Wait for both tasks to complete

        Console.WriteLine($"Expected counter: 20000000");
        Console.WriteLine($"Actual counter  : {_sharedCounter}"); // Should be 200000
    }
}
```

Output:

```
Running Lock Example...
Expected counter: 20000000
Actual counter  : 10127122
```

2. System.Threading.Monitor

The Monitor class provides the underlying mechanism for the lock statement and offers more advanced features, including condition variable support (Wait, Pulse, PulseAll).

- Purpose: Explicit locking and building more complex synchronization patterns like producer-consumer with wait/notify logic.

-  Methods: Enter, Exit, TryEnter, Wait, Pulse, PulseAll. Wait releases the lock and blocks until signaled by Pulse or PulseAll from another thread (which must also hold the lock).

```C#
using System;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;

public class MonitorExample // Basic Producer-Consumer Signal
{
    private static readonly object _lockObject = new object();
    private static Queue<int> _queue = new Queue<int>();
    private static bool _producingFinished = false;

    public static void Producer()
    {
        for (int i = 0; i < 5; i++)
        {
            lock (_lockObject)
            {
                _queue.Enqueue(i);
                Console.WriteLine($"Producer added {i}, queue size: {_queue.Count}");
                // Pulse signals ONE waiting thread (if any)
                Monitor.Pulse(_lockObject);
            }
            Thread.Sleep(100); // Simulate production time
        }
        lock(_lockObject) {
             _producingFinished = true;
             Monitor.PulseAll(_lockObject); // Wake all consumers to check finished flag
        }
        Console.WriteLine("Producer finished.");
    }

    public static void Consumer(string name)
    {
        while (true)
        {
            int item = -1; // Default value
            lock (_lockObject)
            {
                // Wait while the queue is empty AND production isn't finished
                while (_queue.Count == 0 && !_producingFinished)
                {
                    Console.WriteLine($"{name}: Queue empty, waiting...");
                    Monitor.Wait(_lockObject); // Releases lock and waits for Pulse/PulseAll
                    // Reacquires lock upon waking
                }

                if (_queue.Count > 0) {
                    item = _queue.Dequeue();
                } else if (_producingFinished) {
                    // Queue is empty and producer is done
                    Console.WriteLine($"{name}: No more items, exiting.");
                    break; // Exit the loop
                }
            } // Lock released here

            if (item != -1) {
                 Console.WriteLine($"{name}: Consumed {item}");
                 Thread.Sleep(200); // Simulate consumption time
            }
        }
    }

    public static void Main()
    {
        _queue.Clear();
        _producingFinished = false;
        Console.WriteLine("\nRunning Monitor Example (Producer-Consumer)...");

        Task producerTask = Task.Run(Producer);
        Task consumerTask1 = Task.Run(() => Consumer("Consumer 1"));
        Task consumerTask2 = Task.Run(() => Consumer("Consumer 2"));

        Task.WaitAll(producerTask, consumerTask1, consumerTask2);
        Console.WriteLine("Monitor Example finished.");
    }
}
```

Output:

```
Running Monitor Example (Producer-Consumer)...
Producer added 0, queue size: 1
Consumer 2: Queue empty, waiting...
Consumer 1: Consumed 0
Producer added 1, queue size: 1
Consumer 2: Consumed 1
Consumer 1: Queue empty, waiting...
Producer added 2, queue size: 1
Consumer 1: Consumed 2
Consumer 2: Queue empty, waiting...
Producer added 3, queue size: 1
Consumer 2: Consumed 3
Consumer 1: Queue empty, waiting...
Producer added 4, queue size: 1
Consumer 1: Consumed 4
Consumer 2: Queue empty, waiting...
Producer finished.
Consumer 2: No more items, exiting.
Consumer 1: No more items, exiting.
Monitor Example finished.
```

3. System.Threading.Mutex

A Mutex (Mutual Exclusion) is similar to lock, but it can be system-wide, meaning it can synchronize threads across different processes if given a name.

- Purpose: Primarily for inter-process synchronization, though usable within a single process.

- Methods: WaitOne() (acquire), ReleaseMutex() (release).

- Overhead: Generally has more overhead than lock or Monitor for intra-process locking.

```C#
using System;
using System.Threading;

public class MutexExample
{
    // Create a named mutex (can be system-wide) or an unnamed one (local)
    // Note: For system-wide, requires appropriate permissions.
    private static Mutex _mutex = new Mutex(false, "MyUniqueMutexName"); // false = initially not owned
    // For local only: private static Mutex _mutex = new Mutex();

    public static void AccessSharedResource(string threadName)
    {
        Console.WriteLine($"{threadName}: Trying to acquire mutex...");
        bool lockTaken = false;
        try
        {
            // Wait indefinitely to acquire the mutex
            lockTaken = _mutex.WaitOne(); // Can use WaitOne(timeout)
            if (lockTaken)
            {
                 Console.WriteLine($"{threadName}: Acquired mutex. Accessing resource...");
                 Thread.Sleep(1000); // Simulate work
                 Console.WriteLine($"{threadName}: Releasing mutex...");
            } else {
                 Console.WriteLine($"{threadName}: Failed to acquire mutex (e.g., timeout)");
            }

        }
        finally
        {
            // Ensure the mutex is released if it was acquired
            if (lockTaken)
            {
                _mutex.ReleaseMutex();
            }
        }
    }

    public static void Main()
    {
         Console.WriteLine("\nRunning Mutex Example...");
         // Note: Running this example as-is primarily shows intra-process locking.
         // To see inter-process, run multiple instances of the compiled application.
         Task t1 = Task.Run(() => AccessSharedResource("Thread A"));
         Task t2 = Task.Run(() => AccessSharedResource("Thread B"));

         Task.WaitAll(t1, t2);

         _mutex.Dispose(); // Release OS resource
         Console.WriteLine("Mutex Example finished.");
    }
}
```

Output:

```
Running Mutex Example...
Thread A: Trying to acquire mutex...
Thread B: Trying to acquire mutex...
Thread A: Acquired mutex. Accessing resource...
Thread A: Releasing mutex...
Thread B: Acquired mutex. Accessing resource...
Thread B: Releasing mutex...
Mutex Example finished.
```

4. System.Threading.Semaphore / SemaphoreSlim

A semaphore limits the number of threads that can access a specific resource or pool of resources concurrently.

- Purpose: Control concurrency level, manage resource pools (e.g., database connections).
- SemaphoreSlim: A lightweight version optimized for intra-process use (generally preferred over Semaphore unless cross-process is needed).
- Methods: Wait()/WaitAsync() (acquire permit, decrements count), Release() (release permit, increments count).

```C#
using System;
using System.Threading;
using System.Threading.Tasks;

public class SemaphoreSlimExample
{
    // Allow up to 3 threads to access the resource concurrently
    private static SemaphoreSlim _semaphore = new SemaphoreSlim(3, 3); // Initial count=3, Max count=3

    public static async Task AccessLimitedResource(int threadId)
    {
        Console.WriteLine($"Thread {threadId}: Waiting to access resource (Available: {_semaphore.CurrentCount})...");
        await _semaphore.WaitAsync(); // Acquire semaphore slot (async)
        try
        {
            Console.WriteLine($"Thread {threadId}: ---> Access granted (Available: {_semaphore.CurrentCount}). Working...");
            await Task.Delay(TimeSpan.FromSeconds(random.Next(1, 4))); // Simulate work
            Console.WriteLine($"Thread {threadId}: <--- Finished work. Releasing slot.");
        }
        finally
        {
            _semaphore.Release(); // Release semaphore slot
        }
    }
    private static Random random = new Random();
    public static async Task Main()
    {
        Console.WriteLine("\nRunning SemaphoreSlim Example...");
        var tasks = new List<Task>();
        for (int i = 1; i <= 7; i++) // Start 7 tasks
        {
            tasks.Add(AccessLimitedResource(i));
        }
        await Task.WhenAll(tasks);
        _semaphore.Dispose();
        Console.WriteLine("SemaphoreSlim Example finished.");
    }
}
```

Output:

```
Running SemaphoreSlim Example...
Thread 1: Waiting to access resource (Available: 3)...
Thread 1: ---> Access granted (Available: 2). Working...
Thread 2: Waiting to access resource (Available: 2)...
Thread 2: ---> Access granted (Available: 1). Working...
Thread 3: Waiting to access resource (Available: 1)...
Thread 3: ---> Access granted (Available: 0). Working...
Thread 4: Waiting to access resource (Available: 0)...
Thread 5: Waiting to access resource (Available: 0)...
Thread 6: Waiting to access resource (Available: 0)...
Thread 7: Waiting to access resource (Available: 0)...
Thread 2: <--- Finished work. Releasing slot.
Thread 4: ---> Access granted (Available: 0). Working...
Thread 3: <--- Finished work. Releasing slot.
Thread 1: <--- Finished work. Releasing slot.
Thread 5: ---> Access granted (Available: 0). Working...
Thread 6: ---> Access granted (Available: 0). Working...
Thread 4: <--- Finished work. Releasing slot.
Thread 7: ---> Access granted (Available: 0). Working...
Thread 5: <--- Finished work. Releasing slot.
Thread 7: <--- Finished work. Releasing slot.
Thread 6: <--- Finished work. Releasing slot.
SemaphoreSlim Example finished.
```

5. Event Wait Handles (AutoResetEvent, ManualResetEvent, ManualResetEventSlim)

Used for signaling between threads. One thread waits (WaitOne) until another thread signals (Set).

- AutoResetEvent: Resets automatically to non-signaled after releasing one waiting thread.
-  ManualResetEvent / ManualResetEventSlim: Stays signaled until explicitly reset (Reset()). Releases all waiting threads while signaled. Slim is preferred for intra-process use.
- Purpose: Thread communication, signaling completion or readiness.

```C#
using System;
using System.Threading;
using System.Threading.Tasks;

public class ManualResetEventSlimExample
{
    private static ManualResetEventSlim _event = new ManualResetEventSlim(false); // Initially not signaled

    public static void WaitingThread()
    {
        Console.WriteLine("WaitingThread: Waiting for signal...");
        _event.Wait(); // Blocks until _event.Set() is called
        Console.WriteLine("WaitingThread: Signal received! Continuing work.");
        // ... do work after signal ...
         _event.Dispose(); // Clean up
    }

    public static void SignalingThread()
    {
        Console.WriteLine("SignalingThread: Performing work before signaling...");
        Thread.Sleep(2000); // Simulate work
        Console.WriteLine("SignalingThread: Setting signal!");
        _event.Set(); // Signal waiting threads
    }

    public static void Main()
    {
        Console.WriteLine("\nRunning ManualResetEventSlim Example...");
        Task waiter = Task.Run(WaitingThread);
        Task signaler = Task.Run(SignalingThread);

        Task.WaitAll(waiter, signaler);
        Console.WriteLine("ManualResetEventSlim Example finished.");
    }
}
```

Output:

```
Running ManualResetEventSlim Example...
WaitingThread: Waiting for signal...
SignalingThread: Performing work before signaling...
SignalingThread: Setting signal!
WaitingThread: Signal received! Continuing work.
ManualResetEventSlim Example finished.
```


6. System.Threading.ReaderWriterLockSlim

Optimized for scenarios where a resource is read much more frequently than it is written. It allows multiple concurrent readers or one exclusive writer.

- Purpose: High-concurrency reads with exclusive writes.
- Methods: EnterReadLock(), ExitReadLock(), EnterWriteLock(), ExitWriteLock().

```C#
using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

public class ReaderWriterLockSlimExample
{
    private static ReaderWriterLockSlim _lock = new ReaderWriterLockSlim();
    private static Dictionary<int, string> _sharedData = new Dictionary<int, string>();
    private static Random _random = new Random();

    private const int READERS = 5;
    private const int WRITERS = 3;
    
    public static void Reader(int id)
    {
        try
        {
            _lock.EnterReadLock(); // Acquire read lock
            Console.WriteLine($"Reader {id}: Acquired read lock.");
            // Simulate reading
            int keyToRead = _random.Next(1, 5);
            _sharedData.TryGetValue(keyToRead, out string value);
            Console.WriteLine($"Reader {id}: Read key {keyToRead}, value: '{value ?? "N/A"}'.");
            Thread.Sleep(_random.Next(50, 200));
        }
        finally
        {
            _lock.ExitReadLock(); // Release read lock
            Console.WriteLine($"Reader {id}: Released read lock.");
        }
    }

    public static void Writer(int id)
    {
        try
        {
            _lock.EnterWriteLock(); // Acquire write lock (exclusive)
            Console.WriteLine($"Writer {id}: Acquired WRITE lock.");
            // Simulate writing
            int keyToWrite = _random.Next(1, 5);
            string valueToWrite = $"Data from writer {id}";
            _sharedData[keyToWrite] = valueToWrite;
            Console.WriteLine($"Writer {id}: Wrote '{valueToWrite}' to key {keyToWrite}.");
            Thread.Sleep(_random.Next(200, 500));
        }
        finally
        {
            _lock.ExitWriteLock(); // Release write lock
            Console.WriteLine($"Writer {id}: Released WRITE lock.");
        }
    }

     public static async Task Main()
     {
        Console.WriteLine("\nRunning ReaderWriterLockSlim Example...");
        var tasks = new List<Task>();

        // Start many readers and a few writers
        tasks.Add(Task.Run(() => Writer(100)));
        
        tasks.Add(Task.Run(() => Reader(10)));
        tasks.Add(Task.Run(() => Reader(11)));
        tasks.Add(Task.Run(() => Reader(12)));
        tasks.Add(Task.Run(() => Reader(13)));

        tasks.Add(Task.Run(() => Writer(101)));
       
        await Task.WhenAll(tasks);
        
        _lock.Dispose();
        Console.WriteLine("ReaderWriterLockSlim Example finished.");
     }
}
```

Output:
```
Running ReaderWriterLockSlim Example...
Reader 10: Acquired read lock.
Reader 11: Acquired read lock.
Reader 11: Read key 2, value: 'N/A'.
Reader 13: Acquired read lock.
Reader 13: Read key 1, value: 'N/A'.
Reader 10: Read key 2, value: 'N/A'.
Reader 13: Released read lock.
Reader 10: Released read lock.
Reader 11: Released read lock.
Writer 101: Acquired WRITE lock.
Writer 101: Wrote 'Data from writer 101' to key 2.
Writer 101: Released WRITE lock.
Writer 100: Acquired WRITE lock.
Writer 100: Wrote 'Data from writer 100' to key 2.
Writer 100: Released WRITE lock.
Reader 12: Acquired read lock.
Reader 12: Read key 4, value: 'N/A'.
Reader 12: Released read lock.
ReaderWriterLockSlim Example finished.

```

7. System.Threading.Interlocked

Provides static methods for performing simple atomic operations on variables (primarily integers and longs), often avoiding the need for heavier locks.

- Purpose: High-performance, lock-free atomic updates for simple counters or flags.
- Methods: Increment(ref int), Decrement(ref int), Add(ref int, int), CompareExchange(ref int, int, int), Exchange(ref int, int).


```C#
using System;
using System.Threading;
using System.Threading.Tasks;

public class InterlockedExample
{
    private static long _atomicCounter = 0;

    public static void AtomicIncrement()
    {
        for (int i = 0; i < 100000000; i++)
        {
            // Atomically increment the counter, must pass reference to the variable
            // so it can be changed
            Interlocked.Increment(ref _atomicCounter);
        }
    }

    public static void Main()
    {
        _atomicCounter = 0; // Reset
        Console.WriteLine("\nRunning Interlocked Example...");
        Task t1 = Task.Run(AtomicIncrement);
        Task t2 = Task.Run(AtomicIncrement);

        Task.WaitAll(t1, t2);

        Console.WriteLine($"Expected counter: 200000000");
        Console.WriteLine($"Actual counter:   {_atomicCounter}"); // Should be 2000000
        Console.WriteLine("Interlocked Example finished.");
    }
}
```

Output:

```
Running Interlocked Example...
Expected counter: 200000000
Actual counter:   200000000
Interlocked Example finished.
```

## Conclusion of the synchronization primitives

C# offers a comprehensive suite of synchronization primitives. Understanding these tools allows you to build robust and efficient concurrent applications in C#.  Choosing the right one depends on the specific need:

- Use lock for basic mutual exclusion.
- Use Monitor for explicit locking or condition variables.
- Use Mutex primarily for inter-process synchronization.
- Use SemaphoreSlim to limit concurrent access to resources.
- Use ReaderWriterLockSlim for read-heavy scenarios.
- Use Interlocked for simple atomic operations to avoid locking overhead.


## Thread Pools in C#

While C# has a threadPool feature, it is simpler keep track of threads using a list.  You can read about [Thread Pools Here](https://learn.microsoft.com/en-us/dotnet/api/system.threading.threadpool?view=net-9.0).

### Example 1: Simple List of Tasks

```C#
using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

public class TaskWaitAllExample
{
    public static void DoWork(int taskId, int durationMs)
    {
        Console.WriteLine($"Task {taskId} (Thread {Thread.CurrentThread.ManagedThreadId}): Starting work for {durationMs}ms...");
        Thread.Sleep(durationMs); // Simulate work
        Console.WriteLine($"Task {taskId} (Thread {Thread.CurrentThread.ManagedThreadId}): Finished work.");
    }

    public static void Main(string[] args)
    {
        int numberOfThreads = 5;
        Console.WriteLine($"Main thread: Starting {numberOfThreads} tasks using new Thread()...");

        List<Thread> runningThreads = new List<Thread>();
        Random random = new Random();

        for (int i = 1; i <= numberOfThreads; i++)
        {
            int id = i;
            int workDuration = random.Next(1000, 3001); // Random work time (1-3 seconds)

            Thread newThread = new Thread(() => DoWork(id, workDuration));
            runningThreads.Add(newThread);

            newThread.Start();
        }

        Console.WriteLine("Main thread: All threads launched. Waiting for completion using Thread.Join()...");

        foreach (Thread t in runningThreads)
        {
            t.Join();
        }

        Console.WriteLine("Main thread: All threads completed. Exiting.");
    }
}
```

Output:

```
Main thread: Starting 5 tasks using new Thread()...
Main thread: All threads launched. Waiting for completion using Thread.Join()...
Task 1 (Thread 9): Starting work for 1156ms...
Task 3 (Thread 11): Starting work for 2609ms...
Task 2 (Thread 10): Starting work for 2256ms...
Task 4 (Thread 12): Starting work for 2813ms...
Task 5 (Thread 13): Starting work for 2579ms...
Task 1 (Thread 9): Finished work.
Task 2 (Thread 10): Finished work.
Task 5 (Thread 13): Finished work.
Task 3 (Thread 11): Finished work.
Task 4 (Thread 12): Finished work.
Main thread: All threads completed. Exiting.
```

## Task Parallel Library (TPL)

The Task Parallel Library (TPL), primarily located in the `System.Threading.Tasks` namespace, represents .NET's modern, preferred approach for creating concurrent and parallel applications. It provides a higher level of abstraction over raw threads and the ThreadPool, simplifying common patterns, managing resources efficiently, and integrating seamlessly with features like async/await.

The central abstraction in TPL is the `System.Threading.Tasks.Task` (and its generic counterpart Task<TResult>). A Task represents an asynchronous operation. It's not necessarily a thread itself, but rather a unit of work that can be scheduled to run, often utilizing threads from the ThreadPool.

- **Task**: Represents an operation that does not return a value.

- **Task<TResult>**: Represents an operation that does return a value of type TResult.

### Creating and Running Tasks with Task.Run

The simplest and most common way to execute a CPU-bound operation on a background thread (using the ThreadPool) is Task.Run().

```C#
using System;
using System.Threading;
using System.Threading.Tasks;

public class TplBasicTaskRun
{
    public static void DoCpuBoundWork(string taskName)
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($"{taskName} (Thread {id}): Starting CPU work...");

        // Simulate intensive calculation
        long sum = 0;
        for (int i = 0; i < 1_000_000_000; i++)
        {
            sum += i % 10;
        }
        Console.WriteLine($"{taskName} (Thread {id}): Finished CPU work.");
    }

    public static void Main()
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($"Main thread {id}: Starting tasks using Task.Run...");

        Task task1 = Task.Run(() => DoCpuBoundWork("Task 1"));
        Task task2 = Task.Run(() => DoCpuBoundWork("Task 2"));

        Console.WriteLine($"Main thread {id}: Tasks started. Waiting for them to complete...");

        task1.Wait(); // Blocks until task1 is complete
        task2.Wait(); // Blocks until task2 is complete

        Console.WriteLine($"Main thread {id}: All tasks completed.");
    }
}
```

Output:

```
Main thread 1: Starting tasks using Task.Run...
Main thread 1: Tasks started. Waiting for them to complete...
Task 1 (Thread 4): Starting CPU work...
Task 2 (Thread 9): Starting CPU work...
Task 1 (Thread 4): Finished CPU work.
Task 2 (Thread 9): Finished CPU work.
Main thread 1: All tasks completed.
```

### Waiting for Tasks and Getting Results

TPL provides robust ways to wait for task completion and retrieve results, a significant improvement over direct ThreadPool usage.

- **task.Wait()**: Blocks the calling thread until the specific task completes. Avoid using this excessively on UI threads or in highly concurrent server code, as it can lead to deadlocks or reduced throughput.
- **Task.WaitAll(params Task[] tasks)**: Blocks until all tasks in the provided array complete.
- **Task.WaitAny(params Task[] tasks)**: Blocks until at least one task in the provided array completes.
- **task.Result (for Task<TResult>)**: Accesses the return value of a completed task. If the task has not yet completed when Result is accessed, the calling thread blocks until it does. Accessing Result also propagates exceptions that occurred within the task.

```C#
using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

public class TplWaitAndResult
{
    public static int CalculateSquare(int number)
    {
        Console.WriteLine($"Calculating square for {number} on thread {Thread.CurrentThread.ManagedThreadId}...");
        Thread.Sleep(500 + number * 100); // Simulate work
        
        int result = number * number;
        Console.WriteLine($"Calculation for {number} finished. Result: {result}");
        
        if (number % 4 == 0) 
            throw new ArgumentException($"Simulated error for {number}"); // Simulate errors

        return result;
    }

    public static void Main()
    {
        Console.WriteLine($"\nMain thread {Thread.CurrentThread.ManagedThreadId}: Starting multiple tasks with results...");
        List<Task<int>> tasks = new List<Task<int>>();

        // Create 5 tasks
        for (int i = 1; i <= 5; i++)
        {
            int num = i;
            tasks.Add(Task.Run(() => CalculateSquare(num)));
        }

        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: All tasks launched. Waiting with WaitAll...");

        try
        {
            // Wait for all tasks to complete
            Task.WaitAll(tasks.ToArray()); // Blocks main thread
            Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: All tasks completed successfully.");

            // Retrieve results (safe now because WaitAll completed)
            foreach (var task in tasks)
            {
                Console.WriteLine($"MAIN: Result from completed task: {task.Result}");
            }
        }
        catch (AggregateException ae) // WaitAll wraps exceptions
        {
            Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: One or more tasks failed.");
            foreach (var ex in ae.Flatten().InnerExceptions)
            {
                Console.WriteLine($" - Error: {ex.Message}");
            }
        }

         // Example of accessing .Result directly (can block and throw)
         Console.WriteLine("\nAccessing result directly for Task 3:");
         try
         {
             int result3 = tasks[2].Result;
             Console.WriteLine($"Result for Task 3: {result3}");
         }
         catch (AggregateException ae) { /* Handle potential exception from Task 3 if it failed */
              Console.WriteLine($"Error getting result 3: {ae.InnerException?.Message}");
         }

         Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Exiting.");
    }
}
```

Output:

```
Main thread 1: Starting multiple tasks with results...
Main thread 1: All tasks launched. Waiting with WaitAll...
Calculating square for 1 on thread 4...
Calculating square for 2 on thread 10...
Calculating square for 3 on thread 12...
Calculating square for 4 on thread 13...
Calculating square for 5 on thread 14...
Calculation for 1 finished. Result: 1
Calculation for 2 finished. Result: 4
Calculation for 3 finished. Result: 9
Calculation for 4 finished. Result: 16
Calculation for 5 finished. Result: 25
Main thread 1: One or more tasks failed.
 - Error: Simulated error for 4

Accessing result directly for Task 3:
Result for Task 3: 9
Main thread 1: Exiting.
```

### Task Continuations (ContinueWith)

Continuations allow you to specify code that should run automatically when a preceding task (the "antecedent") finishes.  While ContinueWith is powerful, the async/await keywords (covered next) provide a much more readable and natural way to handle asynchronous workflows and continuations in most cases.


```C#
using System;
using System.Threading;
using System.Threading.Tasks;

public class TplContinuation
{
    public static void Main()
    {
        Console.WriteLine($"\nMain thread {Thread.CurrentThread.ManagedThreadId}: Starting task with continuation...");

        // Lambda Function as a task
        Task<string> initialTask = Task.Run(() =>
        {
            Console.WriteLine($"Initial task (Thread {Thread.CurrentThread.ManagedThreadId}): Working...");
            Thread.Sleep(1000);
            return "Initial Result";
        });

        // Schedule a continuation task to run after initialTask completes
        Task continuationTask = initialTask.ContinueWith(antecedent =>
        {
            // 'antecedent' is the completed initialTask
            Console.WriteLine($"Continuation (Thread {Thread.CurrentThread.ManagedThreadId}): Started.");
            if (antecedent.IsFaulted)
            {
                Console.WriteLine($"Continuation: Antecedent task failed: {antecedent.Exception?.InnerException?.Message}");
            }
            else if (antecedent.IsCompletedSuccessfully)
            {
                Console.WriteLine($"Continuation: Antecedent task completed with result: '{antecedent.Result}'");
            }
            else if (antecedent.IsCanceled)
            {
                Console.WriteLine($"Continuation: Antecedent task was canceled.");
            }
        });

        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Initial task and continuation scheduled.");

        // Wait for the *continuation* task to finish for this demo
        continuationTask.Wait();

        Console.WriteLine($"Main thread {Thread.CurrentThread.ManagedThreadId}: Continuation finished.");
    }
}
```

Output:

```
Main thread 1: Starting task with continuation...
Main thread 1: Initial task and continuation scheduled.
Initial task (Thread 6): Working...
Continuation (Thread 6): Started.
Continuation: Antecedent task completed with result: 'Initial Result'
Main thread 1: Continuation finished.
```

### Data Parallelism (System.Threading.Tasks.Parallel Class)

TPL provides the static Parallel class to simplify common patterns where you perform the same operation on many different data items concurrently.

- **Parallel.For(fromInclusive, toExclusive, body)**: Executes a for loop where iterations can run in parallel.
- **Parallel.ForEach(source, body)**: Executes a foreach loop where processing of items in the source collection can run in parallel.

Important: Be very careful about thread safety when using Parallel.For or Parallel.ForEach. If the body delegate modifies shared variables outside its scope without proper locking or concurrent collections, you will introduce race conditions.

The default task scheduler used by TPL (e.g., for Task.Run, Parallel.For, Parallel.ForEach) typically uses the System.Threading.ThreadPool to execute the tasks. TPL intelligently manages how work is queued and executed on the pool, handling details like partitioning work and load balancing.


```C#
using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using System.Diagnostics; // For Stopwatch
using System.Linq; // For .ToList()

public class TplDataParallelism
{
    public static void ProcessItem(int item)
    {
        // Simulate work based on item value
        Thread.Sleep(item * 5);
    }

    public static void Main()
    {
        List<int> data = Enumerable.Range(1, 50).ToList(); // Create list 1..50
        Stopwatch stopwatch = new Stopwatch();

        Console.WriteLine($"\nRunning Data Parallelism Example (Processing {data.Count} items)...");

        // --- Sequential ForEach ---
        Console.WriteLine("\nSequential ForEach:");
        stopwatch.Restart();
        foreach (var item in data)
        {
            ProcessItem(item);
        }
        stopwatch.Stop();
        Console.WriteLine($"Sequential ForEach took: {stopwatch.ElapsedMilliseconds} ms");

        // --- Parallel.ForEach ---
        Console.WriteLine("\nParallel.ForEach:");
        stopwatch.Restart();
        Parallel.ForEach(data, item => // Body executed in parallel for items
        {
            // Console.WriteLine($"Processing item {item} on thread {Thread.CurrentThread.ManagedThreadId}");
            ProcessItem(item);
        });
        stopwatch.Stop();
        Console.WriteLine($"Parallel.ForEach took: {stopwatch.ElapsedMilliseconds} ms"); // Should be faster

        // --- Parallel.For ---
        Console.WriteLine("\nParallel.For:");
        stopwatch.Restart();
        Parallel.For(0, data.Count, index => // Body executed in parallel for index range
        {
            int item = data[index];
            // Console.WriteLine($"Processing index {index} (item {item}) on thread {Thread.CurrentThread.ManagedThreadId}");
            ProcessItem(item);
        });
        stopwatch.Stop();
        Console.WriteLine($"Parallel.For took: {stopwatch.ElapsedMilliseconds} ms"); // Should be faster

        Console.WriteLine("\nData Parallelism Example finished.");
    }
}
```

Output:

```
Running Data Parallelism Example (Processing 50 items)...

Sequential ForEach:
Sequential ForEach took: 6527 ms

Parallel.ForEach:
Parallel.ForEach took: 707 ms

Parallel.For:
Parallel.For took: 698 ms

Data Parallelism Example finished.
```

## Asynchronous Programming with async and await

Building upon the foundation laid by the Task Parallel Library (TPL), C# provides powerful language features – the async and await keywords – specifically designed to simplify writing asynchronous code. While TPL's Task object represents an asynchronous operation, async/await provides a much more readable and manageable syntax for working with these operations, especially for I/O-bound scenarios.  [See Documentation on async and await](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/)

The Problem with Blocking. Consider operations that don't heavily use the CPU but involve waiting for external resources:

- Network requests (calling web APIs, downloading files)
- Database queries
- File I/O (reading from or writing to disk)

If you perform these operations synchronously, the calling thread blocks – it sits idle, consuming resources (like memory for its stack) while waiting for the operation to complete. In a UI application, this freezes the user interface. In a server application (like ASP.NET Core), blocked threads cannot handle other incoming requests, severely limiting scalability.

Async and await work together to enable asynchronous operations without blocking the calling thread.

### async Modifier

- Applied to a method signature (e.g., public async Task MyMethodAsync()).
- Signals to the compiler that the method contains one or more await expressions.
- Enables the use of await within the method.
- Causes the method to return Task, Task<TResult>, or void (though async void is discouraged except for event handlers). The returned Task represents the ongoing execution of the async method.

### await Operator

- Can only be used inside a method marked async.
- Applied to an awaitable operation (most commonly a Task or Task<TResult>).

### Crucial Behavior

- If the awaited task has not yet completed, await does the following:
- It registers a continuation (callback) with the task.
- It returns control immediately to the caller of the async method. The current thread is not blocked and is free to do other work (like respond to UI events or handle other web requests).
- When the awaited task eventually completes, the continuation is scheduled to run, and execution resumes within the async method right after the await expression.
- If the awaited task has already completed when await is encountered, execution continues synchronously within the method without yielding control.
- If awaiting a Task<TResult>, await unwraps the task and returns the TResult value.
Return Types for async Methods

### async Task

- Use for asynchronous methods that perform an operation but don't return a value to the caller (analogous to a void synchronous method).
- async Task<TResult>: Use for asynchronous methods that compute and return a value of type TResult.

### async void

Primarily for event handlers (like button clicks in UI frameworks). Avoid using async void for other purposes because exceptions thrown from async void methods are harder to catch and can crash the application.

### How it Works

The compiler transforms an async method into a sophisticated state machine. When await yields control, the current state of the method is saved. When the awaited task completes, the runtime uses the continuation to restore the method's state and resume execution, potentially on a different thread (often a ThreadPool thread, managed by the Synchronization Context or Task Scheduler).

### Example Basic Async Operations

```C#
using System;
using System.Threading;
using System.Threading.Tasks;

public class AsyncAwaitBasic
{
    // Simulates an I/O-bound operation like a network call
    public static async Task<string> FetchDataAsync(string resource)
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($"   Fetching '{resource}' on thread {id}... (Starting delay)");

        await Task.Delay(TimeSpan.FromSeconds(2)); // Simulate network latency - DOES NOT block thread

        Console.WriteLine($"   Fetching '{resource}' on thread {id}... (Finished delay)");
        return $"Data from {resource}";
    }

    // An async method that calls another async method
    public static async Task ProcessDataAsync()
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($" ProcessDataAsync started on thread {id}.");

        // Call FetchDataAsync and await its completion.
        // Control returns to the caller (Main) while FetchDataAsync 'waits'.
        string result = await FetchDataAsync("RemoteServer");

        // Execution resumes here AFTER FetchDataAsync completes (potentially on a different thread)
        Console.WriteLine($" ProcessDataAsync resumed on thread {id}.");
        Console.WriteLine($" Received result: '{result}'");

        // Simulate some CPU work with the result
        await Task.Delay(500); // Simulate more async work

        Console.WriteLine($" ProcessDataAsync finished processing on thread {id}.");
    }

    // Use async Task Main for top-level await (C# 7.1+)
    public static async Task Main(string[] args) // Note 'async Task Main'
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($"Main thread {id}: Calling ProcessDataAsync...");

        Task processingTask = ProcessDataAsync(); // Start the async method

        Console.WriteLine($"Main thread {id}: ProcessDataAsync called, Main continues executing...");

        // Do other work while ProcessDataAsync is running...
        for(int i = 0; i < 3; i++) {
            Console.WriteLine($"Main thread {id}: Doing other work {i+1}/3...");
            await Task.Delay(300); // Using await here too, so Main doesn't block
        }

        Console.WriteLine($"Main thread {id}: Waiting for ProcessDataAsync to complete...");
        await processingTask; // Wait for the entire async operation initiated by ProcessDataAsync

        Console.WriteLine($"Main thread {id}: ProcessDataAsync completed. Exiting.");
    }
}
```

Output:

```
Main thread 1: Calling ProcessDataAsync...
 ProcessDataAsync started on thread 1.
   Fetching 'RemoteServer' on thread 1... (Starting delay)
Main thread 1: ProcessDataAsync called, Main continues executing...
Main thread 1: Doing other work 1/3...
Main thread 1: Doing other work 2/3...
Main thread 1: Doing other work 3/3...
Main thread 1: Waiting for ProcessDataAsync to complete...
   Fetching 'RemoteServer' on thread 1... (Finished delay)
 ProcessDataAsync resumed on thread 1.
 Received result: 'Data from RemoteServer'
 ProcessDataAsync finished processing on thread 1.
Main thread 1: ProcessDataAsync completed. Exiting.
```

## Concurrent Collections (System.Collections.Concurrent)

A common requirement in concurrent programming is to have multiple threads safely access and modify a shared collection (like a list, dictionary, queue, etc.) without causing race conditions or data corruption.

### The Problem with Standard Collections

Standard .NET collection classes like List<T>, Dictionary<TKey, TValue>, Queue<T>, and Stack<T> are not thread-safe for concurrent write operations (or scenarios involving reads concurrent with writes). If multiple threads attempt to modify these collections simultaneously without external locking, the internal state can become corrupted, leading to unpredictable behavior, incorrect data, or application crashes.

Example: The final count of unsafeList is likely NOT 1000 and exceptions might occur.

```C#
// Conceptual Example - DO NOT DO THIS without locking!
List<int> unsafeList = new List<int>();
Parallel.For(0, 1000, i => {
    unsafeList.Add(i); // Potential race condition! Multiple threads adding can corrupt the list's internal state.
});
```

While you can use manual locking (like the lock statement) around every access to a standard collection to make it thread-safe, this can be cumbersome, error-prone, and sometimes inefficient due to coarse-grained locking.

### Introducing System.Collections.Concurrent

The `System.Collections.Concurrent` namespace provides a set of collection classes specifically designed for safe and efficient use in multi-threaded scenarios. These collections handle all necessary internal synchronization, often using fine-grained locking or lock-free techniques for better performance compared to manually locking standard collections.

### ConcurrentQueue<T>

A thread-safe FIFO (First-In, First-Out) queue.

Use Case: 

Ideal for producer-consumer scenarios, work queues, or any situation where items need to be processed in the order they were added by multiple threads.

Key Methods

- **Enqueue(T item)**: Adds an item to the end of the queue.
- **TryDequeue(out T result)**: Attempts to remove and return the item at the beginning. Returns true if successful, false if the queue was empty.
- **TryPeek(out T result)**: Attempts to return the item at the beginning without removing it.
- **IsEmpty**: Gets a value indicating whether the queue is empty.

```C#
using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Threading;
using System.Linq; // For Enumerable.Range

public class ConcurrentQueueExample
{
    public static async Task Main()
    {
        ConcurrentQueue<int> queue = new ConcurrentQueue<int>();
        Console.WriteLine("\nRunning ConcurrentQueue Example...");

        // Producers
        var producers = Task.Run(() => {
            Parallel.For(0, 100, i => {
                queue.Enqueue(i);
                Thread.Sleep(10); // Simulate variability
            });
            Console.WriteLine($"--- Producer finished. Queue count approx: {queue.Count} ---");
        });

        // Consumers
        var consumers = Task.Run(() => {
            int itemsProcessed = 0;
            Parallel.For(0, 100, i => {
                if (queue.TryDequeue(out int item)) {
                    // Console.WriteLine($"Dequeued {item} on thread {Thread.CurrentThread.ManagedThreadId}");
                    Interlocked.Increment(ref itemsProcessed); // Safely count processed items
                    Thread.Sleep(15); // Simulate work
                } else {
                    Thread.Sleep(15); // Wait                    
                }
            });
            Console.WriteLine($"--- Consumer finished processing {itemsProcessed} items. Queue count approx: {queue.Count} ---");
        });

        await Task.WhenAll(producers, consumers);
        Console.WriteLine($"Final Queue size (approx): {queue.Count}");
        Console.WriteLine("ConcurrentQueue Example finished.");
    }
}
```

Output:
```
Running ConcurrentQueue Example...
--- Consumer finished processing 98 items. Queue count approx: 2 ---
--- Producer finished. Queue count approx: 2 ---
Final Queue size (approx): 2
ConcurrentQueue Example finished.
```

### ConcurrentStack<T>

A thread-safe LIFO (Last-In, First-Out) stack.

Use Case

Scenarios requiring LIFO semantics in a multi-threaded environment (less common than queues, but useful for tasks like backtracking or managing nested operations).

Key Methods
- **Push(T item)**: Adds an item to the top of the stack.
- **TryPop(out T result)**: Attempts to remove and return the item from the top.
- **TryPeek(out T result)**: Attempts to return the item at the top without removing it.
- **PushRange(T[])**, **TryPopRange(T[])**: Efficiently add/remove multiple items.

```C#
using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Threading;

public class ConcurrentStackExample
{
    public static async Task Main()
    {
        ConcurrentStack<int> stack = new ConcurrentStack<int>();
        Console.WriteLine("\nRunning ConcurrentStack Example...");

        // Push tasks
        var pushTasks = Task.Run(() => {
            Parallel.For(0, 50, i => {
                stack.Push(i);
                // Console.WriteLine($"Pushed {i} on thread {Thread.CurrentThread.ManagedThreadId}");
                Thread.Sleep(10);
            });
            Console.WriteLine($"--- Push finished. Stack count approx: {stack.Count} ---");
        });

        // Pop tasks (will likely get higher numbers first due to LIFO)
        var popTasks = Task.Run(() => {
            int itemsProcessed = 0;
            Parallel.For(0, 50, i => {
                if (stack.TryPop(out int item)) {
                    Console.WriteLine($"Popped {item} on thread {Thread.CurrentThread.ManagedThreadId}"); // Notice LIFO order
                    Interlocked.Increment(ref itemsProcessed);
                    Thread.Sleep(15);
                }
            });
            Console.WriteLine($"--- Pop finished processing {itemsProcessed} items. Stack count approx: {stack.Count} ---");
        });

        await Task.WhenAll(pushTasks, popTasks);
        Console.WriteLine($"Final Stack size (approx): {stack.Count}");
        Console.WriteLine("ConcurrentStack Example finished.");
    }
}
```

Output:
```
Running ConcurrentStack Example...
Popped 9 on thread 17
Popped 21 on thread 13
Popped 3 on thread 15
Popped 12 on thread 19
Popped 15 on thread 10
--- Pop finished processing 5 items. Stack count approx: 15 ---
--- Push finished. Stack count approx: 45 ---
Final Stack size (approx): 45
ConcurrentStack Example finished.
```

### ConcurrentBag<T>

A thread-safe, unordered collection of items. It's optimized for scenarios where the same thread might be both producing and consuming items, as it tries to keep items local to a thread for efficiency.

Use Case

Temporary storage of objects where order doesn't matter, object pooling, accumulating results from parallel tasks when the source thread might also be the one retrieving.

Key Methods
- **Add(T item)**: Adds an item to the bag.
- **TryTake(out T result)**: Attempts to remove and return any item from the bag (order is not guaranteed).
- **TryPeek(out T result)**: Attempts to return an item without removing it (order not guaranteed).
- **IsEmpty**: Gets a value indicating whether the bag is empty.


```C#
using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Threading;
using System.Linq;

public class ConcurrentBagExample
{
    public static async Task Main()
    {
        ConcurrentBag<int> bag = new ConcurrentBag<int>();
        Console.WriteLine("\nRunning ConcurrentBag Example...");

        // Add items in parallel
        var addTasks = Task.Run(() => {
            Parallel.For(0, 20, i => {
                bag.Add(i);
                // Console.WriteLine($"Added {i} on thread {Thread.CurrentThread.ManagedThreadId}");
                Thread.Sleep(20);
            });
            Console.WriteLine($"--- Adding finished. Bag count: {bag.Count} ---");
        });

        await addTasks; // Wait for adding to finish before trying to take

        // Take items in parallel
        var takeTasks = Task.Run(() => {
            int itemsTaken = 0;
            Console.WriteLine("Taking items (order not guaranteed):");
            Parallel.For(0, 20, i => {
                if (bag.TryTake(out int item)) {
                    Console.Write($"{item}, "); // Items likely appear out of order
                    Interlocked.Increment(ref itemsTaken);
                    Thread.Sleep(25);
                }
            });
            Console.WriteLine($"\n--- Taking finished processing {itemsTaken} items. Bag count: {bag.Count} ---");
        });


        await takeTasks;
        Console.WriteLine($"Final Bag size: {bag.Count}");
        Console.WriteLine("ConcurrentBag Example finished.");
    }
}
```

Output:
```
Running ConcurrentBag Example...
--- Adding finished. Bag count: 20 ---
Taking items (order not guaranteed):
9, 17, 16, 13, 18, 15, 14, 19, 8, 4, 3, 10, 5, 7, 12, 11, 0, 6, 1, 2, 
--- Taking finished processing 20 items. Bag count: 0 ---
Final Bag size: 0
ConcurrentBag Example finished.
```

### ConcurrentDictionary<TKey, TValue>

A thread-safe dictionary (key-value store). Multiple threads can read and write concurrently with high performance.

Use Case

Shared caches, lookup tables, state tracking in concurrent applications.


Key Methods (often atomic or near-atomic):
- `TryAdd(TKey key, TValue value)`: Attempts to add a key/value pair. Returns false if the key already exists.
- `TryGetValue(TKey key, out TValue value)`: Attempts to get the value associated with a key.
- `TryRemove(TKey key, out TValue value)`: Attempts to remove a key/value pair.
- `TryUpdate(TKey key, TValue newValue, TValue comparisonValue)`: Attempts to update the value only if the current value matches the comparisonValue.
- `AddOrUpdate(TKey key, TValue addValue, Func<TKey, TValue, TValue> updateValueFactory)`: Adds a key/value if the key doesn't exist, or updates the existing value using the factory function if it does.
- `GetOrAdd(TKey key, TValue value)` / `GetOrAdd(TKey key, Func<TKey, TValue> valueFactory)`: Gets the value if the key exists, or adds the new value/factory-generated value if it doesn't.


```C#
using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Threading;

public class ConcurrentDictionaryExample
{
    public static async Task Main()
    {
        ConcurrentDictionary<string, int> scores = new ConcurrentDictionary<string, int>();
        Console.WriteLine("\nRunning ConcurrentDictionary Example...");

        var tasks = new List<Task>();

        // Simulate multiple threads updating scores
        for (int i = 0; i < 5; i++)
        {
            tasks.Add(Task.Run(() => {
                Random rand = new Random(Thread.CurrentThread.ManagedThreadId + i); // Seed random per task
                for (int j = 0; j < 5; j++)
                {
                    string playerName = $"Player{rand.Next(1, 4)}"; // Player 1, 2, or 3
                    int points = rand.Next(1, 11); // Score 1-10

                    // Atomically add new player or update existing score
                    scores.AddOrUpdate(
                        playerName,      // Key
                        points,          // Value to add if key is new
                        (key, currentScore) => currentScore + points // Function to update existing value
                    );
                    Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId}: Updated {playerName} by {points}. New score approx: {scores.GetValueOrDefault(playerName)}");
                    Thread.Sleep(rand.Next(50, 150));
                }
            }));
        }

        await Task.WhenAll(tasks);

        Console.WriteLine("\n--- Final Scores ---");
        foreach (var kvp in scores.OrderBy(kv => kv.Key)) // Order for consistent output
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }
        Console.WriteLine("ConcurrentDictionary Example finished.");
    }
}
```

Output:
```
Running ConcurrentDictionary Example...
Thread 9: Updated Player1 by 10. New score approx: 10
Thread 10: Updated Player2 by 3. New score approx: 3
Thread 11: Updated Player1 by 6. New score approx: 16
Thread 12: Updated Player2 by 9. New score approx: 12
Thread 4: Updated Player2 by 5. New score approx: 17
Thread 4: Updated Player2 by 3. New score approx: 20
Thread 10: Updated Player3 by 10. New score approx: 10
Thread 9: Updated Player2 by 6. New score approx: 26
Thread 12: Updated Player1 by 9. New score approx: 25
Thread 11: Updated Player3 by 5. New score approx: 15
Thread 4: Updated Player3 by 10. New score approx: 25
Thread 10: Updated Player2 by 10. New score approx: 36
Thread 12: Updated Player2 by 10. New score approx: 46
Thread 4: Updated Player2 by 10. New score approx: 56
Thread 9: Updated Player1 by 5. New score approx: 30
Thread 11: Updated Player1 by 5. New score approx: 35
Thread 12: Updated Player2 by 9. New score approx: 65
Thread 4: Updated Player3 by 2. New score approx: 27
Thread 10: Updated Player3 by 4. New score approx: 31
Thread 9: Updated Player2 by 7. New score approx: 72
Thread 12: Updated Player1 by 4. New score approx: 39
Thread 10: Updated Player3 by 3. New score approx: 34
Thread 11: Updated Player1 by 1. New score approx: 40
Thread 9: Updated Player1 by 8. New score approx: 48
Thread 11: Updated Player2 by 8. New score approx: 80

--- Final Scores ---
Player1: 48
Player2: 80
Player3: 34
ConcurrentDictionary Example finished.
```

### BlockingCollection<T>

A wrapper class that provides blocking and bounding capabilities for concurrent collections (it uses ConcurrentQueue<T> by default). It's exceptionally useful for implementing producer-consumer patterns.

Use Case

The go-to class for robust producer-consumer scenarios.

Key Features:
- `Blocking`: Take() blocks if the collection is empty; Add() blocks if the collection is bounded and full.
- `Bounding`: Can be initialized with a maximum capacity.
- `Signaling Completion`: CompleteAdding() signals that no more items will be added.
- `Consuming Enumerable`: GetConsumingEnumerable() provides an IEnumerable<T> that blocks waiting for items and automatically completes when CompleteAdding() is called and the collection is empty.
- Methods: `Add(T)`, `Take()`, `TryAdd(T)`, `TryTake(out T)`, `CompleteAdding()`, `IsAddingCompleted`.


```C#
using System;
using System.Collections.Concurrent;
using System.Threading;
using System.Threading.Tasks;

public class BlockingCollectionExample
{
    // Bounded to 5 items. Uses ConcurrentQueue by default.
    static BlockingCollection<int> messages = new BlockingCollection<int>(5);

    public static void Producer()
    {
        Console.WriteLine("Producer: Starting...");
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine($"Producer: Adding item {i}. Current count: {messages.Count}");
            messages.Add(i); // Blocks if messages.Count == 5
            Console.WriteLine($"Producer: Added item {i}.");
            Thread.Sleep(TimeSpan.FromMilliseconds(100 * (i % 3 + 1))); // Varying production time
        }
        // Signal that production is finished
        messages.CompleteAdding();
        Console.WriteLine("Producer: Finished adding items and called CompleteAdding().");
    }

    public static void Consumer(string name)
    {
        Console.WriteLine($"Consumer {name}: Starting...");
        // GetConsumingEnumerable blocks until an item is available
        // or CompleteAdding is called and the queue is empty.
        foreach (var item in messages.GetConsumingEnumerable())
        {
            Console.WriteLine($"Consumer {name}: Processing item {item}. Current count: {messages.Count}");
            Thread.Sleep(TimeSpan.FromMilliseconds(300)); // Simulate processing time
        }
        Console.WriteLine($"Consumer {name}: Finished consuming (collection completed).");
    }

    public static async Task Main()
    {
        Console.WriteLine("\nRunning BlockingCollection Example (Producer-Consumer)...");

        Task producerTask = Task.Run(Producer);
        Task consumerTask1 = Task.Run(() => Consumer("C1"));
        Task consumerTask2 = Task.Run(() => Consumer("C2"));

        await Task.WhenAll(producerTask, consumerTask1, consumerTask2);

        messages.Dispose();
        Console.WriteLine("BlockingCollection Example finished.");
    }
}
```

Output:
```
Running BlockingCollection Example (Producer-Consumer)...
Producer: Starting...
Consumer C2: Starting...
Consumer C1: Starting...
Producer: Adding item 0. Current count: 0
Producer: Added item 0.
Consumer C2: Processing item 0. Current count: 0
Producer: Adding item 1. Current count: 0
Producer: Added item 1.
Consumer C1: Processing item 1. Current count: 0
Producer: Adding item 2. Current count: 0
Producer: Added item 2.
Consumer C2: Processing item 2. Current count: 0
Producer: Adding item 3. Current count: 0
Producer: Added item 3.
Consumer C1: Processing item 3. Current count: 0
Producer: Adding item 4. Current count: 0
Producer: Added item 4.
Consumer C2: Processing item 4. Current count: 0
Producer: Finished adding items and called CompleteAdding().
Consumer C1: Finished consuming (collection completed).
Consumer C2: Finished consuming (collection completed).
BlockingCollection Example finished.
```


Benefits of Concurrent Collections:

1. `Thread Safety`: Eliminates the need for manual locking around basic collection operations.
1. `Simplicity`: Makes concurrent code involving shared collections easier to write and reason about.
1. `Performance`: Often provide better performance than manual locking on standard collections due to optimized internal implementations (fine-grained locking, lock-free techniques).

Conclusion

When you need to share mutable collections between multiple threads in C#, the classes within the System.Collections.Concurrent namespace are almost always the best choice. They provide built-in thread safety and often optimized performance, simplifying your code and reducing the likelihood of concurrency bugs. BlockingCollection<T> is particularly powerful for implementing producer-consumer patterns.
