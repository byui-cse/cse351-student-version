using System.Text.Json;
using System.Text.Json.Serialization;

public class NullToZeroLongConverter : JsonConverter<long>
{
    public override long Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        // If the JSON token is null, return 0
        if (reader.TokenType == JsonTokenType.Null)
        {
            return 0;
        }
        
        // Otherwise, read the number as a long
        return reader.GetInt64();
    }

    public override void Write(Utf8JsonWriter writer, long value, JsonSerializerOptions options)
    {
        // Write the long value back to JSON as a number
        writer.WriteNumberValue(value);
    }
}