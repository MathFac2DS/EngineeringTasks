# Warm-Up Challenge — Terminal Tic-Tac-Toe

## Overview

Build a simple terminal-based Tic-Tac-Toe game.

This is a lightweight warm-up exercise designed to practice:

- Working with a 2D grid (matrix)
- Rendering output cleanly in the terminal
- Handling user input and validation
- Managing game state
- Implementing basic win-detection logic

You may use **any programming language** you’re comfortable with.

---

## What We Care About

- Clean and readable code (without using AI to write the code for you)
- Correct use of a 2D data structure
- Careful handling of coordinates
- Correct win detection
- Clear separation of responsibilities
- Steady progress and systematic testing
- Speed (time yourself to see how much you can complete in 1 hour)


---

## Game Rules

- The board is **3 x 3**
- The human player is **`X`**
- The computer is **`O`**
- The computer selects a **random available square**
- The game ends when:
  - A player gets 3 in a row (horizontal, vertical, or diagonal)
  - The board is full (draw)

---

## Board Rendering

You must display the board clearly after each move.

Example format (you may choose a different clean format):

    0 1 2
    0 . . .
    1 . . .
    2 . . .

or

    . | . | .
    . | . | .
    . | . | .
    

Empty squares must be visually distinguishable.

Rendering should remain consistent throughout the game.

---

## Player Move

Prompt the user to enter a move:
    enter row and column


Input example:

    1 2 


You must:

- Parse the input
- Validate that:
  - Row and column are in bounds
  - The square is not already occupied
- Update the board if valid
- Re-prompt if invalid

---

## Computer Move

After the user’s move:

- Randomly select one of the remaining empty squares
- Update the board
- Re-render the board

No AI or strategy is required — random selection is sufficient.

---

## Win Detection

You must detect wins in:

- All rows
- All columns
- Both diagonals

When someone wins, print:

    X wins!

or

    O wins!


If the board fills without a winner:

    Draw!


The game should terminate after a win or draw.

---

## Requirements

- Use a proper 2D data structure to represent the board.
- Keep rendering logic separate from game logic if possible.
- Avoid hardcoding repeated logic unnecessarily.
- Validate input carefully.
- Keep the implementation simple and clear.

You do **not** need to implement:

- Minimax or optimal play
- Advanced UI
- Persistent storage
- Networking