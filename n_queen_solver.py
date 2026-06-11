import time


def print_board(board):
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == "Q":
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_first_solution(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            if solve_first_solution(board, row + 1, n):
                return True

            board[row][col] = "."

    return False


def solve_all_solutions(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            solve_all_solutions(board, row + 1, n, solutions)

            board[row][col] = "."


def create_board(n):
    return [["." for _ in range(n)] for _ in range(n)]


def get_board_size():
    try:
        n = int(input("Enter board size: "))

        if n < 1:
            print("Board size must be positive.")
            return None

        return n

    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def find_first_solution():
    n = get_board_size()

    if n is None:
        return

    start = time.time()

    board = create_board(n)

    if solve_first_solution(board, 0, n):
        end = time.time()
        print("\nFirst solution found:\n")
        print_board(board)
        print(f"\nTime taken: {end - start:.4f} seconds")
    else:
        print("No solution found.")


def find_all_solutions():
    n = get_board_size()

    if n is None:
        return

    start = time.time()

    board = create_board(n)
    solutions = []

    solve_all_solutions(board, 0, n, solutions)

    end = time.time()

    if solutions:
        for index, solution in enumerate(solutions, 1):
            print(f"\nSolution {index}:\n")
            print_board(solution)

        print(f"\nTotal solutions: {len(solutions)}")
        print(f"Time taken: {end - start:.4f} seconds")
    else:
        print("No solution found.")


def count_solutions():
    n = get_board_size()

    if n is None:
        return

    start = time.time()

    board = create_board(n)
    solutions = []

    solve_all_solutions(board, 0, n, solutions)

    end = time.time()

    print(f"\nTotal solutions for N = {n}: {len(solutions)}")
    print(f"Time taken: {end - start:.4f} seconds")


def save_solutions_to_file():
    n = get_board_size()

    if n is None:
        return

    start = time.time()

    board = create_board(n)
    solutions = []

    solve_all_solutions(board, 0, n, solutions)

    end = time.time()

    file_name = f"n_queen_solutions_{n}.txt"

    with open(file_name, "w") as file:
        file.write(f"N-Queen Solutions for N = {n}\n")
        file.write(f"Total solutions: {len(solutions)}\n")
        file.write(f"Time taken: {end - start:.4f} seconds\n\n")

        for index, solution in enumerate(solutions, 1):
            file.write(f"Solution {index}:\n\n")

            for row in solution:
                file.write(" ".join(row) + "\n")

            file.write("\n")

    print(f"\n{len(solutions)} solutions saved to {file_name}")
    print(f"Time taken: {end - start:.4f} seconds")


def show_statistics():
    n = get_board_size()

    if n is None:
        return

    start = time.time()

    board = create_board(n)
    solutions = []

    solve_all_solutions(board, 0, n, solutions)

    end = time.time()

    print("\n===== Statistics =====")
    print(f"Board Size: {n}")
    print(f"Total Solutions: {len(solutions)}")
    print(f"Time Taken: {end - start:.4f} seconds")


def main():
    while True:
        print("\n===== N-Queen Solver Pro =====")
        print("1. Find first solution")
        print("2. Find all solutions")
        print("3. Count solutions")
        print("4. Save solutions to file")
        print("5. Show statistics")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            find_first_solution()

        elif choice == "2":
            find_all_solutions()

        elif choice == "3":
            count_solutions()

        elif choice == "4":
            save_solutions_to_file()

        elif choice == "5":
            show_statistics()

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


main()