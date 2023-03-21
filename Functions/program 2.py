
def celcius_farhenheit(num):
    formula = (5 / 9) * (num - 32)
    return f"The celsius value for {num}F is {formula}C"


print(celcius_farhenheit(float(input("Enter fahrenheit value : "))))
