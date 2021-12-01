from . import pieces

class Rook(pieces.Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)
        self.moved = False
        self.left_castle_possible = False
        self.right_castle_possible = False
    
    def set_moves(self, board):
        self.vertical_horizontal_moves(board)