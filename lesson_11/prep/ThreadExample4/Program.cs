namespace ThreadExample4;

public class BackgroundThreading
{
    public static void BackgroundWorker()
    {
        Console.WriteLine("Background thread: Starting work...");
        Thread.Sleep(3000); // Simulate long work
        Console.WriteLine("Background thread: Finishing work.");
    }

    public static void Main()
    {
        Console.WriteLine("Main thread: Creating background worker.");
        Thread worker = new Thread(BackgroundWorker);

        // Set the thread to be a background thread
        worker.IsBackground = true;

        worker.Start();

        Console.WriteLine("Main thread: Background worker started. Main thread is exiting NOW.");
        // Note: We DO NOT call worker.Join() here.
        // Because the worker is a background thread, the application
        // will exit immediately after this line, potentially terminating
        // the background thread before it finishes its Sleep.
    }
}