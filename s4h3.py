# Nazanin Ebrahimi - Thursday 14-18
# Algebraic Identities


def square_of_binomial(a, b, type):
    if type == 'sum':
        outcome = (a ** 2) + (2 * a * b) + (b ** 2)
        return outcome
    elif type == 'difference':
        outcome = (a ** 2) - (2 * a * b) + (b ** 2)
        return outcome

result = square_of_binomial(4, 2,'sum')
a = 4
b = 2
print(f'({a}+{b})^2 = {result}')
result = square_of_binomial(4, 2,'difference')
a = 4
b = 2
print(f'({a}-{b})^2 = {result}')
