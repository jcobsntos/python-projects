def decimal_to_binary(decimal):
    i = 0
    binary = 0
    while decimal != 0:
        remainder = decimal % 2
        binary = binary + remainder * (10 ** i)
        decimal = decimal // 2
        i += 1

    return binary


def binary_to_decimal(binary):
    i = 0
    decimal = 0
    while binary != 0:
        remainder = binary % 10
        decimal = decimal + remainder * (2 ** i)
        binary = binary // 10
        i += 1

    return decimal


while True:
    print("\nDecimal To Binary - Vice Versa")
    print("Menu: ")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    user_input = int(input("Enter choice: "))

    match user_input:
        case 1:
            decimal_input = int(input("Enter decimal number : "))
            print("Binary Equivalent : ", decimal_to_binary(decimal_input))
        case 2:
            binary_input = int(input("Enter binary number : "))
            print("Decimal Equivalent :", binary_to_decimal(binary_input))
        case other:
            print("Invalid... Please re-enter")
            continue

    if input("Again? [y/n] = ") == 'y':
        continue
    else:
        print("Program Termination...Goodbye!")
        break
