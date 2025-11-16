num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number:"))
operation = input("What type of operation would you like to use:")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1/num2)
    case "_:":
        print("invalid operation entered")
