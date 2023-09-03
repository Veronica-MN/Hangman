import random
from random import randrange

word_list = ['LEARNING','PYTHON','CREATING','GAME','HANGMAN','CODING']
word = word_list[randrange(len(word_list))]
hidden_word = "- " * len(word)
print(f"The hidden word is: {hidden_word}")
no_of_attempts = 4
print('==============================================================')


while no_of_attempts > 0 and hidden_word.count("- ") != 0:
    index_count = 0
    letter_count = 0
    
    print("pick a letter: ")
    picked_letter = input().capitalize()
    for letter in word:
        if(picked_letter == letter):
            hidden_word = hidden_word[:index_count] + picked_letter + hidden_word[index_count+1:]
            letter_count += 1
        index_count += 1
    if(letter_count == 0):
        no_of_attempts -= 1
        print(f'WRONG! Number of attempts left: {no_of_attempts}')
        print(4 - no_of_attempts)
    else:
        print(f"CORRECT! There is a letter {picked_letter} in the secret word")
    print(hidden_word)
    print('==============================================================')
if(no_of_attempts == 0):
    print("HANGED!!!")
else:
    print("CONGRATULATIONS!!!")