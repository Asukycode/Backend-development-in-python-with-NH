# Write a program that converts kilometer to miles

def mile_converter(num):
    return f'{num * 0.621371:.4} miles'


print("Enter Value in kilometer to convert to miles")

print(mile_converter(int(input("Enter you value : "))))
