import random

animals_name = ["lion", "tiger", "elephant", "giraffe", "zebra","monkey", "kangaroo", "panda", 
                "leopard", "cheetah","bear", "wolf", "fox", "rabbit", "deer","horse", "cow", 
                "goat", "sheep", "dog","cat", "camel", "dolphin", "whale", "shark"]

def choose_word():
    return random.choice(animals_name)

def display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_game():
    word = choose_word()
    guessed = []
    tries = 6

    print("Welcome to Hangman Game")

    while tries > 0:
        print("Word:", display_word(word, guessed))

        guess = input("Enter a letter: ").lower()

        if guess in guessed:
            print("Already guessed")
            continue

        if guess in word:
            guessed.append(guess)
            print("Correct!")
        else:
            tries -= 1
            print("Wrong! Tries left:", tries)

        if all(letter in guessed for letter in word):
            print("You won! The word was:", word)
            return

    print("Game over! The word was:", word)

play_game()
