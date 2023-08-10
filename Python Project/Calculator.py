import sys

# while True:
#   operator = input('''
#     1. Addition
#     2. Subtraction
#     3. Multiplication
#     4. Division
#     5. Quit
        
#     Please select an operation: 
#     ''')

#   if operator == '5':
#     sys.exit()

#   numbers = []
  
#   while True:
#     number = input('Enter a number: ')
#     if number.isnumeric():
#       numbers.append(float(number))
#     elif number == 'done':
#       break
#     else:
#       print('Error! Please enter a valid number.')
#       number = input('Enter a number: ')
#       if number.isnumeric():
#         numbers.append(float(number))
            

#   if operator == '1':
#     result = sum(numbers)
#     print(f"The result is {result}")
#   elif operator == '2':
#     result = numbers[0]
#     for number in numbers[1:]:
#       result -= number
#       print(f"The result is {result}")
#   elif operator == '3':
#     result = 1
#     for number in numbers:
#       result *= number
#     print(f"The result is {result}")
#   elif operator == '4':
#     result = numbers[0]
#     for number in numbers[1:]:
#       result /= number
#     print(f"The result is {result}")
#   else:
#     print("Error! Please try again")
#     sys.exit()

def get_numbers():
    numbers = []
    while True:
        number = input('Enter a number or c to complete the input: ')
        if number.isnumeric():
            numbers.append(float(number))
        elif number == 'c':
            break
        else:
            print('Error! Please enter a valid number.')
    return numbers

def addition(numbers):
    result = sum(numbers)
    print(f"The result is {result}")

def subtraction(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    print(f"The result is {result}")

def multiplication(numbers):
    result = 1
    for number in numbers:
        result *= number
    print(f"The result is {result}")

def division(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    print(f"The result is {result}")

while True:
    operator = input('''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Quit
        
    Please select an operation: 
    ''')

    if operator == '5':
        sys.exit()

    numbers = get_numbers()

    if operator == '1':
        addition(numbers)
    elif operator == '2':
        subtraction(numbers)
    elif operator == '3':
        multiplication(numbers)
    elif operator == '4':
        division(numbers)
    else:
        print("Error! Please try again")
