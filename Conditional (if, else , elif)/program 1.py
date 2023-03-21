# Write a program that takes in two numbers and identifies whether the first number is greater than, less than,
# or equal to the second number.

while True:
    num1 = float(input("Enter thr first number: "))
    num2 = float(input("Enter the second number: "))

    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print(f"{num2} is equal to {num1}")
