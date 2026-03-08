def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Test the functions
print("Addition: 5 + 3 =", add(5, 3))
print("Subtraction: 10 - 4 =", subtract(10, 4))
print("Multiplication: 6 * 7 =", multiply(6, 7))
print("Division: 15 / 3 =", divide(15, 3))

def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Error: Cannot calculate square root of negative number"

print("Square root of 16 =", square_root(16))