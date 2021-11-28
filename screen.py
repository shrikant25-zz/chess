import pygame
from chessboard import Board
from cases import *


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

    def mouse_up(self, active_piece):
        pos = pygame.mouse.get_pos()
        row, column = self.get_row_col_from_pos(pos)
        if (row != None and column != None) and (row!= active_piece.row or column != active_piece.column):
            self.make_move(row, column, active_piece)

    def select_piece(self, row, column):
        # check if king got check
        active_piece = self.board.get_piece_from_position(row, column)
        if active_piece and self.board.turn == active_piece.color:
            active_piece.active = True
            square = self.board.get_square_from_position(row, column)
            square.active = True
            if self.board.enpassant_possible:
                update_enpassant_info(active_piece, self.board)
            
            active_piece.update_board_objects(self.board)
            
    def make_move(self, row, column, active_piece):
        possible_squares = self.board.get_possible_squares()
        pieces_inpath = self.board.get_pieces_inpath()
    
        for possible_row, possible_column, possible_victim in active_piece.possible_positions:           
            if possible_row == row and possible_column == column:
        
                if active_piece.__class__.__name__ == 'Pawn':
                    if self.board.enpassant_possible:
                        remove_enpassant_data(self.board, active_piece)
                    check_if_passed(active_piece, self.board, row, column)

                active_piece.row = row
                active_piece.column = column

                if possible_victim:
                    possible_victim.alive = False

                if active_piece.color == 'white':
                    self.board.turn = 'black' 
                else:
                    self.board.turn = 'white'
                break

        for piece in pieces_inpath:
            piece.inpath = False

        for square in possible_squares:
            square.possible_position = False
        
        if self.board.king_under_check:
            self.board.king_under_check = False

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
       
    def update_board_display(self):
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

    
    














