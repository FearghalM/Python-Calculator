def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def modulus(a, b):
    return a % b

def exponent(a, b):
    """Returns a raised to the power of b."""
    return a ** b

def integer_divide(a, b):
    """Performs integer division of a by b."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a // b

def calculator(operation, a, b):
    return operation(a, b)

def main():
    add_result = calculator(add, 5, 3)
    subtract_result = calculator(subtract, 5, 3)
    multiply_result = calculator(multiply, 5, 3)
    division_result = calculator(divide, 5, 3)
    modulus_result = calculator(modulus, 5, 3)
    exponent_result = calculator(exponent, 5, 3)  # Exponent added here
    int_division_result = calculator(integer_divide, 5, 3)  # Integer division added here
    print(f"Addition: {add_result}")
    print(f"Subtraction: {subtract_result}")
    print(f"Multiplication: {multiply_result}")
    print(f"Division: {division_result}")
    print(f"Modulus: {modulus_result}")
    print(f"Exponent: {exponent_result}")  # Output: 125
    print(f"Integer Division: {int_division_result}")  # Output: 1

if __name__ == "__main__":
    main()
