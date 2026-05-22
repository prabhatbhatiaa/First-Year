print("----- !! CALCULATOR  !! -----")
print("Choose an operation for calculation: ")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = input("Enter your choice (1/2/3/4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", a + b)

    elif choice == "2":
        print("Result:", a - b)

    elif choice == "3":
        print("Result:", a * b)

    elif choice == "4":
        try:
            print("Result:", a / b)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")

    else:
        print("Invalid choice")

except ValueError:
    print("Error: Please enter valid numbers!")
except Exception as e:

    print("Unexpected error:", e)
