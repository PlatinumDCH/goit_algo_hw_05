import sys
from pathlib import Path
import re
from typing import DefaultDict, Optional, Callable
from collections import defaultdict
from functools import wraps


def parse_log_file(line:str)->dict|None:
    pattern = (
    r'(?P<date>\d{4}-\d{2}-\d{2})\s+'
    r'(?P<time>\d{2}:\d{2}:\d{2})\s+'
    r'(?P<log_level>[A-Z]+)\s+'
    r'(?P<message>.+)'
)
    match = re.match(pattern, line)
    if match:
        log_data = match.groupdict()
        return log_data
    else:
        return None

F = Callable[[Path], list]
def error_handling_decorator(func: F) -> F:
    @wraps(func)
    def wrapper(path: Path) -> list:
        try:
            return func(path)
        except FileNotFoundError:
            print(f"Error: File '{path}' does not exist.")
            sys.exit(1)
        except OSError as e:
            print(f"Error reading file '{path}': {e}")
            sys.exit(1)

    return wrapper


@error_handling_decorator
def load_logs(path: Path) -> list:
    log_list = []
    with open(path, 'r') as file:
        for line in file:
            parse_line = parse_log_file(line)
            if parse_line:
                log_list.append(parse_line)
            else:
                print(f'Skipping invalid format: {line.strip()}')
    return log_list

def filter_logs_by_level(logs, level:str):
    return list(
    filter(
        lambda log: log['log_level'].lower() == level.lower(), 
        logs
    )
)

DF = DefaultDict[str, int]
def count_logs_by_level(logs:list)->DF:
    count_dict:DF = defaultdict(int)
    for log in logs:
        count_dict[log['log_level']] += 1
    return count_dict

def display_log(log_counts:dict):
    print("Logs name          | counted")
    print("-------------------|----------")
    for level, count in sorted(log_counts.items()):
        print(f"{level:<18} | {count:>5}")

def display_filtered_logs(logs:list):
    for log in logs:
        print(
    f"{log['date']} "
    f"{log['time']} "
    f"{log['log_level']} "
    f"{log['message']}"
)

def main(path:Path, target_log:Optional[str] = None):
    logs = load_logs(path)

    if not logs:
        print("No logs found in file")
        return
    log_counts = count_logs_by_level(logs)
    display_log(log_counts)
    
    if target_log:
        filtered_logs = filter_logs_by_level(logs, target_log)
        display_filtered_logs(filtered_logs)

if __name__ == '__main__':
    if len(sys.argv) ==  2:
        path = Path(sys.argv[1])
        target_log = None
    elif len(sys.argv) == 3:
        path = Path(sys.argv[1])
        target_log = sys.argv[2]
    
    if path.exists() and path.is_file():
        main(path, target_log)
    else:
        print(f"File {path} does not exist or is not a file")
