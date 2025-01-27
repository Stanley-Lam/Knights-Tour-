# Knights-Tour-
CSC 202 Data Structures Knights Tour Project

Description: In chess, a knight is a piece that moves either two squares vertically and one square horizontally, or vice versa, "jumping" over any other pieces in the way. A knight's tour is a sequence of moves such that a knight, starting from a given square in a given board, explores each and every empty square exactly once.

Base Case: If the board has 0 empty squares, then there exists a knight's tour.

Recursive Case: If the board has n empty squares, then up to 8 possibilities exist. If the knight has valid moves and, for some valid moves, the resulting board with n - 1 squares has a night's tour, then there exists a knight's tour. Else, there does not exist a knight's tour.
