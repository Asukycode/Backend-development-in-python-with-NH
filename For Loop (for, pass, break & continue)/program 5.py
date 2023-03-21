# Write a program that takes a list of strings and prints out the string with the maximum length.


while True:
    my_list_size = int(input("Enter your list size: "))
    my_str_list = []
    count = 1
    longest_length = 0
    longest_word = ""
    while len(my_str_list) < my_list_size:
        my_str_list_input = input(f"Enter your word {count}: ")
        my_str_list.append(my_str_list_input)
        count += 1
    for each in my_str_list:  # FOR LOOP USED HERE
        if len(each) > len(longest_word):
            longest_word = each
    print(f'longest word is {longest_word} from the the list of words {my_str_list}')
