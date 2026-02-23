import sys
import re

commit_msg_filepath = sys.argv[1]

with open(commit_msg_filepath, 'r') as f:
    content = f.read()

pattern = r'^\[[A-Z]+-[0-9]+\]'

if not re.match(pattern, content):
    print("ERROR: Your commit message is missing a Jira Ticket ID!")
    print("Example: [PROJ-123] My commit message")
    sys.exit(1)  
else:
    print("Jira ID found. Commit allowed.")
    sys.exit(0)  