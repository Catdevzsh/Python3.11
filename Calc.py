## write a calculator program that takes two numbers and an operator (+, -, *, /) as input and then outputs the result of the calculation.
## For example, if the user enters 2, +, and 3, the program should output 5.
## If the user enters 2, /, and 3, the program should output 0.6666667.
## If the user enters 2, -, and 3, the program should output -1.
## If the user enters 2, *, and 3, the program should output 6.
## If the user enters 2, ^, and 3, the program should output 8.

print('Welcome to the Calculator Program')
print('Please enter two numbers and an operator (+, -, *, /)')

num1 = float(input('Enter the first number: '))
op = input('Enter the operator: ')
num2 = float(input('Enter the second number: '))

# if the opearator is invalid, print an error message
if op != '+' and op != '-' and op != '*' and op != '/':
    print('Invalid operator')

# if the operator is valid, print the result of the calculation
else:
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
