print("Simple Calculator")
print("Select an operation")
print("1. + Addition")
print("2. - Subtraction")
print("3. x Multiplication")
print("4. / Division")


def addition(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def multiple(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 <= 0:
        return print("Number cannot be less than 0")
    return num1 / num2


def main():
    value = input("Enter choice from (1-4): ")
    while True:
        if value not in ["1", "2", "3", "4"]:
            print("number must be from 1-4")
        else:
            break
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    if value == "1":
        print(
            f"{first_number} + {second_number} = {addition(first_number, second_number)}")
    elif value == "2":
        print(
            f"{first_number} - {second_number} = {substract(first_number, second_number)}")
    elif value == "3":
        print(
            f"{first_number} * {second_number} = {multiple(first_number, second_number)}")
    elif value == "4":
        print(
            f"{first_number} / {second_number} = {divide(first_number, second_number)}")

    try_again = input("Do you want to perform the calculation? (yes/no): ")

    if try_again.lower() != 'yes':
        print("goodbye!")
    else:
        main()


main()
