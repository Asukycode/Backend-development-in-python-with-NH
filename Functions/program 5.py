def quadratic(a: int, b: int, c: int):
    formula = (-b + - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return f'The answer to the quadratic equation is {formula}'


print(quadratic(int(input("Enter your value for a")), int(input("Enter your value for b")), int(input("Enter your value for c"))))
