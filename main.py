from hangman_pics import HANGMANPICS
import random
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
    word = random.choice(word_list()).lower()
    word_letters = set(word)
    guessed_letters = set()
    lives = 10
    print("\033[1;3mWelcome to Hangman!\033[0m")
    print("\033[1;3mPlease guess the name of an animal!\033[0m")
    print("_ " * len(word))

    while lives > 0 and word_letters:
        print("\nGuessed letters: ", " ".join(sorted(guessed_letters)))
        print(f"Lives remaining: {lives}")
        display_hangman(lives)

        guess = input("Enter a letter or the full word: ").lower()

        if guess.isdigit():
            print("Invalid input! Please enter a letter or word.")
            continue

        if len(guess) == 1:
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
        elif guess == word:
            print("\033[32mCongratulations! You've guessed the word!\033[0m")
            return
        else:
            print("Incorrect guess.")
            lives -= 1

        current_progress = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(current_progress))

    if word_letters:
        print(f"\033[31mGame Over! Unfortunately you lost the game! The word was: {word}\033[0m")
    else:
        print("\033[32mCongratulations! You've won!\033[0m")
    display_hangman(lives)


if __name__ == "__main__":
    play_hangman()
