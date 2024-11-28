# main.py
from Hangman_pics import HANGMANPICS
import random

# Type annotations
from typing import List


def display_hangman(lives: int) -> None:
    """
    Displays the current hangman stage.
    """
    print(HANGMANPICS[10 - lives])


def word_list() -> List[str]:
    """
    Returns a list of possible words for the game.
    """
    return ["cat", "dog", "fox", "owl", "bat", "cow", "ant",
        "rabbit", "panda", "tiger", "zebra", "koala", "camel", "otter",
        "kangaroo", "chameleon", "platypus", "porcupine", "pangolin",
        "armadillo", "hippopotamus"]


def play_hangman() -> None:
    """
    Main function to play the hangman game.
    """
    word = random.choice(word_list()).lower()  # Select a random word
    word_letters = set(word)  # Unique letters in the word
    guessed_letters = set()  # Letters guessed by the user
    lives = 10  # Maximum incorrect guesses
    print("\033[1;3mWelcome to Hangman!\033[0m")
    print("\033[1;3mPlease guess the name of an animal!\033[0m")
    # print("Please guess the name of an animal!")
    print("_ " * len(word))  # Initial display of the word

    while lives > 0 and word_letters:
        print("\nGuessed letters: ", " ".join(sorted(guessed_letters)))
        print(f"Lives remaining: {lives}")
        display_hangman(lives)

        # User input
        guess = input("Enter a letter or the full word: ").lower()

        if guess.isdigit():  # Check if the input is a number
            print("Invalid input! Please enter a letter or word.")
            continue

        if len(guess) == 1:  # Guessing a single letter
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in word_letters:
                print("Good guess!")
                word_letters.remove(guess)
                guessed_letters.add(guess)
            else:
                print("Incorrect guess.")
                guessed_letters.add(guess)
                lives -= 1
        elif guess == word:  # Guessing the full word
            print("Congratulations! You've guessed the word!")
            return
        else:
            print("Incorrect guess.")
            lives -= 1

        # Display current progress
        current_progress = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(current_progress))

    # Game over messages
    if word_letters:
        print(f"Game Over! Unfortunately you lost the game! The word was: {word}")
    else:
        print("Congratulations! You've won!")
    display_hangman(lives)


if __name__ == "__main__":
    play_hangman()
