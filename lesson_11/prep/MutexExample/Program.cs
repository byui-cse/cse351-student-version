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
