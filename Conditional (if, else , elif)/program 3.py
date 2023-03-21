# Write a program that takes in a number and identifies whether it is even or odd.

while True:
    number_entry = int(input("Enter a number to check if it's (EVEN or ODD): "))

    if number_entry % 2 == 0:
        print(f" {number_entry} is an EVEN number")
    else:
        print(f" {number_entry} is an ODD number")