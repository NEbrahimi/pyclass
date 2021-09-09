# Nazanin Ebrahimi - Thursday 14-18
# Surface area and volume calculator
# Choose one of these shapes: cuboid, sphere, cone

def shape_calculator(parameter1, parameter2, parameter3, shape, question):
    if shape == 'cuboid' and question == 'area':
        outcome = (2 * parameter1 * parameter2) + (2 * parameter2 * parameter3)\
        + (2 * parameter1 * parameter3)
        return outcome
    elif shape == 'cuboid' and question == 'volume':
        outcome = parameter1 * parameter2 * parameter3
        return outcome
    elif shape == 'sphere' and question == 'area':
        parameter3 = 3.14
        parameter2 = 1
        outcome = 4 * parameter3 * (parameter1**2)
        return outcome
    elif shape == 'sphere' and question == 'volume':
        parameter1 =3.14
        parameter2 = 1
        outcome = 4/3 * parameter3 * (parameter1 ** 3)
        return outcome
    elif shape == 'cone' and question == 'area':
        parameter3=3.14
        outcome = parameter3 * (parameter1 ** 2) + (parameter1 * parameter2 *\
        parameter3)
        return outcome
    elif shape == 'cone' and question == 'volume':
        parameter3=3.14
        outcome = 1/3 * (parameter1 ** 2) * parameter2 * parameter3
        return outcome



result = shape_calculator(2, 3, 4, 'cuboid', 'area')
print(f'Surface area of cuboid = {result}')
result = shape_calculator(2, 3, 4, 'cuboid', 'volume')
print(f'Volume of cuboid = {result}')
result = shape_calculator(3, 1, 3.14, 'sphere', 'area')
print(f'Surface area of sphere = {result}')
result = shape_calculator(3, 2, 3.14, 'sphere', 'volume')
print(f'Volume of sphere = {result}')
result = shape_calculator(2, 3, 3.14,'cone', 'area')
print(f'Surface area of cone = {result}')
result = shape_calculator(2, 3, 3.14, 'cone', 'volume')
print(f'Volume of cone = {result}')
