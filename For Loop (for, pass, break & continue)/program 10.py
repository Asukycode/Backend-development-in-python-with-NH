# Write a program that takes a list of numbers and prints out the average of the numbers in the list.

my_lst_size = int(input("Enter your list size: "))
my_lst = []
total = 0
while len(my_lst) < my_lst_size:
    lst_entry = int(input("Enter your number: "))
    my_lst.append(lst_entry)
    for i in my_lst:
        total += i
    average = total/len(my_lst)
print(f'The average of the list {my_lst} is {average}')