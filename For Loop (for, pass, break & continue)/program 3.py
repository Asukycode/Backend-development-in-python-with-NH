# Write a program that takes a string and prints out each character of the string in reverse order.

while True:
    my_Str = input("Enter Word: ")
    for i in my_Str:
        print(i)
    print(f"The reverse of {my_Str} is {my_Str[::-1]}")