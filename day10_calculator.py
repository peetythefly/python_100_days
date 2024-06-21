# Calculator

in_operation = ''

# Operations
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

funct = operations["+"]

def calculator():
    # Ask for the first number.
    num1 = float(input("What is the first number? ")) 
    # Ask what operation to perform and give them what to pick from.
    for symbol in operations:
        print (symbol)
    keep_going = True

    while keep_going:
        op = input("What is the operation?\n")
        # Ask for the second number.
        num2 = float(input("What is the second number?\n"))

        # Perform the operation and show the result.
        # Use the given operator to pick the proper function in the dict.
        calculate = operations[op]
        # Use the proper function and pass in the two user inputs.
        answer = calculate(num1,num2)
        print (f"{num1} {op} {num2} = {answer}")
        # Ask if they want to perform another operation.
        another = input('''Do you want to perform another operation?
Type 'y' to continue with {answer}.
Type 'n' to start a new calculation.
Type anything else to exit.\n''')
        if another == 'n':
            # Recursively go into it again if they want to do a new calculation.
            calculator()
            keep_going = False
        elif another == 'y':
            keep_going == True
            num1 = answer
        else:
            keep_going = False

calculator()