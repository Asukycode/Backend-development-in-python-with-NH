# Write a program that takes a list of integers and prints the sum of all the numbers in the list.

while True:
    my_list_size = int(input("Please your list size: "))
    my_list = []
    count = 1
    total = 0
    while len(my_list) < my_list_size:
        my_list_input = int(input(f"Enter your number {count}: "))
        my_list.append(my_list_input)
        count += 1
    for i in my_list:
        total += i

    print(f"The sum of {my_list} is = {total} ")


