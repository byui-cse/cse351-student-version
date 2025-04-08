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
