from . import pieces

class King(pieces.Pieces):
    def __init__(self, name, row, column, color, piece_type):
        super().__init__(name, row, column, color, piece_type)
        self.moved = False
        self.left_castle_possible = False
        self.right_castle_possible = False

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
            #print("king")
            self.movements(board, row, column)
        
        if not self.moved:
            if board.turn == "white":
                if not board.white_king_in_check:
                    self.add_castling_info(board)
            else:
                if board.turn == "black":
                    if not board.black_king_in_check:
                        self.add_castling_info(board)
        
        #print("in king")
        #for moves in self.possible_positions:
            #print(moves)
        #print("&&&&&&&&")            

    