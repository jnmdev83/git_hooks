import sys
import re

SECRET_PATTERNS = {
    "AWS API Key": r"AKIA[0-9A-Z]{16,}",
    "Generic Secret": r"[a-zA-Z0-9_]*([sS][eE][cC][rR][eE][tT]|[pP][aA][sS][sS][wW][oO][rR][dD])[a-zA-Z0-9_]*\s*[:=]\s*['\"].+['\"]",
    "Bearer Token": r"Bearer\s+[A-Za-z0-9\-\._~\+\/]+"
}

def scan_file(filepath):
    failed = False
    with open(filepath, 'r') as f:
        for line_num, line in enumerate(f, 1):
            if line.strip().startswith('#'):
                continue  
            for name, pattern in SECRET_PATTERNS.items():
                if re.search(pattern, line):
                    print(f"CRITICAL: {name} found in {filepath} at line {line_num}!")
                    failed = True
    return failed

if __name__ == "__main__":
    files_to_check = sys.argv[1:]
    has_errors = False

    for file in files_to_check:
        if scan_file(file):
            has_errors = True

    if has_errors:
        sys.exit(1) 
    sys.exit(0) 