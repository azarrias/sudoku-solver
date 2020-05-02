from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    all_digits = '123456789'
    values = [all_digits if c == '.' else c for c in grid]
    assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, values))

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved_boxes = [k for k in values.keys() if len(values[k]) == 1]
    for box in solved_boxes:
        value = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(value, '')
    return values

if __name__ == "__main__":
    sudoku_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    values = grid_values(sudoku_grid) 
    print("* Initial state:\n")
    display(values)
    print("\n* Apply elimination strategy:\n")
    values = eliminate(values)
    display(values)
