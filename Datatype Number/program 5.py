# Calculates the Quadratic formulae for 3 given numbers

def quadratic(a: int, b: int, c: int):
    formula = (-b + - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print(f'The answer to the quadratic equation is {formula}')


quadratic(int(input("Enter your value for a")), int(input("Enter your value for b")), int(input("Enter your value for c")))
