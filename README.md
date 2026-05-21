# Hangman Game 🎯

A feature-rich text-based Hangman game built with Python as part of the **CodeAlpha Python Programming Internship**.

## How to Run

```bash
python hangman.py
```

> No external libraries needed. Works with Python 3.x out of the box.

## Features

- **4 Categories** — Animals, Programming, Countries, Movies
- **3 Difficulty Levels** — Easy (8 lives), Medium (6 lives), Hard (4 lives)
- **Hint System** — Request a clue; hints cost lives on Medium/Hard
- **Score Tracking** — Earn points each round based on lives remaining and difficulty
- **ASCII Art Gallows** — 8-stage drawing that updates with each wrong guess
- **Play Again Loop** — Keep playing and accumulate your score across rounds
- **Scoreboard** — Summary of points earned after every round

## How to Play

1. Choose a category (or pick Random)
2. Choose a difficulty level
3. Guess one letter at a time
4. Type `hint` for a clue (costs lives on Medium/Hard)
5. Type `quit` to exit the current round early

## Scoring

| Condition | Points |
|---|---|
| Base win | 10 pts |
| Per life remaining | +2 pts |
| Medium difficulty bonus | +5 pts |
| Hard difficulty bonus | +10 pts |
| Loss | 0 pts |

## Concepts Used

`random`, `while` loops, `if-else`, strings, lists, dictionaries, functions

## Project Structure

```
CodeAlpha_HangmanGame/
└── hangman.py
```

## Internship Details

- **Organization:** CodeAlpha
- **Domain:** Python Programming
- **Student ID:** CA/DF1/75758
- **Duration:** 20th May 2026 – 20th June 2026
