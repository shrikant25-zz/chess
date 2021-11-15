import pygame
from pieces import Pieces
from colors import color

class Board():
    def __init__(self, rows, columns, window, square_dimensions, borderline):
        self.rows = rows
        self.columns = columns
        self.window = window
        self.square_dimensions = square_dimensions
        self.borderline = borderline
        self.active_piece = None
        self.pieces_list = []

    def create_board(self):
        for row in range(self.rows):
            for column in range(self.columns):
                square_color = (('dark_silver', 'dark_red') [(row+column) & 1])
                self.draw_square(square_color, row, column) 
                  
    def draw_square(self, square_color, row, column):
        rect = ((column * self.square_dimensions)+self.borderline, 
                (row * self.square_dimensions)+self.borderline, self.square_dimensions, self.square_dimensions)
    
            # adding distance equal to borderline in starting points of sqaure shifts them enough to have place for a borderline 
        pygame.draw.rect(self.window, color[square_color], rect)

    def create_pieces(self): 
        self.pieces_list.append(Pieces("white_pawn1", 6, 0))
        self.pieces_list.append(Pieces("white_pawn2", 6, 1))
        self.pieces_list.append(Pieces("white_pawn3", 6, 2))
        self.pieces_list.append(Pieces("white_pawn4", 6, 3))
        self.pieces_list.append(Pieces("white_pawn5", 6, 4))
        self.pieces_list.append(Pieces("white_pawn6", 6, 5))
        self.pieces_list.append(Pieces("white_pawn7", 6, 6))
        self.pieces_list.append(Pieces("white_pawn8", 6, 7))
        self.pieces_list.append(Pieces("white_rook1", 7, 0, "R"))
        self.pieces_list.append(Pieces("white_knight1", 7, 1, "N"))
        self.pieces_list.append(Pieces("white_bishop1", 7, 2, "B"))
        self.pieces_list.append(Pieces("white_queen", 7, 3, "Q"))
        self.pieces_list.append(Pieces("white_king", 7, 4, "K"))
        self.pieces_list.append(Pieces("white_bishop2", 7, 5, "B"))
        self.pieces_list.append(Pieces("white_knight2", 7, 6, "N"))
        self.pieces_list.append(Pieces("white_rook2", 7, 7, "R"))

        self.pieces_list.append(Pieces("black_pawn1", 1, 0))
        self.pieces_list.append(Pieces("black_pawn2", 1, 1))
        self.pieces_list.append(Pieces("black_pawn3", 1, 2))
        self.pieces_list.append(Pieces("black_pawn4", 1, 3))
        self.pieces_list.append(Pieces("black_pawn5", 1, 4))
        self.pieces_list.append(Pieces("black_pawn6", 1, 5))
        self.pieces_list.append(Pieces("black_pawn7", 1, 6))
        self.pieces_list.append(Pieces("black_pawn8", 1, 7))
        self.pieces_list.append(Pieces("black_rook1", 0, 0, "R"))
        self.pieces_list.append(Pieces("black_knight1", 0, 1, "N"))
        self.pieces_list.append(Pieces("black_bishop1", 0, 2, "B"))
        self.pieces_list.append(Pieces("black_queen", 0, 3, "Q"))
        self.pieces_list.append(Pieces("black_king", 0, 4, "K"))
        self.pieces_list.append(Pieces("black_bishop2", 0, 5, "B"))
        self.pieces_list.append(Pieces("black_knight2", 0, 6, "N"))
        self.pieces_list.append(Pieces("black_rook2", 0, 7, "R"))

    def set_pieces(self):
        for piece in self.pieces_list:
            self.display_piece_on_board(piece.name, piece.current_row, piece.current_column)

    def display_piece_on_board(self, piece_name, row, column):
        position_on_chessboard =((column * self.square_dimensions) + self.borderline*2, 
                (row * self.square_dimensions) + self.borderline*2)
        path = r'C:\Users\Shrikant\projects\chess\images'
        piece_image = pygame.image.load(path + "\\" + piece_name + ".png")
        piece_image = pygame.transform.scale(piece_image, (67, 67))
        self.window.blit(piece_image, position_on_chessboard)

    def remove_piece_from_board(self, piece):
        square_color = (('dark_silver', 'dark_red') [(piece.current_row + piece.current_column) & 1])
        self.draw_square(square_color, piece.current_row, piece.current_column)

    def is_there_piece_on_position(self, row, column):
        for piece in self.pieces_list:
            if piece.current_row == row and piece.current_column == column:
                return True
        return False
    
    def get_piece_from_position(self, row, column):
        for piece in self.pieces_list:
            if piece.current_row == row and piece.current_column == column:
                return piece
        return None


