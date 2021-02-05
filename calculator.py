def add(a, b):
    try:
        a_conv = int(a)
        b_conv = int(b)

        return a_conv + b_conv
    except ValueError:
        return "Error: Inputs must be integers!"


def subtract(a, b):
    try:
        a_conv = int(a)
        b_conv = int(b)

        return a_conv - b_conv
    except ValueError:
        return "Error: Inputs must be integers!"


def multiply(a, b):
    try:
        a_conv = int(a)
        b_conv = int(b)

        return a_conv * b_conv
    except ValueError:
        return "Error: Inputs must be integers!"


def divide(a, b):
    try:
        a_conv = int(a)
        b_conv = int(b)

        if (b_conv == 0):
            return "Error: Cannot divide by zero!"
        else:
            return a_conv // b_conv
    except ValueError:
        return "Error: Inputs must be integers!"


def main():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    while True:
        choice = input("Enter choice: ")

        if choice in ('1', '2', '3', '4', '5'):
            if (choice == '5'):
                break

            a = input("Enter first number: ")
            b = input("Enter second number: ")

            if choice == '1':
                print(add(a, b))

            elif choice == '2':
                print(subtract(a, b))

            elif choice == '3':
                print(multiply(a, b))

            elif choice == '4':
                print(divide(a, b))
        else:
            print("Error: Invalid choice!")


if __name__ == "__main__":
    main()
