from . import pieces

class Bishop(pieces.Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        self.diagonal_moves(board)