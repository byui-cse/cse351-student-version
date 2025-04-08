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
