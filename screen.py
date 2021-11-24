import pygame
from chessboard import Board

class Screen():
    def __init__(self, square_dimensions, rows, columns, window, borderline):
        self.square_dimensions = square_dimensions
        self.rows = rows
        self.columns = columns
        self.window = window
        self.borderline = borderline
        self.board = Board(self.window, self.square_dimensions, self.borderline, 'white')

    def mouse_down(self):
        pos = pygame.mouse.get_pos()
        row, column = self.get_row_col_from_pos(pos)
        if row != None and column!= None:
            self.select_piece(row, column)

    def mouse_up(self):
        pos = pygame.mouse.get_pos()
        row, column = self.get_row_col_from_pos(pos)
        active_piece = self.board.get_active_piece()
        if (row != None and column != None) and (row!= active_piece.row or column != active_piece.column):
            self.make_move(row, column, active_piece)

    def select_piece(self, row, column):
        # check if king got check
        active_piece = self.board.get_piece_from_position(row, column)
        if active_piece and self.board.turn == active_piece.color:
            active_piece.active = True
            square = self.board.get_square_from_position(row, column)
            square.active = True
            self.check_game_status(active_piece)
            
    def make_move(self, row, column, active_piece):
        possible_squares = self.board.get_possible_squares()
        pieces_inpath = self.board.get_pieces_inpath()
        for square in possible_squares:
            square.possible_position = False
            if square.row == row and square.column == column:
                active_piece.row = row
                active_piece.column = column
                for piece in pieces_inpath:
                    if piece.row == row and piece.column == column:
                        piece.alive = False
                if active_piece.color == 'white':
                    self.board.turn = 'black'
                if active_piece.color == 'black':
                    self.board.turn = 'white'
        for piece in pieces_inpath:
            piece.inpath = False
        active_piece.active = False
        active_square = self.board.get_active_square()
        active_square.active = False
        active_piece.possible_positions = []
    
    def get_row_col_from_pos(self, pos): # gets cursor position
        x, y = pos
        row = y // self.square_dimensions 
        col = x // self.square_dimensions 
        if row >= self.rows or col >= self.columns:
            return None, None
        return row, col
       
    def update_board(self):
        for square in self.board.squares_list:
            if square.possible_position is True:
                square.color = 'faint_blue'
            if square.color == 'faint_blue' and square.possible_position is False:
                square.color =  (('dark_silver', 'dark_red') [(square.row+square.column) & 1])
            if square.active is True:
                square.color = 'faint_green'
            if square.color == 'faint_green' and square.active is False:
                square.color =  (('dark_silver', 'dark_red') [(square.row+square.column) & 1])
            self.board.draw_square(square.color, square.row, square.column)
        for piece in self.board.pieces_list:
            if piece.alive == False:
                continue
            self.board.display_piece_on_board(piece, piece.row, piece.column)
        pygame.display.update()

    def check_game_status(self, our_piece):
        available_positions = []
        our_piece.set_moves(self.board)
        our_original_row = our_piece.row
        our_original_column = our_piece.column

        for our_possible_row, our_possible_column, opposite_piece_under_attack in our_piece.possible_positions:
            king_in_check = False
            our_piece.row = our_possible_row
            our_piece.column = our_possible_column
            if opposite_piece_under_attack:
                opposite_piece_under_attack.alive = False
            for opposite_piece in self.board.pieces_list:
                if self.board.turn != opposite_piece.color and opposite_piece.alive:
                    opposite_piece.set_moves(self.board)
                    for _, _, our_piece_under_attack in opposite_piece.possible_positions:
                        if our_piece_under_attack.__class__.__name__ == 'King':
                            king_in_check = True
                            break
                opposite_piece.possible_positions = []
                if king_in_check:
                    break
            
            if opposite_piece_under_attack:
                opposite_piece_under_attack.alive = True
            if not king_in_check:
                available_positions.append([our_possible_row, our_possible_column, opposite_piece_under_attack])
        
        our_piece.row = our_original_row
        our_piece.column = our_original_column
        our_piece.possible_positions = available_positions
        our_piece.update_board_objects(self.board)