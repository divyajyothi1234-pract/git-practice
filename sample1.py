from dotenv import load_dotenv
import os
load_dotenv()

def addition(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtraction(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiplication(a, b):
    """Returns the product of a and b."""
    return a * b



addition(5,3)
print(addition(5, 3))


print(subtraction(5, 3))


## Output: 8
print(multiplication(5, 3))
print(os.getenv('secret_key'))
print(os.getenv('database_url'))  # Example of using an environment variable
