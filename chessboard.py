import pygame
from items import *
import squares
from colors import color

class Board():
    def __init__(self, window, square_dimensions, borderline, turn):
        self.window = window
        self.square_dimensions = square_dimensions
        self.borderline = borderline
        self.turn = turn
        self.black_king_in_check = False
        self.white_king_in_check = False
        self.enpassant_possible = False
        self.pieces_list = []
        self.squares_list = []
        self.squares_under_attack = []
    
    def create_board(self, rows, columns):
        for i in range(2):
            even = i%2 ==0
            piece_color =  (('white', 'black')[even] )
            pawn_row = ((6,1) [even])
            other_row = ((7,0) [even])
            
            self.pieces_list.append(queen.Queen(piece_color+"_queen", other_row, 3, piece_color, "Queen"))
            self.pieces_list.append(king.King(piece_color+"_king", other_row, 4, piece_color, "King"))
           
            for j in range(8):
                self.pieces_list.append(pawn.Pawn(piece_color+"_pawn"+str(j+1), pawn_row, j, piece_color, "Pawn"))
                if j < 2:
                   
                    column = ((0,7) [j%2 ==0])
                    self.pieces_list.append(rook.Rook(piece_color+"_rook"+str(j+1), other_row, column, piece_color, "Rook"))
                    
                    column = ((1,6) [j%2 ==0])
                    self.pieces_list.append(knight.Knight(piece_color+"_knight"+str(j+1), other_row, column, piece_color, "Knight"))
                    
                    column = ((2,5) [j%2 ==0])
                    self.pieces_list.append(bishop.Bishop(piece_color+"_bishop"+str(j+1), other_row, column, piece_color, "Bishop"))
                
        for row in range(rows):
            for column in range(columns):
                square_color = (('dark_silver', 'dark_red') [(row+column) & 1])
                self.squares_list.append(squares.Square(row, column, square_color))
                               
    def draw_square(self, square_color, row, column):
        rect = ((column * self.square_dimensions)+self.borderline, 
                (row * self.square_dimensions)+self.borderline, self.square_dimensions, self.square_dimensions)
            # adding distance equal to borderline in starting points of sqaure shifts them enough to have place for a borderline 
        if square_color != 'dark_silver' and square_color != 'dark_red':
            pygame.draw.rect(self.window, color[square_color], rect)
            square_color = 'black'
            pygame.draw.rect(self.window, color[square_color], rect,5)
        else:
            pygame.draw.rect(self.window, color[square_color], rect)

    def display_piece_on_board(self, piece, row, column):
        position_on_chessboard =((column * self.square_dimensions) + self.borderline*2, 
                (row * self.square_dimensions) + self.borderline*2)
        path = r'C:\Users\Shrikant\projects\chess\images'
        piece_image = pygame.image.load(path + "\\" + piece.name + ".png")
        piece_image = pygame.transform.scale(piece_image, (67, 67))
        self.window.blit(piece_image, position_on_chessboard)

    def is_there_piece_on_position(self, row, column):
        for piece in self.pieces_list:
            if piece.row == row and piece.column == column and piece.alive:
                return True
        return False
    
    def get_piece_from_position(self, row, column):
        for piece in self.pieces_list:
            if piece.row == row and piece.column == column and piece.alive:
                return piece
        return None

    def get_square_from_position(self, row, column):
        for square in self.squares_list:
            if square.row == row and square.column == column:
                return square
        return None
    
    def is_there_square_on_position(self, row, column):
        for square in self.squares_list:
            if square.row == row and square.column == column:
                return True
        return False

    def get_active_square(self):
        for square in self.squares_list:
            if square.active is True:
                return square
        return None

    def get_active_piece(self):
        for piece in self.pieces_list:
            if piece.active is True and piece.alive:
                return piece
        return None

    def get_pieces_inpath(self):
        pieces_inpath = []
        for piece in self.pieces_list:
            if piece.inpath is True and piece.alive:
                pieces_inpath.append(piece)
        return pieces_inpath

    def get_possible_squares(self):
        possible_squares = []
        for square in self.squares_list:
            if square.possible_position is True:
                possible_squares.append(square)
        return possible_squares
    
    def promote(self, active_piece, possible_row, possible_column):
        piece_color = active_piece.color
        active_piece.active = False
        active_piece.alive = False
        self.pieces_list.remove(active_piece)
        new_piece = queen.Queen(piece_color+"_queen", possible_row, possible_column, piece_color, "Queen")
        self.pieces_list.append(new_piece)
        new_piece.active = True
        return new_piece
    
    def is_king_under_attack(self):
        for piece in self.pieces_list:
            if piece.color != self.turn and piece.alive:
                piece.set_moves(self)
                for _, _, opposite_piece_under_attack in piece.possible_positions:
                    if opposite_piece_under_attack:
                        if opposite_piece_under_attack.piece_type == 'King':
                            return True
        return False

    def is_the_square_safe(self, piece, square):

        if self.is_there_piece_on_position(square[0], square[1]):
            return False

        for opposite_piece in self.pieces_list:
            
            if opposite_piece.color != piece.color:
            
                for square_under_attack in self.squares_under_attack:
                    if square[0] == square_under_attack.row and square[1] == square_under_attack.column:
                            return False
                    
        return True 