# Write a program that takes a string and checks if it is a palindrome.

user_string = input("Enter your word: ")
word_rev = ''.join(reversed(user_string))
print(word_rev)
if user_string == word_rev:
    print(f'{user_string} is a planidrome')
else:
    print(f'sorry {user_string} is not a planidrome')