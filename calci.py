def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("a. Addition (+)")
        print("b. Subtraction (-)")
        print("c. Multiplication (*)")
        print("d. Division (/)")
        print("e. Exit")

        choice = input("Enter choice (a/b/c/d/e): ")

        if choice == "d":
            print("Goodbye!")
            break

        if choice not in ["a", "b", "c", "d"]:
            print("Invalid choice! Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == "a":
            result = add(num1, num2)
        elif choice == "b":
            result = subtract(num1, num2)
        elif choice == "c":
            result = multiply(num1, num2)
        elif choice == "d":
            result = divide(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
