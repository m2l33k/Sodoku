# Sudoku Solver

A simple Sudoku solver application built using Python and Tkinter. This app allows users to input a Sudoku puzzle and find the solution.

## Features

- Input Sudoku puzzles in a 9x9 grid.
- Solve the puzzle with a single click.
- Display the solution directly in the grid.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/m2l33k/Sudoku-App.git
    cd Sudoku-App
    ```

2. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

3. **Run the Application**: Execute the Python script to start the Sudoku Solver:

    ```bash
    python sudoku_app.py
    ```

## Code Overview

The `sudoku_app.py` script includes the following key components:

- **Sudoku Solver**: Implements a backtracking algorithm to solve the Sudoku puzzle.
- **Graphical User Interface**: Built with Tkinter, allows users to input puzzle values and view the solution.
- **Validation**: Ensures that entered values are valid Sudoku numbers.
