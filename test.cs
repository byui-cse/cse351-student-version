using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;

namespace assignment11
{
    public class Assignment11
    {
        private const long START_NUMBER = 10_000_000_000;
        private const int RANGE_COUNT = 1_000_000;
        private static readonly Queue<long> NumberQueue = new Queue<long>();
        private static readonly object QueueLock = new object();
        private static readonly object ConsoleLock = new object();

        private static int PrimeCount = 0;
        private static int NumbersProcessed = 0;
        private static int ThreadCount = 10;
        private static bool AddingComplete = false;

        public static void Main(string[] args)
        {
            Console.WriteLine("Prime numbers found:");
            var stopwatch = Stopwatch.StartNew();

            // Start worker threads
            Thread[] workers = new Thread[ThreadCount];
            for (int i = 0; i < ThreadCount; i++)
            {
                workers[i] = new Thread(Worker);
                workers[i].Start();
            }

            // Producer thread: enqueue numbers
            for (long i = START_NUMBER; i < START_NUMBER + RANGE_COUNT; i++)
            {
                lock (QueueLock)
                {
                    NumberQueue.Enqueue(i);
                }
            }

            // Mark queue as complete
            AddingComplete = true;

            // Wait for all workers to complete
            foreach (Thread worker in workers)
            {
                worker.Join();
            }

            stopwatch.Stop();

            Console.WriteLine(); // new line after primes
            Console.WriteLine();
            Console.WriteLine($"Numbers processed = {RANGE_COUNT}");
            Console.WriteLine($"Primes found      = {PrimeCount}");
            Console.WriteLine($"Total time        = {stopwatch.Elapsed}");
        }

        private static void Worker()
        {
            while (true)
            {
                long number;

                lock (QueueLock)
                {
                    if (NumberQueue.Count > 0)
                    {
                        number = NumberQueue.Dequeue();
                    }
                    else
                    {
                        if (AddingComplete)
                            break;
                        else
                            continue;
                    }
                }

                if (IsPrime(number))
                {
                    Interlocked.Increment(ref PrimeCount);
                    lock (ConsoleLock)
                    {
                        Console.Write($"{number}, ");
                    }
                }
            }
        }

        private static bool IsPrime(long n)
        {
            if (n <= 3) return n > 1;
            if (n % 2 == 0 || n % 3 == 0) return false;

            for (long i = 5; i * i <= n; i += 6)
            {
                if (n % i == 0 || n % (i + 2) == 0)
                    return false;
            }
            return true;
        }
    }
}
