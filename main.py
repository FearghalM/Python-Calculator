def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """Returns the division of a by b. Handles division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator(operation, a, b):
    return operation(a, b)

def main():
    add_result = calculator(add, 5, 3)
    subtract_result = calculator(subtract, 5, 3)
    multiply_result = calculator(multiply, 5, 3)
    division_result = calculator(divide, 5, 0)  # Testing division by zero
    print(f"Addition: {add_result}")
    print(f"Subtraction: {subtract_result}")
    print(f"Multiplication: {multiply_result}")
    print(f"Division: {division_result}")  # Output: Error

if __name__ == "__main__":
    main()
