import pygame
import pieces
import squares
from colors import color

class Board():
    def __init__(self, window, square_dimensions, borderline, turn):
        self.window = window
        self.square_dimensions = square_dimensions
        self.borderline = borderline
        self.turn = turn
        self.pieces_list = []
        self.squares_list = []
    
    def create_board(self, rows, columns):
        for i in range(2):
            even = i%2 ==0
            piece_color =  (('white', 'black')[even] )
            pawn_row = ((6,1) [even])
            other_row = ((7,0) [even])
            
            self.pieces_list.append(pieces.Queen(piece_color+"_queen", other_row, 3, piece_color))
            self.pieces_list.append(pieces.King(piece_color+"_king", other_row, 4, piece_color))
            for j in range(8):
                self.pieces_list.append(pieces.Pawn(piece_color+"_pawn"+str(j+1), pawn_row, j, piece_color))
                if j < 2:
                    column = ((0,7) [j%2 ==0])
                    self.pieces_list.append(pieces.Rook(piece_color+"_rook"+str(j+1), other_row, column, piece_color))
                    column = ((1,6) [j%2 ==0])
                    self.pieces_list.append(pieces.Knight(piece_color+"_knight"+str(j+1), other_row, column, piece_color))
                    column = ((2,5) [j%2 ==0])
                    self.pieces_list.append(pieces.Bishop(piece_color+"_bishop"+str(j+1), other_row, column, piece_color))
                
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

    def remove_piece_from_board(self, piece):
        square_color = (('dark_silver', 'dark_red') [(piece.row + piece.column) & 1])
        self.draw_square(square_color, piece.row, piece.column)

    def is_there_piece_on_position(self, row, column):
        for piece in self.pieces_list:
            if piece.row == row and piece.column == column:
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

    def get_blocking_pieces(self):
        blocking_pieces = []
        for piece in self.pieces_list:
            if piece.blocking_piece is True:
                blocking_pieces.append(piece)
        return blocking_pieces

    def get_possible_squares(self):
        possible_squares = []
        for square in self.squares_list:
            if square.possible_position is True:
                possible_squares.append(square)
        return possible_squares

    
            

          
          






























"""def create_pieces(self): 
        self.pieces_list.append(pieces.Pawn("white_pawn1", 6, 0, 'white'))
        self.pieces_list.append(pieces.Pawn("white_pawn2", 6, 1, 'white'))
        self.pieces_list.append(pieces.Pawn("white_pawn3", 6, 2, 'white'))
        self.pieces_list.append(pieces.Pawn("white_pawn4", 6, 3, 'white'))
        self.pieces_list.append(pieces.Pawn("white_pawn5", 6, 4, 'white'))
        self.pieces_list.append(pieces.Pawn("white_pawn6", 6, 5, 'white'))
        self.pieces_list.append(pieces.Pawn("white_pawn7", 6, 6, 'white'))
        self.pieces_list.append(pieces.Pawn("white_pawn8", 6, 7, 'white'))
        self.pieces_list.append(pieces.Rook("white_rook1", 7, 0, 'white'))
        self.pieces_list.append(pieces.Knight("white_knight1", 7, 1, 'white'))
        self.pieces_list.append(pieces.Bishop("white_bishop1", 7, 2, 'white'))
        self.pieces_list.append(pieces.Queen("white_queen", 7, 3, 'white'))
        self.pieces_list.append(pieces.King("white_king", 7, 4, 'white'))
        self.pieces_list.append(pieces.Bishop("white_bishop2", 7, 5, 'white'))
        self.pieces_list.append(pieces.Knight("white_knight2", 7, 6, 'white'))
        self.pieces_list.append(pieces.Rook("white_rook2", 7, 7, 'white'))

        self.pieces_list.append(pieces.Pawn("black_pawn1", 1, 0, 'black'))
        self.pieces_list.append(pieces.Pawn("black_pawn2", 1, 1, 'black'))
        self.pieces_list.append(pieces.Pawn("black_pawn3", 1, 2, 'black'))
        self.pieces_list.append(pieces.Pawn("black_pawn4", 1, 3, 'black'))
        self.pieces_list.append(pieces.Pawn("black_pawn5", 1, 4, 'black'))
        self.pieces_list.append(pieces.Pawn("black_pawn6", 1, 5, 'black'))
        self.pieces_list.append(pieces.Pawn("black_pawn7", 1, 6, 'black'))
        self.pieces_list.append(pieces.Pawn("black_pawn8", 1, 7, 'black'))
        self.pieces_list.append(pieces.Rook("black_rook1", 0, 0, 'black'))
        self.pieces_list.append(pieces.Knight("black_knight1", 0, 1, 'black'))
        self.pieces_list.append(pieces.Bishop("black_bishop1", 0, 2, 'black'))
        self.pieces_list.append(pieces.Queen("black_queen", 0, 3, 'black'))
        self.pieces_list.append(pieces.King("black_king", 0, 4, 'black'))
        self.pieces_list.append(pieces.Bishop("black_bishop2", 0, 5, 'black'))
        self.pieces_list.append(pieces.Knight("black_knight2", 0, 6, 'black'))
        self.pieces_list.append(pieces.Rook("black_rook2", 0, 7, 'black'))"""