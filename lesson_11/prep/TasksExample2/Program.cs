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
