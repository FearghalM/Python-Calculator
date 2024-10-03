def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b

def calculator(operation, a, b):
    """Performs the given operation on two numbers."""
    return operation(a, b)

def main():
    add_result = calculator(add, 5, 3)
    subtract_result = calculator(subtract, 5, 3)
    print(f"Addition: {add_result}")       # Output: 8
    print(f"Subtraction: {subtract_result}") # Output: 2

if __name__ == "__main__":
    main()