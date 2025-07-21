using System.Text.Json.Serialization;

public class Family
{
    [JsonPropertyName("id")]
    public long Id { get; set; }
    [JsonPropertyName("husband_id")]
    public long Husband { get; set; }
    [JsonPropertyName("wife_id")]
    public long Wife { get; set; }
    [JsonPropertyName("children")]
    public List<long> Children { get; set; } = new();
}