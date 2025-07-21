using System.Text.Json.Serialization;

public class Person
{    [JsonPropertyName("id")]
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
}