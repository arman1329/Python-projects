# Menu Driven Calculator

while True:
    print("\n--- MENU DRIVEN CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Thank you for using calculator")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", num1 + num2)

    elif choice == 2:
        print("Result:", num1 - num2)

    elif choice == 3:
        print("Result:", num1 * num2)

    elif choice == 4:
        if num2 == 0:
            print("Error: Division by zero not allowed")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid choice! Please select 1-5")