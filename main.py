import random
from typing import List

word_pool = ["python", "hangman", "fastapi", "programming", "restaurant"]

# Function to display the current game state
def display_word(word: str, guessed_letters: List[str]) -> str:
    """
    Shows the word with unguessed letters hidden as underscores.

    Args:
        word (str): The word to guess.
        guessed_letters (List[str]): Letters guessed by the user.

    Returns:
        str: The word with underscores for unguessed letters.
    """
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to play the hangman game
def play_hangman(word_list: List[str], max_attempts: int = 10) -> None:
    """
    Main function to run the Hangman game.

    Args:
        word_list (List[str]): List of possible words for the game.
        max_attempts (int): Maximum number of incorrect attempts allowed.
    """
    # Randomly select a word
    word = random.choice(word_list).lower()
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print("Guess the word by guessing letters or the full word.")
    print(f"You have {max_attempts} incorrect attempts.")

    # Game loop
    while incorrect_guesses < max_attempts:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Enter a letter or guess the word: ").lower()

        # Validate input
        if not guess.isalpha():
            print("Invalid input. Please enter only letters.")
            continue

        if len(guess) == 1:  # Single letter guess
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try again!")
            elif guess in word:
                print(f"Good guess! '{guess}' is in the word.")
                guessed_letters.append(guess)
            else:
                print(f"Wrong guess! '{guess}' is not in the word.")
                guessed_letters.append(guess)
                incorrect_guesses += 1
        elif len(guess) == len(word):  # Full word guess
            if guess == word:
                print(f"Congratulations! You guessed the word: {word}")
                return
            else:
                print(f"Wrong guess! '{guess}' is not the word.")
                incorrect_guesses += 1
        else:
            print("Your guess doesn't match the word length. Try again.")

        print(f"Lives left: {max_attempts - incorrect_guesses}")

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return

    print(f"Game Over! The word was: {word}")

# Main function to start the game
if __name__ == "__main__":
    # word_pool = ["python", "hangman", "fastapi", "programming", "restaurant"]
    play_hangman(word_pool)
