```markdown
# N-Queens Solver using Depth-First Search (DFS)

## Overview
This Python project implements a solution to the classic N-Queens problem using a depth-first search (DFS) backtracking algorithm. The goal is to place N queens on an N×N chessboard such that no two queens threaten each other — that is, no two queens share the same row, column, or diagonal.

## Functionality
- The main function `dfs_n_queens(n)` returns all possible solutions for a given size `n`.
- Each solution is represented as a list of length `n`, where the element at index `i` indicates the column position of the queen in row `i`.
- If `n` is less than 1, the function returns an empty list.

## Usage
```python
solutions = dfs_n_queens(4)
print(solutions)
# Output: [[1, 3, 0, 2], [2, 0, 3, 1]]
``

## Implementation Details
- Uses recursion and backtracking to explore all possible placements.
- Maintains sets to track threatened columns and diagonals for efficient conflict detection.
- Checks each row for safe placement before proceeding.

## User Stories & Behavior
- Handles edge cases where `n < 1` by returning an empty list.
- Finds all solutions for `n = 1` through `n = 8`, matching known solutions.
- Efficiently computes solutions for larger `n`, such as 8, which has 92 solutions.

## Example Tests
```python
print(dfs_n_queens(1))  # [[0]]
print(dfs_n_queens(2))  # []
print(dfs_n_queens(3))  # []
print(dfs_n_queens(4))  # [[1, 3, 0, 2], [2, 0, 3, 1]]
print(len(dfs_n_queens(8)))  # 92 solutions
``

## License
This project is for educational purposes and can be freely used and modified.

---

Feel free to extend or optimize this solution further!
