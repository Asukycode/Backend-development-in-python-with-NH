# Write a program that takes in a list of numbers and prints out the largest number in the list.

while True:
    lst_size = int(input("How many numbers do you want to enter in the list Specify below\n :> "))
    my_list = []
    largest_num = 0
    count = 1
    while len(my_list) < lst_size:
        lst_input = int(input(f'Enter your {count} number: '))
        my_list.append(lst_input)
        count += 1

    for x in my_list:
        if x > largest_num:
            largest_num = x
    print(f'{largest_num} is the largest number from the list of {my_list} ')
