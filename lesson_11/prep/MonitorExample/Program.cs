using System;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;

public class MonitorExample // Basic Producer-Consumer Signal
{
    private static readonly object _lockObject = new object();
    private static Queue<int> _queue = new Queue<int>();
    private static bool _producingFinished = false;

    public static void Producer()
    {
        for (int i = 0; i < 5; i++)
        {
            lock (_lockObject)
            {
                _queue.Enqueue(i);
                Console.WriteLine($"Producer added {i}, queue size: {_queue.Count}");
                // Pulse signals ONE waiting thread (if any)
                Monitor.Pulse(_lockObject);
            }
            Thread.Sleep(100); // Simulate production time
        }
        lock(_lockObject) {
             _producingFinished = true;
             Monitor.PulseAll(_lockObject); // Wake all consumers to check finished flag
        }
        Console.WriteLine("Producer finished.");
    }

    public static void Consumer(string name)
    {
        while (true)
        {
            int item = -1; // Default value
            lock (_lockObject)
            {
                // Wait while the queue is empty AND production isn't finished
                while (_queue.Count == 0 && !_producingFinished)
                {
                    Console.WriteLine($"{name}: Queue empty, waiting...");
                    Monitor.Wait(_lockObject); // Releases lock and waits for Pulse/PulseAll
                    // Reacquires lock upon waking
                }

                if (_queue.Count > 0) {
                    item = _queue.Dequeue();
                } else if (_producingFinished) {
                    // Queue is empty and producer is done
                    Console.WriteLine($"{name}: No more items, exiting.");
                    break; // Exit the loop
                }
            } // Lock released here

            if (item != -1) {
                 Console.WriteLine($"{name}: Consumed {item}");
                 Thread.Sleep(200); // Simulate consumption time
            }
        }
    }

    public static void Main()
    {
        _queue.Clear();
        _producingFinished = false;
        Console.WriteLine("\nRunning Monitor Example (Producer-Consumer)...");

        Task producerTask = Task.Run(Producer);
        Task consumerTask1 = Task.Run(() => Consumer("Consumer 1"));
        Task consumerTask2 = Task.Run(() => Consumer("Consumer 2"));

        Task.WaitAll(producerTask, consumerTask1, consumerTask2);
        Console.WriteLine("Monitor Example finished.");
    }
}
