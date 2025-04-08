namespace ThreadExample2;

public class ParameterizedThreading
{
    public static void DoWorkWithParameter(object data)
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        // Parameter is always object, needs casting
        if (data is string message) // Use pattern matching for safe casting
        {
            Console.WriteLine($"Worker thread {id}: Received '{message}'. Starting work.");
            Thread.Sleep(1500); // Simulate work
            Console.WriteLine($"Worker thread {id}: Finished work with '{message}'.");
        }
        else
        {
            Console.WriteLine($"Worker thread {id}: Received invalid data type.");
        }
    }

    public static void Main()
    {
        var id = Thread.CurrentThread.ManagedThreadId;

        Console.WriteLine($"Main thread {id}: Creating parameterized worker thread.");

        Thread workerThread = new Thread(DoWorkWithParameter);

        string messageToSend = "Hello from Main!";

        // Start the thread and pass data via the Start method
        workerThread.Start(messageToSend); // The argument here is passed as 'object'

        Console.WriteLine($"Main thread {id}: Worker thread started. Waiting...");
        workerThread.Join();
        Console.WriteLine($"Main thread {id}: Exiting.");
    }
}