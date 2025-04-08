using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Threading;
using System.Linq;

public class ConcurrentBagExample
{
    public static async Task Main()
    {
        ConcurrentBag<int> bag = new ConcurrentBag<int>();
        Console.WriteLine("\nRunning ConcurrentBag Example...");

        // Add items in parallel
        var addTasks = Task.Run(() => {
            Parallel.For(0, 20, i => {
                bag.Add(i);
                // Console.WriteLine($"Added {i} on thread {Thread.CurrentThread.ManagedThreadId}");
                Thread.Sleep(20);
            });
            Console.WriteLine($"--- Adding finished. Bag count: {bag.Count} ---");
        });

        await addTasks; // Wait for adding to finish before trying to take

        // Take items in parallel
        var takeTasks = Task.Run(() => {
            int itemsTaken = 0;
            Console.WriteLine("Taking items (order not guaranteed):");
            Parallel.For(0, 20, i => {
                if (bag.TryTake(out int item)) {
                    Console.Write($"{item}, "); // Items likely appear out of order
                    Interlocked.Increment(ref itemsTaken);
                    Thread.Sleep(25);
                }
            });
            Console.WriteLine($"\n--- Taking finished processing {itemsTaken} items. Bag count: {bag.Count} ---");
        });


        await takeTasks;
        Console.WriteLine($"Final Bag size: {bag.Count}");
        Console.WriteLine("ConcurrentBag Example finished.");
    }
}