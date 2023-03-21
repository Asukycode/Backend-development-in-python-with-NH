# Write a program that takes in a list of numbers and prints out all the numbers that are divisible by 3.

while True:
    lst_size = int(input("How many numbers do you want to enter into the list :> "))
    my_list = []
    new_li = []
    count = 0
    while len(my_list) < lst_size:
        ls_entry = int(input(f"Enter number {count+1}: "))
        my_list.append(ls_entry)
        if my_list[count] % 3 == 0:
            new_li.append(my_list[count])
        count +=1
    print(f'These are the numbers which are divisible by 3 {new_li}')