from . import pieces

class Pawn(pieces.Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):

        if self.color == 'white':
            diagonal_movements = [[self.row - 1, self.column - 1], [self.row - 1, self.column + 1]]
            if self.row == 6:
                row = self.row - 1
                row2 = self.row -2
                column = self.column
                self.straight_movement_beginning(board, row, row2, column)
            else:
                row = self.row - 1
                column = self.column
                if not board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                    self.possible_positions.append([row, column, None])
        else: 
            if self.color == 'black':
                diagonal_movements = [[self.row + 1, self.column - 1], [self.row + 1, self.column + 1]]
                if self.row == 1:
                    row = self.row + 1
                    row2 = self.row + 2
                    column = self.column
                    self.straight_movement_beginning(board, row, row2, column)
                else:
                    row = self.row + 1
                    column = self.column
                    if not board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                        self.possible_positions.append([row, column, None])

                        # diagonal movements
        for row , column in diagonal_movements:
            if board.is_there_piece_on_position(row, column)  and board.is_there_square_on_position(row, column):    
                self.movement_with_piece(board, row, column)
                
    def straight_movement_beginning(self, board, row, row2, column):
        if not board.is_there_piece_on_position(row, column)  and board.is_there_square_on_position(row, column):   
            self.possible_positions.append([row, column, None])
            if not board.is_there_piece_on_position(row2, column)  and board.is_there_square_on_position(row2, column):
                self.possible_positions.append([row2, column, None])