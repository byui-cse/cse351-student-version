namespace ThreadExample1;

public class BasicThreading
{
    public static void DoWork()
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($"Worker thread {id}: Starting work.");
        Thread.Sleep(1000); // Simulate work
        Console.WriteLine($"Worker thread {id}: Finished work.");
    }

    public static void Main() // Renamed Main for clarity
    {
        var id = Thread.CurrentThread.ManagedThreadId;

        Console.WriteLine($"Main thread {id}: Creating worker thread.");

        // Create a Thread object, passing the method to execute
        Thread workerThread = new Thread(DoWork);

        // Start the thread's execution
        workerThread.Start();

        Console.WriteLine($"Main thread {id}: Worker thread started. Waiting for it to finish...");

        // Wait for the worker thread to complete before the main thread continues
        workerThread.Join();

        Console.WriteLine($"Main thread {id}: Worker thread finished. Exiting.");
    }
}