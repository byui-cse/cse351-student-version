using System;
using System.Threading;
using System.Threading.Tasks;

public class ManualResetEventSlimExample
{
    private static ManualResetEventSlim _event = new ManualResetEventSlim(false); // Initially not signaled

    public static void WaitingThread()
    {
        Console.WriteLine("WaitingThread: Waiting for signal...");
        _event.Wait(); // Blocks until _event.Set() is called
        Console.WriteLine("WaitingThread: Signal received! Continuing work.");
        // ... do work after signal ...
        _event.Dispose(); // Clean up
    }

    public static void SignalingThread()
    {
        Console.WriteLine("SignalingThread: Performing work before signaling...");
        Thread.Sleep(2000); // Simulate work
        Console.WriteLine("SignalingThread: Setting signal!");
        _event.Set(); // Signal waiting threads
    }

    public static void Main()
    {
        Console.WriteLine("\nRunning ManualResetEventSlim Example...");
        Task waiter = Task.Run(WaitingThread);
        Task signaler = Task.Run(SignalingThread);

        Task.WaitAll(waiter, signaler);
        Console.WriteLine("ManualResetEventSlim Example finished.");
    }
}
