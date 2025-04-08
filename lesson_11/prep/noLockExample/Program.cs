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