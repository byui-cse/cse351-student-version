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
