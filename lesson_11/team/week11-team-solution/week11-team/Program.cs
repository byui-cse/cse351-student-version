/*
 * Course: CSE 3541
 * Week  : 11
 *
 * - You need to run the server in Python for this program first
 * 
 * Goal: (Look for to do comments)
 * 1) install package Newtonsoft.Json.Linq for this project.
 *    - very easy to do in Rider (right click on the error)
 *    - for VSCode, do search for instructions (ie., "how to install Newtonsoft.Json.Linq in dotnet")
 * 2) Make the program faster
 * 3) Add an int to count the number of calls to the server.
 *
 * Hint
 * - look at the documentation of the method Select() for lists, also Task.WhenAll()
 * - https://www.dotnetperls.com/select
 * - https://www.csharptutorial.net/csharp-linq/linq-select/
 */

using System;
using System.Diagnostics;
using Newtonsoft.Json.Linq;

class Program
{
    private static readonly HttpClient HttpClient = new();
    private const string TopApiUrl = "http://127.0.0.1:8790";
    private static int callCount = 0;
    
    // Makes one URL call to the server
    private static async Task<JObject?> GetDataFromServerAsync(string url)
    {
        try
        {
            // TODO - increment calls to the server int
            Interlocked.Increment(ref callCount);
            var jsonString = await HttpClient.GetStringAsync(url);
            return JObject.Parse(jsonString);
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error fetching data from {url}: {e.Message}");
            return null;
        }
    }    
    
    // Retrieves all urls from a list of urls
    private static async Task GetUrlsAsync(JObject filmData, string kind)
    {
        // Safely get the list of URLs for the given category (e.g., "characters").
        var urls = filmData[kind]?.ToObject<List<string>>();
        if (urls == null || !urls.Any())
            return;

        Console.WriteLine(kind.ToUpper());

        Console.WriteLine($"  Number of urls = {urls.Count}");
        
        // Use Select() to process all urls in the list at once
        // This works because we are using async for the lambda function
        var tasks = urls.Select(async url =>
        {
            var item = await GetDataFromServerAsync(url);
            if (item != null)
            {
                // Print the name or title from the returned object.
                var name = item["name"] ?? item["title"];
                Console.WriteLine($"  - {name}");
            }
        });

        // Wait for ALL the tasks in the list to complete.
        await Task.WhenAll(tasks);
    }    
    
    static async Task Main()
    {
        var stopwatch = Stopwatch.StartNew();
        
        var film6 = await GetDataFromServerAsync($"{TopApiUrl}/films/6");
        Console.WriteLine(film6["director"]);

        await GetUrlsAsync(film6, "characters");
        await GetUrlsAsync(film6, "planets");
        await GetUrlsAsync(film6, "starships");
        await GetUrlsAsync(film6, "vehicles");
        await GetUrlsAsync(film6, "species");
        
        stopwatch.Stop();
        
        // TODO - display the number of calls to the server
        Console.WriteLine($"Total calls to the server = {callCount}");
        Console.WriteLine($"Total execution time: {stopwatch.Elapsed.TotalSeconds:F2} seconds");
    }
}
