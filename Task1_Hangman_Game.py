import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6

print(logo[0])

chosen_word = random.choice(word_list).lower()
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []
while not game_over:

    print(f"*******{lives}/6 LIVES LEFT********")
    guess = input("Guess a letter : ").lower()

    if guess in correct_letter:
        print(f"you have aleardy guess this letter:{guess}")

    disply = ""
    for letter in chosen_word:
        if letter == guess:
            disply += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            disply += letter
        else:
            disply += "_"
    print(disply)

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess},that is not there in the word.you lost a life !!")
        if lives == 0:
            game_over = True
            print(f"*****************IT WAS {chosen_word}, YOU LOSE*****************")

    if "_" not in disply:
        game_over = True
        print("you win !")

    print(stages[-lives - 1])