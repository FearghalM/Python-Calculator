# Version 1: Basic structure with addition

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def calculator(operation, a, b):
    """Performs the given operation on two numbers."""
    return operation(a, b)

def main():
    add_result = calculator(add, 5, 3)
    print(f"Addition: {add_result}")  # Output: 8

if __name__ == "__main__":
    main()
