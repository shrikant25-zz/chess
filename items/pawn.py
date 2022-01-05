
from . import pieces

class Pawn(pieces.Pieces):
    def __init__(self, name, row, column, color, piece_type):
        self.passed = False
        self.can_do_enpassant = False
        super().__init__(name, row, column, color, piece_type)

    def set_moves(self, board):

        if board.enpassant_possible:
            self.update_enpassant_info(self, board)

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
    
    
    def update_enpassant_info(self, active_piece, board):
        target_piece = None
        for piece in board.pieces_list:
            if piece.piece_type == 'Pawn':
                if piece.passed and piece.color != active_piece.color and piece.alive:
                    target_piece = piece
                        
        if active_piece.piece_type == 'Pawn' and active_piece.can_do_enpassant:
            if active_piece.color == 'white':
                if not board.is_there_piece_on_position(target_piece.row - 1, target_piece.column):
                    active_piece.possible_positions.append([target_piece.row - 1, target_piece.column, target_piece])
    
            else:
                if active_piece.color == 'black':
                    if not board.is_there_piece_on_position(target_piece.row + 1, target_piece.column):
                        active_piece.possible_positions.append([target_piece.row + 1, target_piece.column, target_piece])
                
    def remove_enpassant_data(self, board, active_piece):
        board.enpassant_possible = False
        for piece in board.pieces_list:
            if piece.piece_type == 'Pawn':
                if piece.can_do_enpassant and piece.color == active_piece.color and piece.alive: # finding other pieces that can do enpssant
                    piece.can_do_enpassant = False
                if piece.passed and piece.color != active_piece.color and piece.alive:
                    piece.passed = False

    def check_if_passed(self, active_piece, board, new_row, new_column):

        if (active_piece.color == 'white' and active_piece.row - 2 == new_row) or (active_piece.color == 'black' and active_piece.row + 2 == new_row):
            
            if board.is_there_piece_on_position(new_row, new_column + 1):
                adjacent_piece1 = board.get_piece_from_position(new_row, new_column + 1)
                
                if adjacent_piece1.piece_type == 'Pawn' and adjacent_piece1.color != active_piece.color:
                    adjacent_piece1.can_do_enpassant = True
                    active_piece.passed = True
                    board.enpassant_possible = True
            
            if board.is_there_piece_on_position(new_row, new_column - 1):
                adjacent_piece1 = board.get_piece_from_position(new_row, new_column - 1)
                
                if adjacent_piece1.piece_type == 'Pawn' and adjacent_piece1.color != active_piece.color:
                    adjacent_piece1.can_do_enpassant = True
                    active_piece.passed = True
                    board.enpassant_possible = True