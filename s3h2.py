# Nazanin Ebrahimi - Thursday 14-18
# Calculator
# Choose one of the operators: addition, substraction, multiplication, division

def calculator(number1, number2, operator):

    if operator == 'addition':
        result = number1 + number2
        print(f'{number1} + {number2} = {result}')
    elif operator == 'substraction':
        result = number1 - number2
        print(f'{number1} - {number2} = {result}')
    elif operator == 'multiplication':
        result = number1 * number2
        print(f'{number1} * {number2} = {result}')
    elif operator == 'division':
        result = number1 / number2
        print(f'{number1} / {number2} = {result}')

calculator(27, 33, 'addition')
calculator(25, 13, 'substraction')
calculator(44, 7, 'multiplication')
calculator(55, 10, 'division')
