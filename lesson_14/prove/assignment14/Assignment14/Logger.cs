using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;

namespace Assignment14;

public enum LogLevel
{
    Debug,    // Detailed information, typically of interest only when diagnosing problems.
    Info,     // Confirmation that things are working as expected.
    Warning,  // An indication that something unexpected happened, or an upcoming problem.
    Error,    // Due to a more serious problem, the software has not been able to perform some function.
    Fatal     // A severe error that will presumably lead to application termination.
}

public static class Logger
{
    // --- Configuration ---
    public static LogLevel MinimumLevel { get; set; } = LogLevel.Info;
    public static string? LogFilePath { get; private set; }
    public static bool LogToConsole { get; set; } = true;
    public static bool LogToFile { get; private set; } = false;

    private static readonly object _fileLock = new object(); // For thread-safe file writing

    public static void Configure(LogLevel minimumLevel = LogLevel.Info, bool logToFile = false, string? filePath = null)
    {
        MinimumLevel = minimumLevel;
        LogToFile = logToFile;

        if (LogToFile)
        {
            if (string.IsNullOrWhiteSpace(filePath))
            {
                // Default log file in the application's directory
                LogFilePath = Path.Combine(AppContext.BaseDirectory, "application.log");
            }
            else
            {
                // Ensure the directory exists if a custom path is provided
                try
                {
                    string? directory = Path.GetDirectoryName(filePath);
                    if (!string.IsNullOrEmpty(directory) && !Directory.Exists(directory))
                    {
                        Directory.CreateDirectory(directory);
                    }
                    LogFilePath = filePath;
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"[LOGGER_ERROR] Failed to set or create log file directory '{filePath}': {ex.Message}. File logging will be disabled.");
                    LogToFile = false;
                    LogFilePath = null;
                }
            }

            if (LogToFile && LogFilePath != null)
            {
                // --- CHANGE: Delete the existing log file ---
                try
                {
                    if (File.Exists(LogFilePath))
                    {
                        File.Delete(LogFilePath);
                        Console.WriteLine($"[LOGGER_CONFIG] Deleted existing log file: {LogFilePath}");
                    }
                }
                catch (Exception ex)
                {
                    // Warn the user but don't disable logging
                    Console.WriteLine($"[LOGGER_ERROR] Could not delete existing log file: {ex.Message}");
                }
                // --- END CHANGE ---

                Console.WriteLine($"[LOGGER_CONFIG] File logging enabled. Path: {LogFilePath}");
            }
        }
        else
        {
            LogFilePath = null;
            Console.WriteLine("[LOGGER_CONFIG] File logging disabled.");
        }

        Console.WriteLine($"[LOGGER_CONFIG] Minimum log level set to: {MinimumLevel}");
        Console.WriteLine($"[LOGGER_CONFIG] Console logging enabled: {LogToConsole}");
    }


    // --- Public Logging Methods ---
    public static void Debug(string message,
        [CallerMemberName] string memberName = "",
        [CallerFilePath] string sourceFilePath = "",
        [CallerLineNumber] int sourceLineNumber = 0)
    {
        Log(LogLevel.Debug, message, null, memberName, sourceFilePath, sourceLineNumber);
    }

    public static void Info(string message,
        [CallerMemberName] string memberName = "",
        [CallerFilePath] string sourceFilePath = "",
        [CallerLineNumber] int sourceLineNumber = 0)
    {
        Log(LogLevel.Info, message, null, memberName, sourceFilePath, sourceLineNumber);
    }

    public static void Warning(string message, Exception? exception = null,
        [CallerMemberName] string memberName = "",
        [CallerFilePath] string sourceFilePath = "",
        [CallerLineNumber] int sourceLineNumber = 0)
    {
        Log(LogLevel.Warning, message, exception, memberName, sourceFilePath, sourceLineNumber);
    }

    public static void Error(string message, Exception? exception = null,
        [CallerMemberName] string memberName = "",
        [CallerFilePath] string sourceFilePath = "",
        [CallerLineNumber] int sourceLineNumber = 0)
    {
        Log(LogLevel.Error, message, exception, memberName, sourceFilePath, sourceLineNumber);
    }

    public static void Fatal(string message, Exception? exception = null,
        [CallerMemberName] string memberName = "",
        [CallerFilePath] string sourceFilePath = "",
        [CallerLineNumber] int sourceLineNumber = 0)
    {
        Log(LogLevel.Fatal, message, exception, memberName, sourceFilePath, sourceLineNumber);
    }

    // --- Core Logging Logic ---
    private static void Log(LogLevel level, string message, Exception? exception = null,
        string memberName = "", string sourceFilePath = "", int sourceLineNumber = 0)
    {
        if (level < MinimumLevel)
        {
            return;
        }

        // Basic formatting for caller info
        string timestamp = DateTime.Now.ToString("HH:mm:ss.fff");
        string levelString = level.ToString().ToUpper();

        var logEntryBuilder = new System.Text.StringBuilder();
        logEntryBuilder.Append($"[{timestamp}] [{levelString}] {message}");

        if (exception != null)
        {
            logEntryBuilder.AppendLine(); // New line before exception details
            logEntryBuilder.Append($"    Exception: {exception.GetType().Name}: {exception.Message}");
            if (exception.StackTrace != null)
            {
                logEntryBuilder.AppendLine();
                logEntryBuilder.Append($"    Stack Trace: {exception.StackTrace.Trim()}");
            }
            // You can add InnerException details recursively if needed
            Exception? inner = exception.InnerException;
            int depth = 0;
            while (inner != null && depth < 5) // Limit depth
            {
                logEntryBuilder.AppendLine();
                logEntryBuilder.Append($"    Inner Exception ({depth + 1}): {inner.GetType().Name}: {inner.Message}");
                if (inner.StackTrace != null)
                {
                    logEntryBuilder.AppendLine();
                    logEntryBuilder.Append($"        Stack Trace: {inner.StackTrace.Trim()}");
                }
                inner = inner.InnerException;
                depth++;
            }
        }

        string formattedMessage = logEntryBuilder.ToString();

        // Thread-safe writing
        lock (_fileLock)
        {
            if (LogToConsole)
            {
                ConsoleColor originalColor = Console.ForegroundColor;
                switch (level)
                {
                    case LogLevel.Debug:
                        Console.ForegroundColor = ConsoleColor.Gray;
                        break;
                    case LogLevel.Info:
                        Console.ForegroundColor = ConsoleColor.White;
                        break;
                    case LogLevel.Warning:
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        break;
                    case LogLevel.Error:
                        Console.ForegroundColor = ConsoleColor.Red;
                        break;
                    case LogLevel.Fatal:
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        break;
                }
                Console.WriteLine(formattedMessage);
                Console.ForegroundColor = originalColor; // Reset color
            }

            if (LogToFile && !string.IsNullOrEmpty(LogFilePath))
            {
                try
                {
                    File.AppendAllText(LogFilePath, formattedMessage + Environment.NewLine);
                }
                catch (Exception ex)
                {
                    // Log to console that file logging failed
                    Console.WriteLine($"[LOGGER_FILE_ERROR] Failed to write to log file '{LogFilePath}': {ex.Message}");
                }
            }
        }
    }

    public static void Write(string value)
    {
        Debug(value);
    }
}
