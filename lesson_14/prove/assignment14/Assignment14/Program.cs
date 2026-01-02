/*
 * Course    : CSE 351
 * Assignment: 14
 */
using System;
using Assignment14;
using Newtonsoft.Json.Linq;

class Program
{
    public static async Task run_part(long startId, int generations, string title, Func<long, Tree, Task<bool>> func)
    {
        // var tree = new Tree(startId);

        var startData = await Solve.GetDataFromServerAsync($"{Solve.TopApiUrl}/start/{generations}");
        Console.WriteLine(startData);

        Logger.Write("\n");
        Logger.Write("".PadRight(45, '#'));
        Logger.Write(title + ": " + generations + " generations");
        Logger.Write("".PadRight(45, '#'));
        
        var timer = System.Diagnostics.Stopwatch.StartNew();
        var tree = new Tree(startId);
        await func(startId, tree);
        timer.Stop();
        double totalTime = timer.Elapsed.TotalSeconds;

        var serverData = await Solve.GetDataFromServerAsync($"{Solve.TopApiUrl}/end");
        Console.WriteLine(serverData);

        // tree.Display(log);
        Logger.Write("");
        Logger.Write($"total_time                  : {totalTime:F5}");
        Logger.Write($"Generations                 : {generations}");

        // double operationsPerSecond = (tree.GetPersonCount() + tree.GetFamilyCount()) / totalTime;
        // log.Write($"People & Families / second  : {operationsPerSecond:F5}");
        // log.Write("");

        Logger.Write("STATS        Retrieved | Server details");
        Logger.Write($"People  : {tree.PersonCount,12:N0} | {serverData["people"],14:N0}");
        Logger.Write($"Families: {tree.FamilyCount,12:N0} | {serverData["families"],14:N0}");
        Logger.Write($"API Calls                   : {serverData["api"]}");
        Logger.Write($"Max number of threads       : {serverData["threads"]}");
    }
    
    static async Task Main()
    {
        string logLocation = Environment.CurrentDirectory[ ..(Environment.CurrentDirectory.LastIndexOf("Assignment14", StringComparison.Ordinal) + 13)];
        Logger.Configure(minimumLevel: LogLevel.Debug, logToFile: true, filePath: $"{logLocation}assignment.log");
        
        var data = await Solve.GetDataFromServerAsync($"{Solve.TopApiUrl}");
        long start_id = (long)data["start_family_id"];
        
        try
        {
            // File.ReadLines reads the file line by line without loading it all into memory.
            foreach (string line in File.ReadLines("runs.txt"))
            {
                string[] parts = line.Split(',');

                // Ensure the line has at least two parts and that they are valid integers.
                if (parts.Length >= 2 && 
                    int.TryParse(parts[0], out int partToRun) && 
                    int.TryParse(parts[1], out int generations))
                {
                    // A switch statement is a clean alternative to if-elif chains.
                    switch (partToRun)
                    {
                        case 1:
                            await run_part(start_id, generations, "Depth First Search", Solve.DepthFS);
                            break;
                        case 2:
                            await run_part(start_id, generations, "Breadth First Search", Solve.BreadthFS);
                            break;
                    }
                }
                else
                {
                    Console.WriteLine($"Skipping invalid line: {line}");
                }
            }
        }
        catch (FileNotFoundException)
        {
            Console.Error.WriteLine("Error: runs.txt not found.");
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"An unexpected error occurred: {ex.Message}");
        }        
        
    }
}
