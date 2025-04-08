using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

public class TaskWaitAllExample
{
    public static void DoWork(int taskId, int durationMs)
    {
        Console.WriteLine($"Task {taskId} (Thread {Thread.CurrentThread.ManagedThreadId}): Starting work for {durationMs}ms...");
        Thread.Sleep(durationMs); // Simulate work
        Console.WriteLine($"Task {taskId} (Thread {Thread.CurrentThread.ManagedThreadId}): Finished work.");
    }

    public static void Main(string[] args)
    {
        int numberOfThreads = 5;
        Console.WriteLine($"Main thread: Starting {numberOfThreads} tasks using new Thread()...");

        List<Thread> runningThreads = new List<Thread>();
        Random random = new Random();

        for (int i = 1; i <= numberOfThreads; i++)
        {
            int id = i;
            int workDuration = random.Next(1000, 3001); // Random work time (1-3 seconds)

            Thread newThread = new Thread(() => DoWork(id, workDuration));
            runningThreads.Add(newThread);

            newThread.Start();
        }

        Console.WriteLine("Main thread: All threads launched. Waiting for completion using Thread.Join()...");

        foreach (Thread t in runningThreads)
        {
            t.Join();
        }

        Console.WriteLine("Main thread: All threads completed. Exiting.");
    }
}
