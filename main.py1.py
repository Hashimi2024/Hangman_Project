import random
import requests
from typing import List, Dict
from Hangman_pics import HANGMANPICS

# URLs for hangman pictures
HANGMAN_IMAGES = [
    "https://raw.githubusercontent.com/some-repository/hangman-images/step-0.txt",
    "https://raw.githubusercontent.com/some-repository/hangman-images/step-1.txt",
    # Add links for each step
]

# Load Hangman images as ASCII art from URLs
def load_images() -> List[str]:
    images = []
    for url in HANGMAN_IMAGES:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                images.append(response.text)
            else:
                images.append("Image not available")
        except Exception as e:
            images.append(f"Error loading image: {e}")
    return images

# Choose a random word from the pool
def choose_word(word_pool: List[str]) -> str:
    return random.choice(word_pool)

# Display the hangman stage
def display_hangman(lives: int, images: List[str]) -> None:
    print(images[10 - lives])

# Check if the guessed letter or word is correct
def check_guess(word: str, guess: str, guessed: List[str]) -> bool:
    if len(guess) == 1:  # Single letter
        return guess in word and guess not in guessed
    return guess == word  # Full word guess

# Main game function
def play_hangman(word_pool: List[str]) -> None:
    images = load_images()
    word = choose_word(word_pool).lower()
    guessed_letters = []
    lives = 10
    print(f"Welcome to Hangman! Your word has {len(word)} letters.")
    print("_ " * len(word))

    while lives > 0:
        print("\n" + " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print(f"Lives left: {lives}")
        guess = input("Enter a letter or word: ").lower()

        if not guess.isalpha() or len(guess) == 0:
            print("Invalid input. Please guess a letter or word.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again!")
            continue

        guessed_letters.append(guess)

        if check_guess(word, guess, guessed_letters):
            print(f"Good job! '{guess}' is in the word.")
            if all([letter in guessed_letters for letter in word]):
                print(f"Congratulations! You guessed the word '{word}'!")
                break
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is incorrect.")
            display_hangman(lives, images)

        if lives == 0:
            print(f"Game Over! The word was '{word}'. Better luck next time.")

# Word pool for the game
WORD_POOL = ["python", "hangman", "developer", "terminal", "coding"]

if __name__ == "__main__":
    play_hangman(WORD_POOL)

