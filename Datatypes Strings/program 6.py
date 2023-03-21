# Character Count: Write a program to count the number of times (a,e,i,o,u) appears in the user's input.

my_word = input("Enter word: ")
x = [i for i in my_word]
count = 0
vowel = ["a", "e", "i", "o", "u"]
for v in vowel:
    for each in x:
        if v == each:
            count += 1
print(f"We have {count} vowels in the word {my_word.upper()}")
