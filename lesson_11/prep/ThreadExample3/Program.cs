namespace ThreadExample3;

public class LambdaThreading
{
    public static void Main()
    {
        var id = Thread.CurrentThread.ManagedThreadId;
        Console.WriteLine($"Main thread {id}: Creating worker thread using lambda.");

        string dataToPass = "Some Data";
        int iterations = 5;

        // Create thread using a lambda expression
        Thread workerThread = new Thread(() =>
        {
            var id = Thread.CurrentThread.ManagedThreadId;
            Console.WriteLine($"Thread name: {Thread.CurrentThread.Name}");
            Console.WriteLine($"Worker thread {id}: Started with data '{dataToPass}'.");
            for (int i = 0; i < iterations; i++)
            {
                Console.WriteLine($"Worker thread {id}: Working... ({i + 1}/{iterations})");
                Thread.Sleep(200);
            }
            Console.WriteLine($"Worker thread {id}: Finished.");
        });

        // Optionally name the thread for easier debugging
        workerThread.Name = "MyLambdaWorker";

        workerThread.Start();

        Console.WriteLine($"Main thread {id}: Worker thread '{workerThread.Name}' started. Waiting...");
        workerThread.Join();
        Console.WriteLine($"Main thread {id}: Exiting.");
    }
}