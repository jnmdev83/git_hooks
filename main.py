import os

def greeting(name):
    """A simple function to demonstrate code formatting."""
    return f"Hello, {name}! Welcome to the DevOps pipeline."

if __name__ == "__main__":
   
    user_name = os.getenv("USER", "DevOps Engineer")
    print(greeting(user_name))


