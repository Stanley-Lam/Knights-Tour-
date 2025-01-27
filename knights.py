# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#checks for a move within the bounds of the board
def is_within_bound(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0])

def find_tour(board, row, col):
    """
    Find a knight's tour in a chessboard.
    TODO: Complete this function. It must be recursive, and it must not
          modify the given board.

    :param board: A rectangular board where empty squares are set to None
    :param row: A knight's row index within the board
    :param col: A knight's column index within the board
    :return: A list of (row, col) pairs forming a tour, None if no tour exists
    """
    movement = [(1, -2), (-1, -2), (-2, 1), (-2, -1), (-1, 2), (1, 2), (2, -1), (2, 1)]
    if board == None or len(board) == 0 or len(board[0]) == 0:
        return None
    def tour_helper(board, row, col, tour):
        tour.append((row, col))


        if len(tour) == sum(1 for row in board for cell in row if cell is None) + 1:
            return tour

        for m in movement:
            next_row, next_col = row + m[0], col + m[1]
            if is_within_bound(board, next_row, next_col) and board[next_row][next_col] is None:
                result = tour_helper(board, next_row, next_col, tour)
                if result:
                    return result

        tour.pop()
        return None

    return tour_helper(board, row, col, [])

def check_tour(board, tour):
    """
    Check a knight's tour in a chessboard.
    TODO: Complete this function. It must be recursive, and it must not
          modify the given board.

    :param board: A rectangular board where empty squares are set to None
    :param tour: A list of (row, col) pairs
    :return: Whether or not the list of pairs forms a tour
    """
    movement = [(1, -2), (-1, -2), (-2, 1), (-2, -1), (-1, 2), (1, 2), (2, -1), (2, 1)]
    if tour == None or len(tour) == 0:
        return False

    for i in range(1, len(tour)):
        previous_row, previous_col = tour[i-1]
        current_row, current_col = tour[i]
        if (current_row - previous_row, current_col - previous_col) not in movement:
            return False

        empty_cells = sum(1 for row in board for cell in row if cell is None) + 1
        if len(tour) != empty_cells:
            return False
    return True


#Notes
# when knights moves to a new square, the previous square can be interpreted as occupied
# moving creates a smaller problem because the previous square becomes occupied
# moving is the recursive behavior
# a solution will be a list of airs forming a tour including the starting coordinate