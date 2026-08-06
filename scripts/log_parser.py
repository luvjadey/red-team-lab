import json
from datetime import datetime

def parse_log_line(line):
    """Parse a single log line and return structured data."""
    parts = line.split(' | ')
    if len(parts) < 4:
        return None
    
    return {
        'timestamp': parts[0],
        'level': parts[1],
        'source': parts[2],
        'message': parts[3]
    }

def parse_logs(filename):
    """Parse all logs from a file."""
    logs = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parsed = parse_log_line(line.strip())
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"File {filename} not found")
    
    return logs

def main():
    logs = parse_logs('sample.log')
    print(f"Parsed {len(logs)} log entries")
    for log in logs[:5]:
        print(json.dumps(log, indent=2))

if __name__ == "__main__":
    main()