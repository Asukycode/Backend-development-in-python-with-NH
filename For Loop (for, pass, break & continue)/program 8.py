# Write a program that takes a list of strings and prints out the string with the minimum length.

while True:
    my_list_size = int(input("Enter your list size: "))
    my_str_list = []
    count = 1
    shortest_length = 0
    shortest_word = "x"*my_list_size
    while len(my_str_list) < my_list_size:
        my_str_list_input = input(f"Enter your word {count}: ")
        my_str_list.append(my_str_list_input)
        count += 1
    for each in my_str_list:  # FOR LOOP USED HERE
        if len(each) < len(shortest_word):
            shortest_word = each
    print(f'Shortest word is {shortest_word} from the the list of words {my_str_list}')
