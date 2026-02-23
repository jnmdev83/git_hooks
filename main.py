import os

def greeting(name):
    """A simple function to demonstrate code formatting."""
    return f"Hello, {name}! Welcome to the DevOps pipeline."

if __name__ == "__main__":
    # --- TESTING AREA ---
    # 1. To test 'trailing-whitespace' hook: Leave spaces at the end of a line.
    # 2. To test 'end-of-file-fixer': Delete the very last empty line of this file.
    
    user_name = os.getenv("USER", "DevOps Engineer")
    print(greeting(user_name))

    # 3. To test 'detect-secrets' or 'gitleaks' hook: 
    # Uncomment the line below. The hook should block the commit!
# AWS_SECRET_KEY = "AKIAIMOR76BEXAMPLE"