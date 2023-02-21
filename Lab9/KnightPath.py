import pandas as pd


def read_input(filename):
    with open(filename) as input_file:
        m, n, x, y = map(int, input_file.readline().split())
    return m, n, x, y


def create_empty_board(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]


def find_allowed_moves(x, y):
    """
    Finds all allowed coordinates changes which doesn't across the board
    and lead to not visited positions
    :param x: current coordinate 'x' of horse
    :param y: current coordinate 'y' of horse
    :return: list[int] a list of allowed steps
    """
    allowed = []
    for step in coord_changes:
        if (0 <= x + step[0] < n) and (0 <= y + step[1] < m) and (board[y + step[1]][x + step[0]]) == 0:
            allowed.append(step)
    return allowed


def format_board(board):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chess_board_index = list(range(1, m+1))
    chess_board_columns = [alphabet[i] for i in range(n)]
    chess_board = pd.DataFrame(index=chess_board_index,
                               columns=chess_board_columns,
                               data=board)
    return chess_board.to_markdown()


def solve(m, n, x_0, y_0, board):
    """
    The function that find path for knight or decides that it's impossible.
    It uses the Vandorf's rule, according to it, horse should go to the coordinates with minimal amounts of possible
    next steps.
    :param m: length of chess board
    :param n: width of chess board
    :param x_0: start position 'x' coordinate
    :param y_0: start position 'y' coordinate
    :param board: chess board
    :return: The result of pah searching: board with steps if path exists phrase 'Маршрут не существует' in other case.
    """
    # Transforming coordinates to index view
    x = x_0 - 1
    y = y_0 - 1
    # Cycle where every iteration is a number of step
    for i in range(1, m * n + 1):
        # Writing the number of step on board
        board[y][x] = i
        # Choosing the next step according to rule
        next_step = None
        min_amount_of_next_steps = 9
        # Choosing step with yhe the smallest amount of next steps
        for move in find_allowed_moves(x, y):
            if not move:
                continue
            amount_of_next_steps = len(find_allowed_moves(x + move[0], y + move[1]))
            if amount_of_next_steps < min_amount_of_next_steps and (amount_of_next_steps != 0 or i == n * m - 1):
                min_amount_of_next_steps = amount_of_next_steps
                next_step = move
        if next_step is None:
            if i == m*n:
                return format_board(board)
            else:
                return "Маршрут не существует"
        x += next_step[0]
        y += next_step[1]


# Checking conditions:
m, n, x_0, y_0 = read_input("input.txt")

# All possible changes for knight coordinates
coord_changes = ((-2, -1), (2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (2, 1), (1, 2))

# Creating an empty board filled by zeros
board = create_empty_board(m, n)

# Solving the task
with open("output.txt", "w", encoding="utf-8") as output_file:
    solution = solve(m, n, x_0, y_0, board)
    output_file.write(solution)