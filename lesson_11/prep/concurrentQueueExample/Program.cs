using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Threading;
using System.Linq; // For Enumerable.Range

public class ConcurrentQueueExample
{
    public static async Task Main()
    {
        ConcurrentQueue<int> queue = new ConcurrentQueue<int>();
        Console.WriteLine("\nRunning ConcurrentQueue Example...");

        // Producers
        var producers = Task.Run(() => {
            Parallel.For(0, 100, i => {
                queue.Enqueue(i);
                Thread.Sleep(10); // Simulate variability
            });
            Console.WriteLine($"--- Producer finished. Queue count approx: {queue.Count} ---");
        });

        // Consumers
        var consumers = Task.Run(() => {
            int itemsProcessed = 0;
            Parallel.For(0, 100, i => {
                if (queue.TryDequeue(out int item)) {
                    // Console.WriteLine($"Dequeued {item} on thread {Thread.CurrentThread.ManagedThreadId}");
                    Interlocked.Increment(ref itemsProcessed); // Safely count processed items
                    Thread.Sleep(15); // Simulate work
                } else {
                    Thread.Sleep(15); // Wait                    
                }
            });
            Console.WriteLine($"--- Consumer finished processing {itemsProcessed} items. Queue count approx: {queue.Count} ---");
        });

        await Task.WhenAll(producers, consumers);
        Console.WriteLine($"Final Queue size (approx): {queue.Count}");
        Console.WriteLine("ConcurrentQueue Example finished.");
    }
}
