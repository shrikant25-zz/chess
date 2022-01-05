from . import pieces

class Queen(pieces.Pieces):
    def __init__(self, name, row, column, color, piece_type):
        super().__init__(name, row, column, color, piece_type)

    def set_moves(self, board):
        self.vertical_horizontal_moves(board)
        self.diagonal_moves(board)