import random
import re

all_words = []
choose_from = []
guessed_it = []
in_it = []
difficulty = ""
guess_this = ""

def reads():
    with open('dictionary.txt', 'r') as read:
        for line in read:
            for word in line.split():
                word = re.sub('[^A-Za-z]', '', word).lower()
                all_words.append(word)

def make_difficulty_wordlist(all_words, difficulty):
    for word in all_words:
        if difficulty == "1":
            if len(word) <= 6 and len(word) >= 4:
                choose_from.append(word)
                continue
        elif difficulty == "2":
            if len(word) <= 8 and len(word) >= 6:
                choose_from.append(word)
                continue
        elif difficulty == "3":
            if len(word) > 8:
                choose_from.append(word)
                continue

def display_blankspaces(guess_this):
    blanks = '_' * len(guess_this)
    for i in range(len(guess_this)):
        if guess_this[i] in in_it:
              blanks = blanks[:i] + guess_this[i] + blanks[i+1:]
    for letter in blanks:
        print(letter.upper(), end=' ')

def guess_awful(user_guess):
    if not user_guess.isalpha():
        print("with letters")
    if len(user_guess) != 1:
        print("one at a time")

reads()
difficulty = input("difficulty level 1, 2, or 3? ")
make_difficulty_wordlist(all_words, difficulty)
guess_this = random.choice(choose_from)

def main(display_blankspaces, guess_awful):
    count = 8
    while count >= 0:

        print(count, "guesses left")

        display_blankspaces(guess_this)

        if set(guess_this) == set(in_it):
            print("You Win!")
            break

        user_guess = input('> ')
        user_guess = user_guess.lower()

        guess_awful(user_guess)

        if user_guess in guessed_it:
            print("Try again")
            continue
        elif user_guess in guess_this:
            in_it.append(user_guess)
            guessed_it.append(user_guess)
            continue
        guessed_it.append(user_guess)
        count -= 1
        if count == 0:
            print("You lose")
            print("the word was", guess_this)
            break
        continue

if __name__ == '__main__':
    main(display_blankspaces, guess_awful)
