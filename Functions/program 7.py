import math


def hypotenous_length(opp, adj):
    formula = math.sqrt(opp ** 2 + adj ** 2)
    return f"The answers is {formula:.3f}"


print(hypotenous_length(int(input("Enter value for your opposite: ")), int(input("Enter value for your adjacent: "))))
