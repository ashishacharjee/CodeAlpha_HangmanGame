import random

words = ["python", "guitar", "mountain", "keyboard", "elephant"]

stages = [
    "\n   -----\n   |   |\n       |\n       |\n       |\n       |\n--------",
    "\n   -----\n   |   |\n   O   |\n       |\n       |\n       |\n--------",
    "\n   -----\n   |   |\n   O   |\n   |   |\n       |\n       |\n--------",
    "\n   -----\n   |   |\n   O   |\n  /|   |\n       |\n       |\n--------",
    "\n   -----\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n--------",
    "\n   -----\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n--------",
    "\n   -----\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n--------",
]


def display_word(guessed, word):
    return " ".join(letter if letter in guessed else "_" for letter in word)


def hangman():
    word = random.choice(words)
    guessed = set()
    wrong = 0
    max_wrong = 6

    print("\n Welcome to Hangman!")
    print(f" Guess the word. You have {max_wrong} wrong guesses allowed.\n")

    while wrong < max_wrong:
        print(stages[wrong])
        print(f"\n Word : {display_word(guessed, word)}")
        print(f" Wrong: {wrong}/{max_wrong}")
        print(f" Tried: {', '.join(sorted(guessed)) if guessed else 'none'}\n")

        if all(letter in guessed for letter in word):
            print(f" You got it! The word was: '{word}'")
            return

        guess = input(" Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print(" Enter a single letter only.\n")
            continue

        if guess in guessed:
            print(f" Already tried '{guess}'. Pick another.\n")
            continue

        guessed.add(guess)

        if guess in word:
            print(f" Yes! '{guess}' is in the word.\n")
        else:
            wrong += 1
            print(f" Nope, '{guess}' is not in the word.\n")

    print(stages[max_wrong])
    print(f"\n Game over! The word was: '{word}'")


if __name__ == "__main__":
    while True:
        hangman()
        again = input("\n Play again? (yes/no): ").lower().strip()
        if again != "yes":
            print(" Thanks for playing! Goodbye.")
            break
