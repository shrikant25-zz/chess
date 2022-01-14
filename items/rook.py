from . import pieces

class Rook(pieces.Pieces):
    def __init__(self, name, row, column, color, piece_type):
        super().__init__(name, row, column, color, piece_type)
        self.moved = False
    
    def set_moves(self, board):
        self.vertical_horizontal_moves(board)

        if not self.moved:
            if board.turn == "white":
                if not board.white_king_in_check:
                    self.add_castling_info(board)
            else:
                if board.turn == "black":
                    if not board.black_king_in_check:
                        self.add_castling_info(board)