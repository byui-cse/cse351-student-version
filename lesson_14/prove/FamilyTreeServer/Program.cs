using System.Net;
using System.Text.Json;

internal static class Program
{
    private const string Hostname = "127.0.0.1";
    private const int Port = 8123;
    private const double Sleep = 0.25;
    private const int MaxGenerations = 6;


    private static readonly long[] Primes =
    [
        5000007787, 5000007797, 5000007799, 5000007811, 5000007823, 5000007829, 5000007877, 5000007899,
        5000007911, 5000007919, 5000007953, 5000007977, 5000007983, 5000008007, 5000008037, 5000008043,
        5000008109, 5000008121, 5000008127, 5000008133, 5000008147, 5000008151, 5000008201, 5000008219,
        5000008271, 5000008297, 5000008313, 5000008319, 5000008361, 5000008369, 5000008373, 5000008417
    ];

    private static readonly Random Random = new Random();
    private static readonly long Prime = Random.GetItems(Primes, 1)[0];
    private static readonly long Id = Random.NextInt64(10000, 10000000);

    private static readonly string[] MaleNames =
    [
        "Liam", "Noah", "Oliver", "William", "Elijah", "James", "Benjamin", "Lucas", "Mason", "Ethan", "Alexander",
        "Henry", "Jacob", "Michael", "Daniel", "Logan", "Jackson", "Sebastian", "Jack", "Aiden", "Owen", "Samuel",
        "Matthew", "Joseph", "Levi", "Mateo", "David", "John", "Wyatt", "Carter", "Julian", "Luke", "Grayson", "Isaac",
        "Jayden", "Theodore", "Gabriel", "Anthony", "Dylan", "Leo", "Lincoln", "Jaxon", "Asher", "Christopher",
        "Josiah", "Andrew", "Thomas", "Joshua", "Ezra", "Hudson"
    ];

    private static readonly string[] FemaleNames =
    [
        "Olivia", "Emma", "Ava", "Sophia", "Isabella", "Charlotte", "Amelia", "Mia", "Harper", "Evelyn", "Abigail",
        "Emily", "Ella", "Elizabeth", "Camila", "Luna", "Sofia", "Avery", "Mila", "Aria", "Scarlett", "Penelope",
        "Layla", "Chloe", "Victoria", "Madison", "Eleanor", "Grace", "Nora", "Riley", "Zoey", "Hannah", "Hazel", "Lily",
        "Ellie", "Violet", "Lillian", "Zoe", "Stella", "Aurora", "Natalie", "Emilia", "Everly", "Leah", "Aubrey",
        "Willow", "Addison", "Lucy", "Audrey", "Bella"
    ];

    private static int _maxThreadCount;
    private static int _callCount;
    private static int _threadCount;
    private static readonly object Lock = new();
    private static List<long> _familyRequestOrder = [];

    private static Dictionary<long, Person> _people = new();
    private static Dictionary<long, Family> _families = new();
    private static int _generationsCreated;


    public static void Main()
    {
        // Start the listener
        HttpListener listener = new();
        listener.Prefixes.Add($"http://{Hostname}:{Port}/");
        listener.Start();

        Console.WriteLine($"Listening on http://{Hostname}:{Port}/");

        while (true)
        {
            var context = listener.GetContext();
            Task.Run(() => ProcessRequest(context));
        }

        // ReSharper disable once FunctionNeverReturns
    }

    private static long Encode(long id) => (id * Id) ^ Prime;

    private static long Decode(long code) => (code ^ Prime) / Id;

    private static async Task ProcessRequest(HttpListenerContext context)
    {
        lock (Lock)
        {
            _threadCount++;
            _callCount++;
            if (_threadCount > _maxThreadCount)
            {
                _maxThreadCount = _threadCount;
            }

            Console.WriteLine($"Current: active threads / max count: {_threadCount} / {_maxThreadCount}");
        }

        var path = context.Request.Url?.AbsolutePath.Trim('/');

        await Task.Delay(TimeSpan.FromSeconds(Sleep)); // Simulate processing delay

        var parts = path?.Split("/");
        string? output;
        if (path!.Contains("start"))
        {
            // Start
            _familyRequestOrder = [];
            _nextPersonId = 1;
            _nextFamilyId = 1;
            if (parts!.Length < 2)
            {
                SendNotFound(context);
                return;
            }

            if (!int.TryParse(parts[^1], out var generations))
            {
                generations = MaxGenerations;
            }

            Console.WriteLine($"Creating family tree with {generations} generations...");
            // print(output)
            // log.write(output)
            _generationsCreated = generations;
            BuildTree(generations);

            _maxThreadCount = 1;
            _threadCount = 1;
            _callCount = 1;

            output = "{\"status\":\"OK\"}";
        }
        else if (path.Contains("end"))
        {
            // End
            Console.WriteLine("################################################################################");
            Console.WriteLine($"Total number of people  : {_people.Count}");
            Console.WriteLine($"Total number of families: {_families.Count}");
            Console.WriteLine($"Number of generations   : {_generationsCreated}");
            Console.WriteLine($"Families were requested in this order:\n{string.Join(", ", _familyRequestOrder)}");
            Console.WriteLine(string.Join(", ", _familyRequestOrder));
            Console.WriteLine($"Total number of API calls: {_callCount}");
            Console.WriteLine($"Final thread count (max count): {_maxThreadCount}");
            Console.WriteLine("################################################################################");
            output =
                $"{{\"status\":\"OK\", \"people\": {_people.Count}, \"families\": {_families.Count}, \"api\": {_callCount}, \"threads\": {_maxThreadCount}}}";
        }
        else if (path.Contains("person"))
        {
            // Person
            if (parts!.Length < 2)
            {
                SendNotFound(context);
                return;
            }

            if (!long.TryParse(parts[^1], out var id))
            {
                SendNotFound(context);
                return;
            }

            output = JsonSerializer.Serialize(_people[id]);
        }
        else if (path.Contains("family"))
        {
            // Family
            if (parts!.Length < 2)
            {
                SendNotFound(context);
                return;
            }

            if (!long.TryParse(parts[^1], out var id))
            {
                SendNotFound(context);
                return;
            }

            output = JsonSerializer.Serialize(_families[id]);
            _familyRequestOrder.Add(Decode(id));
        }
        else // default path
        {
            output = $"{{\"start_family_id\":{Encode(1)}}}";
        }

        context.Response.StatusCode = (int)HttpStatusCode.OK;
        context.Response.ContentType = "application/json";

        var buffer = System.Text.Encoding.UTF8.GetBytes(output);
        context.Response.ContentLength64 = buffer.Length;
        await context.Response.OutputStream.WriteAsync(buffer);
        context.Response.OutputStream.Close();
        context.Response.Close();


        lock (Lock)
        {
            _threadCount--;
        }
    }

    private static void SendNotFound(HttpListenerContext context)
    {
        context.Response.StatusCode = (int)HttpStatusCode.NotFound;
        context.Response.ContentType = "application/json";
        context.Response.Close();
        lock (Lock)
        {
            _threadCount -= 1;
        }
    }

    private static long _nextPersonId = 1;
    private static long _nextFamilyId = 1;

    private static void BuildTree(int generations)
    {
        _people = new Dictionary<long, Person>();
        _families = new Dictionary<long, Family>();
        _nextFamilyId = 1;
        _nextPersonId = 1;

        CreateFamily(generations);
        Console.WriteLine($"Number of people  : {_people.Count}");
        Console.WriteLine($"Number of families: {_families.Count}");
    }

    private static Family CreateFamily(int generations)
    {
        var husband = new Person { Id = Encode(_nextPersonId++), Name = MaleName(), Birth = GetBirth() };
        _people[husband.Id] = husband;

        var wife = new Person { Id = Encode(_nextPersonId++), Name = FemaleName(), Birth = GetBirth() };
        _people[wife.Id] = wife;

        var family = new Family { Id = Encode(_nextFamilyId++), Husband = husband.Id, Wife = wife.Id };
        husband.FamilyId = family.Id;
        wife.FamilyId = family.Id;
        _families[family.Id] = family;

        var numberChildren = Random.Next(2, 8);
        for (int i = 0; i < numberChildren; i++)
        {
            var name = Random.Next(2) == 1 ? MaleName() : FemaleName();
            var child = new Person { Id = Encode(_nextPersonId++), Name = name, Birth = GetBirth() };
            _people[child.Id] = child;
            family.Children.Add(child.Id);
        }

        if (generations > 1)
        {
            // create parents and recurve calls
            var husbandParents = CreateFamily(generations - 1);
            husband.ParentId = husbandParents.Id;
            husbandParents.Children.Add(husband.Id);

            var wifeParents = CreateFamily(generations - 1);
            wife.ParentId = wifeParents.Id;
            wifeParents.Children.Add(wife.Id);
        }

        // return the family that was created
        return family;
    }

    private static string GetBirth()
    {
        var startDate = DateTime.Parse("1753/1/1");
        var endDate = DateTime.Parse("2020/1/1");

        var timeBetweenDates = endDate - startDate;
        var daysBetweenDates = timeBetweenDates.Days;
        var randomNumberOfDays = Random.Next(daysBetweenDates);
        var randomDate = startDate + TimeSpan.FromDays(randomNumberOfDays);
        return $"{randomDate.Day}-{randomDate.Month}-{randomDate.Year}";

    }

    private static string FemaleName()
    {
        return FemaleNames[Random.Next(0, FemaleNames.Length)];
    }

    private static string MaleName()
    {
        return MaleNames[Random.Next(0, MaleNames.Length)];
    }
}