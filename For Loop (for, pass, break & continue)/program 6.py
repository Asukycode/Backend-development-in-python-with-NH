# Write a program that takes a string and removes all vowels from the string.

my_word = input("Enter your word")
vowels = ["a", "e", "i", "o", "u"]
my_word_lst = []
for i in my_word:
    my_word_lst.append(i)
for v in vowels:
    for x in my_word_lst:
        if v == x:
            my_word_lst.remove(v)
            my_new_word = "".join(my_word_lst)
print(my_new_word)
