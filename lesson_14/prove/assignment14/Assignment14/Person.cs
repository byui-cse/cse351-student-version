using Newtonsoft.Json.Linq;

namespace Assignment14;

using System.Text.Json;
using System.Text.Json.Serialization;

public class Person()
{
    [JsonPropertyName("id")]
    public long Id { get; set; }

    [JsonPropertyName("name")]
    public string Name { get; set; } = string.Empty;

    // Change from a List<int> to a single 'long' to match the JSON
    [JsonPropertyName("parent_id")]
    [JsonConverter(typeof(NullToZeroLongConverter))]
    public long ParentId { get; set; }

    // Use 'long' for this ID as well
    [JsonPropertyName("family_id")]
    [JsonConverter(typeof(NullToZeroLongConverter))]
    public long FamilyId { get; set; }

    [JsonPropertyName("birth")]
    public string Birth { get; set; } = string.Empty;

    public override string ToString()
    {
        return $"id        : {Id}\n" +
               $"name      : {Name}\n" +
               $"birth     : {Birth}\n" +
               $"parent id : {ParentId}\n" + // Updated to use ParentId
               $"family id : {FamilyId}\n";  // Updated to use FamilyId
    }

    public static Person? FromJson(string jsonString)
    {
        // Console.WriteLine($"jsonstring = {jsonString}");
        // The deserializer can return null if the JSON is invalid or represents null.
        return JsonSerializer.Deserialize<Person>(jsonString);
    }
}