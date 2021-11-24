from . import pieces

class King(pieces.Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        positions = [[self.row - 1, self.column - 1],
                    [self.row - 1, self.column],
                    [self.row - 1, self.column + 1],
                    [self.row, self.column + 1],
                    [self.row + 1, self.column + 1],
                    [self.row + 1, self.column],
                    [self.row + 1, self.column - 1],
                    [self.row, self.column - 1],
                    ]
        for row, column in positions:
            self.movements(board, row, column)