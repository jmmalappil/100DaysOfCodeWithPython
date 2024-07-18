#Calculator
from art import logo
print(logo)
#Add
def add(n1,n2):
    return n1 + n2

#Subtract
def substract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}



def calculator():
    print(logo)
    num1 = float(input("What's the first number?:"))
    for symbol in operations:
        print(symbol)

    is_continue = True
    while is_continue:
        operation_symbol=input("Pick another operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input("Do you want to continue? type 'y' for yes, 'n' to start a new calculation and 'x' to exit the calculator: ")
        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            is_continue = False
            calculator()
        elif choice == 'x':
            is_continue = False

calculator()



