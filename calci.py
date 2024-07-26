
while True:
    print("**** Calculator ****")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Operations:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    choice = input("Enter the operation (1-5): ")

    if choice == '1':
        result = num1 + num2
        print("Addition is:", result)
    elif choice == '2':
        result = num1 - num2
        print("Subtraction is:", result)
    elif choice == '3':
        result = num1 * num2
        print("Multiplication is:", result)
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Division is:", result)
        else:
            print("Cannot divide by zero.")
    elif choice == '5':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    
    next_calculation = input("Do you want to continue? (1:yes 0:no): ")
    if next_calculation.lower() != "1":
        break


