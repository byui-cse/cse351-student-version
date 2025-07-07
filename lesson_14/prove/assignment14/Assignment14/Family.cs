using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Assignment14;

public class Family
{
    [JsonPropertyName("id")]
    public long Id { get; set; }

    [JsonPropertyName("husband_id")]
    public long HusbandId { get; set; }

    [JsonPropertyName("wife_id")]
    public long WifeId { get; set; }

    [JsonPropertyName("children")]
    public List<long> Children { get; set; } = new List<long>();

    // This property replaces the children_count() method
    public int ChildrenCount => Children.Count;

    public override string ToString()
    {
        var output = new StringBuilder();
        output.AppendLine($"id         : {Id}");
        output.AppendLine($"husband    : {HusbandId}");
        output.AppendLine($"wife       : {WifeId}");
        foreach (long childId in Children)
        {
            output.AppendLine($"  Child    : {childId}");
        }
        return output.ToString();
    }

    public static Family? FromJson(string jsonString)
    {
        return JsonSerializer.Deserialize<Family>(jsonString);
    }
}