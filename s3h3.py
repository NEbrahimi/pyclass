# Nazanin Ebrahimi - Thursday 14-18
# Shape area and perimeter calculator
# Choose on of these shapes: rectangule, circle, triangle

def shape_calculator(parameter1, parameter2, shape, question):
    if shape == 'rectangle' and question == 'area':
        result = parameter1 * parameter2
        print(f'Area of rectangle = {result}')
    elif shape == 'rectangle' and question == 'perimeter':
        result = (parameter1 + parameter2) *2
        print(f'Perimeter of rectangle = {result}')
    elif shape == 'circle' and question == 'area':
        parameter1=3.14
        result = parameter1 * (parameter2**2)
        print(f'Area of circle = {result}')
    elif shape == 'circle' and question == 'perimeter':
        parameter1=3.14
        result = 2 * parameter1 * parameter2
        print(f'Perimeter of circle = {result}')
    elif shape == 'triangle' and question == 'area':
        result = parameter1 * parameter2 * 1/2
        print(f'Area of triangle = {result}')
    elif shape == 'triangle' and question == 'perimeter':
        print(f'Third argument is needed to calculate perimeter of a triangle!')

    else:
        print('what')


shape_calculator(2, 3, 'rectangle', 'area')
shape_calculator(2, 3, 'rectangle', 'perimeter')
shape_calculator(3.14, 3, 'circle', 'area')
shape_calculator(3.14, 3, 'circle', 'perimeter')
shape_calculator(2, 3, 'circle', 'area') #To test whether code is robust for the pi
shape_calculator(2, 3, 'circle', 'perimeter') #To test whether code is robust for the pi
shape_calculator(2, 3, 'triangle', 'area')
shape_calculator(2, 3, 'triangle', 'perimeter')
