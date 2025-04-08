using System;
using System.Collections.Concurrent;
using System.Threading;
using System.Threading.Tasks;

public class BlockingCollectionExample
{
    // Bounded to 5 items. Uses ConcurrentQueue by default.
    static BlockingCollection<int> messages = new BlockingCollection<int>(5);

    public static void Producer()
    {
        Console.WriteLine("Producer: Starting...");
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine($"Producer: Adding item {i}. Current count: {messages.Count}");
            messages.Add(i); // Blocks if messages.Count == 5
            Console.WriteLine($"Producer: Added item {i}.");
            Thread.Sleep(TimeSpan.FromMilliseconds(100 * (i % 3 + 1))); // Varying production time
        }
        // Signal that production is finished
        messages.CompleteAdding();
        Console.WriteLine("Producer: Finished adding items and called CompleteAdding().");
    }

    public static void Consumer(string name)
    {
        Console.WriteLine($"Consumer {name}: Starting...");
        // GetConsumingEnumerable blocks until an item is available
        // or CompleteAdding is called and the queue is empty.
        foreach (var item in messages.GetConsumingEnumerable())
        {
            Console.WriteLine($"Consumer {name}: Processing item {item}. Current count: {messages.Count}");
            Thread.Sleep(TimeSpan.FromMilliseconds(300)); // Simulate processing time
        }
        Console.WriteLine($"Consumer {name}: Finished consuming (collection completed).");
    }

    public static async Task Main()
    {
        Console.WriteLine("\nRunning BlockingCollection Example (Producer-Consumer)...");

        Task producerTask = Task.Run(Producer);
        Task consumerTask1 = Task.Run(() => Consumer("C1"));
        Task consumerTask2 = Task.Run(() => Consumer("C2"));

        await Task.WhenAll(producerTask, consumerTask1, consumerTask2);

        messages.Dispose();
        Console.WriteLine("BlockingCollection Example finished.");
    }
}
