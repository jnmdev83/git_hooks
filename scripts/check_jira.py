import sys
import re

# The first argument passed by git is usually the path to the commit message file
commit_msg_filepath = sys.argv[1]

with open(commit_msg_filepath, 'r') as f:
    content = f.read()

# Regular Expression to find [PROJECT-NUMBER]
pattern = r'^\[[A-Z]+-[0-9]+\]'

if not re.match(pattern, content):
    print("ERROR: Your commit message is missing a Jira Ticket ID!")
    print("Example: [PROJ-123] My commit message")
    sys.exit(1)  # EXIT 1 blocks the commit
else:
    print("Jira ID found. Commit allowed.")
    sys.exit(0)  # EXIT 0 allows the commit