from . import pieces

class King(pieces.Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)
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
            self.movements(board, row, column)

    def add_castling_moves(self, board):
        castling_positions_white =  [
                                    {"rook":[7, 0], "square1": [7, 3], "square2" : [7, 2], "possible_position": [7, 2]},
                                    {"rook":[7, 7], "square1": [7, 5], "square2" : [7, 6], "possible_position": [7, 6]}
                                    ]
                                
        castling_positions_black =  [
                                    {"rook":[0, 0], "square1": [0, 3], "square2" : [0, 2], "possible_position": [0, 2]},
                                    {"rook":[0, 7], "square1": [0, 5], "square2" : [0, 6], "possible_position": [0, 6]}
                                    ]

        if not self.moved:
            if self.color == 'white':
                castling_positions = castling_positions_white
            else:
                castling_positions = castling_positions_black

            for pos in castling_positions:
                print("True")
                piece = board.get_piece_from_position(pos["rook"][0], pos["rook"][1])
                if piece.__class__.__name__ == 'Rook' and piece.color == self.color: 
                    if not piece.moved:
                        self.possible_positions.append(pos["possible_position"][0], pos["possible_position"][1], None)
