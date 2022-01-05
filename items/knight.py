from . import pieces

class Knight(pieces.Pieces):
    def __init__(self, name, row, column, color, piece_type):
        super().__init__(name, row, column, color, piece_type)

    def set_moves(self, board):
        positions = [[ self.row - 1, self.column -2], # upward - left - 1 step
        [self.row + 1 , self.column -2],  # downward - right - 1 step 
        [self.row - 1 , self.column + 2], # upward - right - 1 step
        [self.row + 1 , self.column + 2],# downward - right - 1 step
        [self.row - 2 , self.column -1], # upward - left - 2 step,
        [self.row - 2 , self.column + 1],  # upward - right - 2 step
        [self.row + 2 , self.column  - 1],    # downward - left - 2 step
        [self.row + 2 , self.column  + 1]# downward - right - 2 step
        ]

        for row, column in positions:
            self.movements(board, row, column)