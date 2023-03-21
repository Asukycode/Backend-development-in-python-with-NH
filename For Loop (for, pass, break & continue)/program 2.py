# Write a program that takes a list of strings and prints out the length of each string.
size = int(input("enter your size: "))

my_lst = []

for i in range(0, size):
    my_Str = input("Enter Word: ")
    my_lst.append(my_Str)

for x in my_lst:
    print(f'{x} --> {len(x)}')