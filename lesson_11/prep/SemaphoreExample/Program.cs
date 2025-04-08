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
