import random

import art
import words

chosen_word = random.choice(words.word_list)
lives = 6
display = []

for i in range(len(chosen_word)):
    display.append("_")

print(art.logo)

while True:
    print(art.stages[lives])
    print(display)
    print(lives)

    guess = input("Guess a letter >> ").lower()

    if len(guess) == 1:
        correct = False

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                correct = True

        if not correct:
            lives -= 1

            if lives == 0:
                print("You lose! The word was " + chosen_word + ".")
                break

        elif not display.__contains__("_"):
            print("You win!")
            break

    else:
        print("Must be only one letter!")
