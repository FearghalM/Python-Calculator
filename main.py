import tkinter as tk
from tkinter import messagebox

# Calculator functions
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
    return a ** b

def integer_divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a // b

# GUI setup
def create_gui():
    window = tk.Tk()
    window.title("Calculator")

    # Input fields for numbers
    tk.Label(window, text="Enter first number:").grid(row=0, column=0)
    num1 = tk.Entry(window)
    num1.grid(row=0, column=1)

    tk.Label(window, text="Enter second number:").grid(row=1, column=0)
    num2 = tk.Entry(window)
    num2.grid(row=1, column=1)

    # Result label
    result_label = tk.Label(window, text="Result:")
    result_label.grid(row=3, column=0, columnspan=2)

    # Calculator function to handle input and display result
    def calculate(operation):
        try:
            a = float(num1.get())
            b = float(num2.get())
            result = operation(a, b)
            result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    # Buttons for operations
    tk.Button(window, text="Add", command=lambda: calculate(add)).grid(row=2, column=0)
    tk.Button(window, text="Subtract", command=lambda: calculate(subtract)).grid(row=2, column=1)
    tk.Button(window, text="Multiply", command=lambda: calculate(multiply)).grid(row=2, column=2)
    tk.Button(window, text="Divide", command=lambda: calculate(divide)).grid(row=2, column=3)
    tk.Button(window, text="Modulus", command=lambda: calculate(modulus)).grid(row=2, column=4)
    tk.Button(window, text="Exponent", command=lambda: calculate(exponent)).grid(row=2, column=5)
    tk.Button(window, text="Integer Divide", command=lambda: calculate(integer_divide)).grid(row=2, column=6)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
