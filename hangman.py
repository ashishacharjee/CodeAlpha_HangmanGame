import random

# ─────────────────────────────────────────────
#  Word bank — category : [(word, hint), ...]
# ─────────────────────────────────────────────
WORD_BANK = {
    "Animals": [
        ("elephant", "The largest land animal on Earth"),
        ("dolphin",  "A highly intelligent marine mammal"),
        ("penguin",  "A flightless bird found in Antarctica"),
        ("cheetah",  "The fastest land animal"),
        ("kangaroo", "A marsupial native to Australia"),
    ],
    "Programming": [
        ("python",    "A popular high-level programming language"),
        ("variable",  "A container that stores data values"),
        ("function",  "A reusable block of code"),
        ("algorithm", "A step-by-step problem-solving procedure"),
        ("database",  "An organised collection of structured data"),
    ],
    "Countries": [
        ("brazil",   "The largest country in South America"),
        ("germany",  "Home of Oktoberfest and the Autobahn"),
        ("japan",    "Known as the Land of the Rising Sun"),
        ("nigeria",  "The most populous country in Africa"),
        ("iceland",  "Famous for its geysers and northern lights"),
    ],
    "Movies": [
        ("inception",   "A 2010 Christopher Nolan mind-bending thriller"),
        ("interstellar","A space epic also directed by Christopher Nolan"),
        ("avatar",      "A 2009 film set on the moon Pandora"),
        ("titanic",     "A 1997 film about a doomed ocean liner"),
        ("gladiator",   "A 2000 Russell Crowe Roman epic"),
    ],
}

DIFFICULTY = {
    "easy":   {"lives": 8,  "hint_penalty": 0},
    "medium": {"lives": 6,  "hint_penalty": 1},
    "hard":   {"lives": 4,  "hint_penalty": 2},
}

STAGES = [
    """
   ┌─────┐
   │     │
         │
         │
         │
         │
  ═══════════""",
    """
   ┌─────┐
   │     │
   O     │
         │
         │
         │
  ═══════════""",
    """
   ┌─────┐
   │     │
   O     │
   │     │
         │
         │
  ═══════════""",
    """
   ┌─────┐
   │     │
   O     │
  /│     │
         │
         │
  ═══════════""",
    """
   ┌─────┐
   │     │
   O     │
  /│\\    │
         │
         │
  ═══════════""",
    """
   ┌─────┐
   │     │
   O     │
  /│\\    │
  /      │
         │
  ═══════════""",
    """
   ┌─────┐
   │     │
   O     │
  /│\\    │
  / \\    │
         │
  ═══════════""",
    """
   ┌─────┐
   │     │
  [O]    │
  /│\\    │
  / \\    │
         │
  ═══════════  ← Final warning!""",
    """
   ┌─────┐
   │     │
  [X]    │
  /│\\    │
  / \\    │
         │
  ═══════════  ✗ GAME OVER""",
]


def display_word(guessed, word):
    return "  ".join(letter if letter in guessed else "_" for letter in word)


def choose_category():
    categories = list(WORD_BANK.keys())
    print("\n  Choose a category:")
    for i, cat in enumerate(categories, 1):
        print(f"    {i}. {cat}")
    print(f"    {len(categories)+1}. Random (surprise me!)")

    while True:
        choice = input("\n  Enter number: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(categories):
                return categories[idx - 1]
            elif idx == len(categories) + 1:
                return random.choice(categories)
        print("  Invalid choice. Try again.")


def choose_difficulty():
    print("\n  Choose difficulty:")
    print("    1. Easy   (8 lives, hints are free)")
    print("    2. Medium (6 lives, hints cost 1 life)")
    print("    3. Hard   (4 lives, hints cost 2 lives)")

    mapping = {"1": "easy", "2": "medium", "3": "hard"}
    while True:
        choice = input("\n  Enter number: ").strip()
        if choice in mapping:
            return mapping[choice]
        print("  Invalid choice. Try again.")


def show_status(wrong, max_lives, guessed, word, category, difficulty, hint_used):
    stage_index = min(wrong, len(STAGES) - 1)
    print(STAGES[stage_index])
    print(f"\n  Category   : {category}")
    print(f"  Difficulty : {difficulty.capitalize()}")
    print(f"  Lives left : {'❤  ' * (max_lives - wrong)}{'♡  ' * wrong}")
    print(f"\n  Word  : {display_word(guessed, word)}")
    print(f"  Tried : {', '.join(sorted(guessed)) if guessed else 'none'}")
    if hint_used:
        print(f"  Hint  : (already revealed)")


def play_round(scores):
    print("\n" + "═" * 45)
    print("           HANGMAN ")
    print("═" * 45)

    category  = choose_category()
    difficulty = choose_difficulty()
    max_lives  = DIFFICULTY[difficulty]["lives"]
    hint_cost  = DIFFICULTY[difficulty]["hint_penalty"]

    word, hint = random.choice(WORD_BANK[category])
    guessed    = set()
    wrong      = 0
    hint_used  = False

    print(f"\n  A {len(word)}-letter word has been chosen. Good luck!\n")

    while wrong < max_lives:
        show_status(wrong, max_lives, guessed, word, category, difficulty, hint_used)

        # Win check
        if all(letter in guessed for letter in word):
            bonus = max_lives - wrong
            points = 10 + (bonus * 2) + (5 if difficulty == "medium" else 10 if difficulty == "hard" else 0)
            print(f"\n  ✅ You guessed it! The word was: '{word.upper()}'")
            print(f"  🏆 Points earned this round: {points}")
            scores.append(points)
            return True

        print("\n  Options: [letter] to guess  |  [hint] for a clue  |  [quit] to exit\n")
        action = input("  Your input: ").lower().strip()

        if action == "quit":
            print("\n  Quitting current round...")
            return False

        if action == "hint":
            if hint_used:
                print("  You've already used your hint!")
            else:
                if hint_cost > 0 and wrong + hint_cost >= max_lives:
                    print(f"  Not enough lives to use hint (costs {hint_cost} life/lives).")
                else:
                    hint_used = True
                    wrong += hint_cost
                    print(f"\n  💡 Hint: {hint}")
                    if hint_cost > 0:
                        print(f"  (Cost: {hint_cost} life/lives)")
            continue

        if len(action) != 1 or not action.isalpha():
            print("  Please enter a single letter, 'hint', or 'quit'.")
            continue

        if action in guessed:
            print(f"  You already tried '{action}'. Pick another letter.")
            continue

        guessed.add(action)

        if action in word:
            print(f"  ✔  '{action}' is in the word!")
        else:
            wrong += 1
            remaining = max_lives - wrong
            print(f"  ✘  '{action}' is not in the word. {remaining} life/lives remaining.")

    # Lose
    show_status(wrong, max_lives, guessed, word, category, difficulty, hint_used)
    print(f"\n  💀 Out of lives! The word was: '{word.upper()}'")
    print(f"  💡 Hint was: {hint}")
    scores.append(0)
    return False


def show_scoreboard(scores):
    if not scores:
        return
    print("\n  ─── Scoreboard ───────────────────")
    for i, s in enumerate(scores, 1):
        print(f"    Round {i}: {s} points")
    print(f"    Total : {sum(scores)} points")
    print("  ──────────────────────────────────")


def main():
    scores = []
    print("\n  Welcome to Hangman! Guess the hidden word before the man is hanged.")

    while True:
        play_round(scores)
        show_scoreboard(scores)

        again = input("\n  Play another round? (yes/no): ").lower().strip()
        if again != "yes":
            print("\n  Thanks for playing! Final score:", sum(scores), "points.")
            print("  Goodbye! 👋\n")
            break


if __name__ == "__main__":
    main()
