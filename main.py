def dfs_n_queens(n):
    # If n is less than 1, return an empty list
    if n < 1:
        return []

    solutions = []

    def is_safe(row, col, cols, diag1, diag2):
        # Check if placing a queen at (row, col) is safe
        if col in cols or (row + col) in diag1 or (row - col) in diag2:
            return False
        return True

    def backtrack(row, current_solution, cols, diag1, diag2):
        # If all queens are placed
        if row == n:
            solutions.append(current_solution[:])
            return
        for col in range(n):
            if is_safe(row, col, cols, diag1, diag2):
                # Place the queen
                current_solution.append(col)
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                # Move on to the next row
                backtrack(row + 1, current_solution, cols, diag1, diag2)

                # Backtrack
                current_solution.pop()
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

    backtrack(0, [], set(), set(), set())
    return solutions
