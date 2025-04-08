using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Threading;

public class ConcurrentStackExample
{
    public static async Task Main()
    {
        ConcurrentStack<int> stack = new ConcurrentStack<int>();
        Console.WriteLine("\nRunning ConcurrentStack Example...");

        // Push tasks
        var pushTasks = Task.Run(() => {
            Parallel.For(0, 50, i => {
                stack.Push(i);
                // Console.WriteLine($"Pushed {i} on thread {Thread.CurrentThread.ManagedThreadId}");
                Thread.Sleep(10);
            });
            Console.WriteLine($"--- Push finished. Stack count approx: {stack.Count} ---");
        });

        // Pop tasks (will likely get higher numbers first due to LIFO)
        var popTasks = Task.Run(() => {
            int itemsProcessed = 0;
            Parallel.For(0, 50, i => {
                if (stack.TryPop(out int item)) {
                    Console.WriteLine($"Popped {item} on thread {Thread.CurrentThread.ManagedThreadId}"); // Notice LIFO order
                    Interlocked.Increment(ref itemsProcessed);
                    Thread.Sleep(15);
                }
            });
            Console.WriteLine($"--- Pop finished processing {itemsProcessed} items. Stack count approx: {stack.Count} ---");
        });

        await Task.WhenAll(pushTasks, popTasks);
        Console.WriteLine($"Final Stack size (approx): {stack.Count}");
        Console.WriteLine("ConcurrentStack Example finished.");
    }
}
