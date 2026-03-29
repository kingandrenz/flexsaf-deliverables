def add(a, b):
    """ Adds two values """
    return a + b

def subtract(a, b):
    """ Substracts two numbers"""
    return a - b

def multiply(a, b):
    """ Multiply two numbers """
    return a * b

def divide(a, b):
    """ divide a by b as long
        as b is non zero
    """
    if b == 0:
        return "Error: cannot divide by zero (0)"
    return a /b

