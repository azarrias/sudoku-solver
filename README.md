# Sudoku solver
This is an AI agent that solves sudokus, by using Depth-First Search and propagation, iterating with elimination and only choice strategies.

# How to use
There are no prerequisites, so there is no need for virtual environments, only python3 and git are needed:

```
git clone https://github.com/azarrias/sudoku-solver.git
cd sudoku-solver
cd src && python solution.py
```

The sudoku grid to be solved is hard-coded in main:

```
sudoku_grid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
```

which is a single line string representation in row-major order.

So, it is possible to change the value for sudoku_grid, as long as the value represents a valid sudoku grid (otherwise it won't be possible for the agent to solve it).
