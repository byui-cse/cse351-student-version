# Lesson 9: Classic Concurrency Problems

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
9.1 | [Patterns](#Patterns)
9.2 | [The Producer-Consumer Problem](#The-Producer-Consumer-Problem)
9.3 | [The Readers-Writers Problem](#The-Readers-Writers-Problem)
9.4 | [The Dining Philosophers Problem](#The-Dining-Philosophers-Problem)
9.5 | [Monte Carlo Simulations](#Monte-Carlo-Simulations)
9.6 | [Other Classic Problems](#Other-Classic-Problems)


:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

9.1 Patterns
- Boss-Worker
- Bounded Buffer
- Client-Server Pattern

9.2 The Producer-Consumer Problem
Problem Definition and Scenarios
Solutions using Different Synchronization Primitives (Mutexes, Semaphores, Condition Variables)
Bounded Buffer Problem

9.3 The Readers-Writers Problem
Problem Definition (Multiple Readers, Exclusive Writer)
Solutions with Different Priorities (Reader Priority, Writer Priority)
Avoiding Starvation

9.4 The Dining Philosophers Problem
Problem Definition (Resource Contention, Deadlock Potential)
Solutions (Resource Ordering, Semaphores, Monitors)

9.5 Monte Carlo Simulations

9.6 Other Classic Problems
Sleeping Barber Problem
Cigarette Smokers Problem
The Search-Insert-Delete Problem
Bankers algorithm (deadlock prevention)
Elevator Simulation











### Topic 1


1. Boss-Worker Pattern

Concept:
The Boss-Worker pattern involves a "boss" thread that distributes tasks to multiple "worker" threads.
The boss thread is responsible for task creation and distribution, while worker threads perform the actual work.
This pattern is useful for parallelizing tasks that can be divided into independent subtasks.
Details:
Boss:
Creates and manages worker threads.
Divides the workload into smaller tasks.
Distributes tasks to available workers.
May collect and aggregate results from workers.
Workers:
Receive tasks from the boss.
Execute the tasks independently.
May return results to the boss.
Example (Conceptual C# using TPL):
C#

    using System;
    using System.Collections.Concurrent;
    using System.Threading.Tasks;

    public class BossWorkerExample
    {
        public static void RunExample(int numberOfTasks, int numberOfWorkers)
        {
            var tasks = new ConcurrentQueue<int>();
            for (int i = 0; i < numberOfTasks; i++)
            {
                tasks.Enqueue(i);
            }

            var workerTasks = new Task[numberOfWorkers];
            for (int i = 0; i < numberOfWorkers; i++)
            {
                workerTasks[i] = Task.Run(() => Worker(tasks));
            }

            Task.WaitAll(workerTasks);
            Console.WriteLine("All tasks completed.");
        }

        private static void Worker(ConcurrentQueue<int> tasks)
        {
            while (tasks.TryDequeue(out int task))
            {
                // Simulate work
                Console.WriteLine($"Worker {Task.CurrentId} processing task {task}");
                Task.Delay(100).Wait(); // Simulate delay
            }
        }
    }
2. Producer-Consumer Pattern

Concept:
The Producer-Consumer pattern involves one or more "producer" threads that generate data and one or more "consumer" threads that process that data.
A shared buffer is used to hold the data between producers and consumers.
This pattern is useful for decoupling data generation from data processing.
Details:
Producers:
Generate data.
Place data into the shared buffer.
Signal consumers when data is available.
Consumers:
Retrieve data from the shared buffer.
Process the data.
Signal producers when buffer space is available.
Example (Conceptual C# using ConcurrentQueue):
C#

    using System;
    using System.Collections.Concurrent;
    using System.Threading;
    using System.Threading.Tasks;

    public class ProducerConsumerExample
    {
        public static void RunExample()
        {
            var buffer = new ConcurrentQueue<int>();
            var cts = new CancellationTokenSource();

            Task.Run(() => Producer(buffer, cts.Token));
            Task.Run(() => Consumer(buffer, cts.Token));

            Console.ReadKey(); // Press any key to stop
            cts.Cancel();
            Task.Delay(100).Wait(); // Give time to shutdown.
        }

        private static void Producer(ConcurrentQueue<int> buffer, CancellationToken token)
        {
            int i = 0;
            while (!token.IsCancellationRequested)
            {
                buffer.Enqueue(i++);
                Console.WriteLine($"Produced: {i - 1}");
                Task.Delay(50).Wait();
            }
        }

        private static void Consumer(ConcurrentQueue<int> buffer, CancellationToken token)
        {
            while (!token.IsCancellationRequested)
            {
                if (buffer.TryDequeue(out int item))
                {
                    Console.WriteLine($"Consumed: {item}");
                    Task.Delay(100).Wait();
                }
            }
        }
    }
3. Bounded Buffer

Concept:
A Bounded Buffer is a variation of the Producer-Consumer pattern where the shared buffer has a fixed size.
Producers wait if the buffer is full, and consumers wait if the buffer is empty.
This pattern is used to control the rate of data production and consumption.
Details:
Implements a fixed-size buffer.
Uses synchronization mechanisms (e.g., semaphores) to manage buffer access.
Producers block when the buffer is full.
Consumers block when the buffer is empty.
Example (Conceptual C# using SemaphoreSlim):
C#

    using System;
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;

    public class BoundedBufferExample
    {
        public static void RunExample()
        {
            var buffer = new List<int>(5); // Buffer of size 5
            var empty = new SemaphoreSlim(5, 5); // Initially 5 empty slots
            var full = new SemaphoreSlim(0, 5); // Initially 0 full slots

            Task.Run(() => Producer(buffer, empty, full));
            Task.Run(() => Consumer(buffer, empty, full));

            Console.ReadKey();
        }

        private static void Producer(List<int> buffer, SemaphoreSlim empty, SemaphoreSlim full)
        {
            for (int i = 0; ; i++)
            {
                empty.Wait();
                lock (buffer) { buffer.Add(i); }
                full.Release();
                Console.WriteLine($"Produced: {i}");
                Task.Delay(100).Wait();
            }
        }

        private static void Consumer(List<int> buffer, SemaphoreSlim empty, SemaphoreSlim full)
        {
            while (true)
            {
                full.Wait();
                int item;
                lock (buffer) { item = buffer[0]; buffer.RemoveAt(0); }
                empty.Release();
                Console.WriteLine($"Consumed: {item}");
                Task.Delay(200).Wait();
            }
        }
    }
4. Client-Server Pattern

Concept:
The Client-Server pattern involves a "server" that provides services to multiple "clients."
Clients send requests to the server, and the server processes the requests and sends responses back to the clients.
This pattern is fundamental to network applications.
Details:
Server:
Listens for client connections.
Accepts client requests.
Processes requests concurrently (using threads or tasks).
Sends responses to clients.
Clients:
Connect to the server.
Send requests to the server.
Receive responses from the server.
Example (Conceptual C# using TcpListener and Tasks):
C#

    using System;
    using System.Net;
    using System.Net.Sockets;
    using System.Text;
    using System.Threading.Tasks;

    public class ClientServerExample
    {
        public static void RunExample()
        {
            Task.Run(() => Server());
            Task.Run(() => Client());
            Task.Delay(500).Wait();
            Task.Run(() => Client());
            Console.ReadKey();
        }

        private static async Task Server()
        {
            TcpListener listener = new TcpListener(IPAddress.Any, 5000);
            listener.Start();
            while (true)
            {
                TcpClient client = await listener.AcceptTcpClientAsync();
                Task.Run(() => HandleClient(client));
            }
        }

        private static async Task HandleClient(TcpClient client)
        {
            NetworkStream stream = client.GetStream();
            byte[] buffer = new byte[1024];
            int bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length);
            string request = Encoding.ASCII.GetString(buffer, 0, bytesRead);
            Console.WriteLine($"Server received: {request}");

            string response = $"Server response to: {request}";
            byte[] responseBytes = Encoding.ASCII.GetBytes(response);
            await stream.WriteAsync(responseBytes, 0, responseBytes.Length);
            client.Close();
        }

        private static async Task Client()
        {
            TcpClient client = new TcpClient();
            await client.ConnectAsync("127.0.0.1", 5000);





. Reader-Writer Problem

Concept:
The Reader-Writer problem involves managing concurrent access to a shared resource, where multiple readers can access the resource simultaneously, but writers require exclusive access.
The challenge is to allow concurrent reads while preventing data corruption when a writer modifies the resource.
Details:
Readers: Can access the resource concurrently as long as no writer is active.
Writers: Need exclusive access to modify the resource.
Potential Issues:
Starvation: Writers may be starved if there is a continuous stream of readers.
Deadlocks: If readers and writers acquire locks in different orders, deadlocks can occur.
Solution (C# using ReaderWriterLockSlim):
C#

    using System;
    using System.Threading;
    using System.Threading.Tasks;

    public class ReaderWriterExample
    {
        private ReaderWriterLockSlim rwLock = new ReaderWriterLockSlim();
        private int sharedData = 0;

        public void Reader()
        {
            while (true)
            {
                rwLock.EnterReadLock();
                Console.WriteLine($"Reader {Task.CurrentId} reads: {sharedData}");
                rwLock.ExitReadLock();
                Task.Delay(100).Wait();
            }
        }

        public void Writer()
        {
            while (true)
            {
                rwLock.EnterWriteLock();
                sharedData++;
                Console.WriteLine($"Writer {Task.CurrentId} writes: {sharedData}");
                rwLock.ExitWriteLock();
                Task.Delay(500).Wait();
            }
        }
    }
2. Dining Philosophers Problem

Concept:
The Dining Philosophers problem illustrates a classic synchronization issue where multiple philosophers sit around a table with a single chopstick between each pair.
Each philosopher needs two chopsticks to eat, but they can only pick up one chopstick at a time.
The challenge is to prevent deadlocks where each philosopher holds one chopstick and waits indefinitely for the other.
Details:
Philosophers: Need two chopsticks (resources) to eat.
Chopsticks: Shared resources that can only be used by one philosopher at a time.
Potential Issue: Deadlock if all philosophers pick up their left chopstick simultaneously.
Solution (C# using SemaphoreSlim):
C#

    using System;
    using System.Threading;
    using System.Threading.Tasks;

    public class DiningPhilosophersExample
    {
        private SemaphoreSlim chopsticks;

        public DiningPhilosophersExample(int numPhilosophers)
        {
            chopsticks = new SemaphoreSlim[numPhilosophers];
            for (int i = 0; i < numPhilosophers; i++)
            {
                chopsticks[i] = new SemaphoreSlim(1, 1);
            }
        }

        public async Task Philosopher(int id)
        {
            while (true)
            {
                Console.WriteLine($"Philosopher {id} is thinking.");
                await Task.Delay(1000);

                // Acquire chopsticks (preventing deadlock with ordered acquisition)
                int leftChopstick = id;
                int rightChopstick = (id + 1) % chopsticks.Length;
                await chopsticks[Math.Min(leftChopstick, rightChopstick)].WaitAsync();
                await chopsticks[Math.Max(leftChopstick, rightChopstick)].WaitAsync();

                Console.WriteLine($"Philosopher {id} is eating.");
                await Task.Delay(500);

                chopsticks[leftChopstick].Release();
                chopsticks[rightChopstick].Release();
            }
        }
    }
3. Sleeping Barber Problem

Concept:
The Sleeping Barber problem models a barber shop with a single barber and a limited number of waiting chairs.
The barber sleeps when there are no customers, and customers leave if there are no available chairs.
The challenge is to ensure that the barber and customers coordinate properly to avoid race conditions and deadlocks.
Details:
Barber: Sleeps when there are no customers, wakes up when a customer arrives.
Customers: Enter the shop if there is an available chair, otherwise leave.
Waiting Chairs: Limited number of chairs for waiting customers.
Potential Issues:
Race Condition: Multiple customers might try to wake up the barber simultaneously.
Deadlock: The barber might be waiting for a customer while a customer is waiting for the barber.
Solution (C# using SemaphoreSlim and a Queue):
C#

    using System;
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;

    public class SleepingBarberExample
    {
        private SemaphoreSlim waitingChairs;
        private SemaphoreSlim barberReady = new SemaphoreSlim(0, 1);
        private SemaphoreSlim customerReady = new SemaphoreSlim(0, 1);
        private Queue<TaskCompletionSource<bool>> customerQueue = new Queue<TaskCompletionSource<bool>>();

        public SleepingBarberExample(int numChairs)
        {
            waitingChairs = new SemaphoreSlim(numChairs, numChairs);
        }

        public async Task Barber()
        {
            while (true)
            {
                await customerReady.WaitAsync(); // Wait for a customer
                TaskCompletionSource<bool> customerTask = null;
                lock (customerQueue)
                {
                    if (customerQueue.Count > 0)
                        customerTask = customerQueue.Dequeue();
                }
                if (customerTask!= null)
                {
                    Console.WriteLine("Barber is cutting hair.");
                    await Task.Delay(1000); // Simulate haircut
                    customerTask.SetResult(true); // Signal haircut completion
                }
                barberReady.Release(); // Barber is ready again
            }
        }

        public async Task<bool> Customer()
        {
            if (await waitingChairs.WaitAsync(0)) // Try to get a chair
            {
                var taskCompletion = new TaskCompletionSource<bool>();
                lock (customerQueue)
                {
                    customerQueue.Enqueue(taskCompletion);
                }
                customerReady.Release(); // Signal customer arrival
                await barberReady.WaitAsync(); // Wait for barber to be ready
                waitingChairs.Release(); // Release the chair
                return await taskCompletion.Task; // Wait for haircut completion
            }
            else
            {
                Console.WriteLine("No chairs available. Customer leaves.");
                return false;
            }
        }
    }


1. Elevator Simulation

Concept:
Simulate the behavior of an elevator system with multiple elevators, floors, and passengers.
The simulation should handle passenger requests, elevator movement, and floor selection.
This problem demonstrates concurrent process interactions and resource management.
Details:
Elevators: Move between floors, have capacity limits, and door open/close mechanisms.
Floors: Passengers request elevators from floors, and elevators arrive at floors.
Passengers: Generate requests with source and destination floors.
Challenges:
Coordinating elevator movement to minimize waiting time and travel distance.
Handling concurrent passenger requests efficiently.
Avoiding collisions and deadlocks.
Example (Conceptual C# using Tasks and Queues):
C#

    using System;
    using System.Collections.Concurrent;
    using System.Threading.Tasks;

    public class ElevatorSimulation
    {
        private ConcurrentQueue<PassengerRequest> requests = new ConcurrentQueue<PassengerRequest>();
        private Elevator elevators;

        public ElevatorSimulation(int numElevators, int numFloors)
        {
            elevators = new Elevator[numElevators];
            for (int i = 0; i < numElevators; i++)
            {
                elevators[i] = new Elevator(i, numFloors);
                Task.Run(() => elevators[i].Run(requests));
            }
        }

        public void AddRequest(PassengerRequest request)
        {
            requests.Enqueue(request);
        }

        //... (Elevator and PassengerRequest classes with logic for movement, etc.)
    }
2. Cigarette Smokers Problem

Concept:
The Cigarette Smokers problem is a classic concurrency problem that illustrates synchronization challenges.
Three smokers have different resources (tobacco, paper, matches), and an agent provides two of the three resources at a time.
Each smoker needs all three resources to make a cigarette, but they can only acquire the resources provided by the agent.
The challenge is to synchronize the smokers and the agent to avoid deadlocks and ensure progress.
Details:
Smokers: Each smoker has one of the three resources and needs the other two.
Agent: Randomly provides two of the three resources.
Challenges:
Ensuring that only one smoker can acquire the necessary resources at a time.
Preventing deadlocks where smokers wait indefinitely for the missing resource.
Example (Conceptual C# using Semaphores and Tasks):
C#

    using System;
    using System.Threading;
    using System.Threading.Tasks;

    public class CigaretteSmokers
    {
        private Semaphore tobacco = new Semaphore(0, 1);
        private Semaphore paper = new Semaphore(0, 1);
        private Semaphore matches = new Semaphore(0, 1);
        private Semaphore agent = new Semaphore(1, 1);

        public async Task SmokerWithTobacco()
        {
            while (true)
            {
                await paper.WaitAsync();
                await matches.WaitAsync();
                Console.WriteLine("Smoker with tobacco makes a cigarette.");
                agent.Release();
            }
        }

        //... (Similar tasks for SmokerWithPaper and SmokerWithMatches)

        public async Task Agent()
        {
            while (true)
            {
                await agent.WaitAsync();
                Random random = new Random();
                int choice = random.Next(3);
                if (choice == 0)
                {
                    paper.Release();
                    matches.Release();
                }
                else if (choice == 1)
                {
                    tobacco.Release();
                    matches.Release();
                }
                else
                {
                    tobacco.Release();
                    paper.Release();
                }
            }
        }
    }
3. Monte Carlo Simulations

Concept:
Monte Carlo simulations use random sampling to estimate numerical results.
These simulations are often used in finance, physics, and engineering.
Parallelizing Monte Carlo simulations can significantly improve performance.
Details:
Random Number Generation: Generate a large number of random samples.
Computation: Perform calculations on each sample.
Aggregation: Aggregate the results from all samples.
Challenges:
Ensuring that random number generation is thread-safe.
Efficiently distributing the workload across multiple threads or tasks.
Example (Conceptual C# using Parallel.For):
C#

    using System;
    using System.Threading.Tasks;

    public class MonteCarloSimulation
    {
        public double CalculatePi(int numSamples)
        {
            int numInsideCircle = 0;
            Parallel.For(0, numSamples, i =>
            {
                Random random = new Random();
                double x = random.NextDouble();
                double y = random.NextDouble();
                if (x * x + y * y <= 1)
                {
                    Interlocked.Increment(ref numInsideCircle);
                }
            });
            return 4.0 * numInsideCircle / numSamples;
        }
    }
    








































# Lesson 9: Review of C#, Threads

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
1   | [Course Introduction](#topic-1)
2   | [I/O Bound vs. CPU Bound](#topic-2) :key:

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
Concepts:
Thread creation and management.
Thread synchronization basics.
Thread safety.


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


Additional Notes:
Include practical coding examples and exercises for each topic.
Emphasize the differences and similarities between C# and Python concurrency.
Provide hands-on experience with the IDE (e.g., Visual Studio).
Encourage students to experiment with different threading and asynchronous patterns.
Consider including a small project that involves creating a multi-threaded or asynchronous application.