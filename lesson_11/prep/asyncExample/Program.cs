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
