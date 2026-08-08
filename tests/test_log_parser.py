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

def test_parse_log_line():
    line = "2024-08-06 10:15:32 | ERROR | auth-service | Login failed"
    result = parse_log_line(line)
    assert result['level'] == 'ERROR'
    assert result['source'] == 'auth-service'
    print("test_parse_log_line passed")

if __name__ == "__main__":
    test_parse_log_line()
    print("All tests passed!")