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
