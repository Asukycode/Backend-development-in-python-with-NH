# String Substring: Write a program to output the first five characters of a user's input.

user_input = input("Enter your word to find the length: ")
print(f'The first 5 letters of the word {user_input} is {user_input[0:5].upper()}')