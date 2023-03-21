# Write a program that takes in a number and prints out whether it is positive, or negative.

while True:
    num = int(input("Enter thr first number: "))

    if num > 0:
        print(f'{num} is a positive number')
    else:
        print(f'{num} is a negative number')