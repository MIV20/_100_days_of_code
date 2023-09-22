from calc_art import logo
from replit import clear


# calc app


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return round((n1 * n2), 4)


def divide(n1, n2):
    return round((n1 / n2), 4)

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(logo)


    num1 = float(input("What is the first number: "))
    for operator in operations:
        print(operator)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number: "))

        if operation_symbol not in operations:
            print("Not a valid selection, try again.")
        else:
            calc_function = operations[operation_symbol]
            answer = calc_function(num1, num2)
            if isinstance(answer, float):
                print(f"{num1} {operation_symbol} {num2} = {answer:.4f}.")
            else:
                print(f"{num1} {operation_symbol} {num2} = {answer}.")


        if input(f"Type 'y' to continue calculating with {answer}, "
                 f"type 'n' to start a new calculation or , 'e' to exit: ") == 'y'.lower():
            num1 = answer
        elif 'n'.lower():
            should_continue = False
            clear()
            calculator()
        elif 'exit':
            print("Thanks for using the calculator")
            break

calculator()