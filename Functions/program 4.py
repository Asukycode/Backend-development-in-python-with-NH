import math


def logNumber(num):
    return f"The log is {math.log10(num)}"

print(logNumber(int(input("Enter your value to find the log of the number : "))))