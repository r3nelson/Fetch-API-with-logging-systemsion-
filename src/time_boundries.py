from datetime import datetime

def is_timestamp_within_range(start_time, end_time, ascii_timestamp):
    # Convert ASCII timestamp to datetime object with milliseconds
    timestamp_dt = datetime.strptime(ascii_timestamp, "%Y-%m-%d %H:%M:%S.%f")

    # Convert start time and end time to datetime objects
    start_time_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
    end_time_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S.%f")

    # Check if the timestamp is within the specified range
    return start_time_dt <= timestamp_dt <= end_time_dt

# Example usage:
start_time = "2024-01-23 08:00:00.000"
end_time = "2024-06-23 18:00:00.999"
ascii_timestamp = "2024-04-23 12:30:00.500"

result = is_timestamp_within_range(start_time, end_time, ascii_timestamp)
print(result)
