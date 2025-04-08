using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Threading;

public class ConcurrentDictionaryExample
{
    public static async Task Main()
    {
        ConcurrentDictionary<string, int> scores = new ConcurrentDictionary<string, int>();
        Console.WriteLine("\nRunning ConcurrentDictionary Example...");

        var tasks = new List<Task>();

        // Simulate multiple threads updating scores
        for (int i = 0; i < 5; i++)
        {
            tasks.Add(Task.Run(() => {
                Random rand = new Random(Thread.CurrentThread.ManagedThreadId + i); // Seed random per task
                for (int j = 0; j < 5; j++)
                {
                    string playerName = $"Player{rand.Next(1, 4)}"; // Player 1, 2, or 3
                    int points = rand.Next(1, 11); // Score 1-10

                    // Atomically add new player or update existing score
                    scores.AddOrUpdate(
                        playerName,      // Key
                        points,          // Value to add if key is new
                        (key, currentScore) => currentScore + points // Function to update existing value
                    );
                    Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId}: Updated {playerName} by {points}. New score approx: {scores.GetValueOrDefault(playerName)}");
                    Thread.Sleep(rand.Next(50, 150));
                }
            }));
        }

        await Task.WhenAll(tasks);

        Console.WriteLine("\n--- Final Scores ---");
        foreach (var kvp in scores.OrderBy(kv => kv.Key)) // Order for consistent output
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }
        Console.WriteLine("ConcurrentDictionary Example finished.");
    }
}