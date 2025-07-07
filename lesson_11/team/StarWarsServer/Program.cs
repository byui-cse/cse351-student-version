using System.Net;
using System.Text.Json;

internal static class Program
{
    private static readonly Dictionary<string, JsonElement> JsonData = new();

    public static void Main()
    {
        // Load and parse the JSON file
        var jsonText = File.ReadAllText("data.json");
        using var doc = JsonDocument.Parse(jsonText);

        foreach (var property in doc.RootElement.EnumerateObject())
        {
            JsonData[property.Name] = property.Value;
        }

        // Start the listener
        HttpListener listener = new();
        listener.Prefixes.Add("http://127.0.0.1:8790/");
        listener.Start();

        Console.WriteLine("Listening on http://127.0.0.1:8790/");
        
        while (true)
        {
            var context = listener.GetContext();
            // Console.WriteLine($"threads: {ThreadPool.ThreadCount} - {Environment.ProcessorCount}");
            Task.Run(()=>ProcessRequest(context));
        }

        // ReSharper disable once FunctionNeverReturns
    }

    private static async Task ProcessRequest(HttpListenerContext context)
    {
        await Task.Delay(TimeSpan.FromSeconds(.5)); // Simulate processing delay

        var path = context.Request.Url?.AbsolutePath.Trim('/');
        var parts = path?.Split('/');

        if (parts is not { Length: 2 })
        {
            context.Response.StatusCode = (int)HttpStatusCode.OK;
            context.Response.ContentType = "text/json";
            await using var writer = new StreamWriter(context.Response.OutputStream);
            await writer.WriteAsync("{\"people\": \"http://127.0.0.1:8790/people/\", \n\"planets\": \"http://127.0.0.1:8790/planets/\", \n\"films\": \"http://127.0.0.1:8790/films/\", \n\"species\": \"http://127.0.0.1:8790/species/\", \n\"vehicles\": \"http://127.0.0.1:8790/vehicles/\",\n\"starships\": \"http://127.0.0.1:8790/starships/\"}");
            return;
        }

        var category = parts[0];
        var id = parts[1];
        var key = $"{category}{id}";

        if (!JsonData.TryGetValue(key, out var value))
        {
            context.Response.StatusCode = (int)HttpStatusCode.NotFound;
            await using var writer = new StreamWriter(context.Response.OutputStream);
            await writer.WriteAsync("Not found");
            return;
        }

        var responseJson = value.GetRawText();
        var buffer = System.Text.Encoding.UTF8.GetBytes(responseJson);

        context.Response.ContentType = "application/json";
        context.Response.ContentLength64 = buffer.Length;
        await context.Response.OutputStream.WriteAsync(buffer);
        context.Response.OutputStream.Close();
    }
}