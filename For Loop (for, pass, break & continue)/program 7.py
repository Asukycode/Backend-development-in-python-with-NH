# Write a program that takes a list of numbers and prints out the product of all the numbers in the list.

lst_size = int(input("Enter your list size: "))
my_lst_num = []
product = 1
while len(my_lst_num)<lst_size:
    my_lst_input = int(input("Enter your number: "))
    my_lst_num.append(my_lst_input)
for i in my_lst_num:
    product *= i
print(f"The product of all the numbers in the is list is {product}")