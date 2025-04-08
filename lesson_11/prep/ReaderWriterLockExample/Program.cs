
using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

public class ReaderWriterLockSlimExample
{
    private static ReaderWriterLockSlim _lock = new ReaderWriterLockSlim();
    private static Dictionary<int, string> _sharedData = new Dictionary<int, string>();
    private static Random _random = new Random();
   
    public static void Reader(int id)
    {
        try
        {
            _lock.EnterReadLock(); // Acquire read lock
            Console.WriteLine($"Reader {id}: Acquired read lock.");
            // Simulate reading
            int keyToRead = _random.Next(1, 5);
            _sharedData.TryGetValue(keyToRead, out string value);
            Console.WriteLine($"Reader {id}: Read key {keyToRead}, value: '{value ?? "N/A"}'.");
            Thread.Sleep(_random.Next(50, 200));
        }
        finally
        {
            _lock.ExitReadLock(); // Release read lock
            Console.WriteLine($"Reader {id}: Released read lock.");
        }
    }

    public static void Writer(int id)
    {
        try
        {
            _lock.EnterWriteLock(); // Acquire write lock (exclusive)
            Console.WriteLine($"Writer {id}: Acquired WRITE lock.");
            // Simulate writing
            int keyToWrite = _random.Next(1, 5);
            string valueToWrite = $"Data from writer {id}";
            _sharedData[keyToWrite] = valueToWrite;
            Console.WriteLine($"Writer {id}: Wrote '{valueToWrite}' to key {keyToWrite}.");
            Thread.Sleep(_random.Next(200, 500));
        }
        finally
        {
            _lock.ExitWriteLock(); // Release write lock
            Console.WriteLine($"Writer {id}: Released WRITE lock.");
        }
    }

     public static async Task Main()
     {
        Console.WriteLine("\nRunning ReaderWriterLockSlim Example...");
        var tasks = new List<Task>();

        // Start many readers and a few writers
        tasks.Add(Task.Run(() => Writer(100)));
        
        tasks.Add(Task.Run(() => Reader(10)));
        tasks.Add(Task.Run(() => Reader(11)));
        tasks.Add(Task.Run(() => Reader(12)));
        tasks.Add(Task.Run(() => Reader(13)));

        tasks.Add(Task.Run(() => Writer(101)));
       
        await Task.WhenAll(tasks);
        
        _lock.Dispose();
        Console.WriteLine("ReaderWriterLockSlim Example finished.");
     }
}
