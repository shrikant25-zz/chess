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
        self.pieces_list = []

    def create_board(self):
        for row in range(self.rows):
            for column in range(self.columns):
                square_color = (('dark_silver', 'dark_red') [(row+column) & 1])
                self.create_square(square_color, row, column) 
                  
    def create_square(self, square_color, row, column):
        # adding distance equal to borderline in starting points of sqaure shifts them enough to have place for a borderline 
        pygame.draw.rect(self.window, color[square_color], ((column * self.square_dimensions)+self.borderline, 
                (row * self.square_dimensions)+self.borderline, self.square_dimensions, self.square_dimensions))
    
    def create_pieces(self): 
        self.pieces_list.append(Pieces("white_pawn1", "a", "2"))
        self.pieces_list.append(Pieces("white_pawn2", "b", "2"))
        self.pieces_list.append(Pieces("white_pawn3", "c", "2"))
        self.pieces_list.append(Pieces("white_pawn4", "d", "2"))
        self.pieces_list.append(Pieces("white_pawn5", "e", "2"))
        self.pieces_list.append(Pieces("white_pawn6", "f", "2"))
        self.pieces_list.append(Pieces("white_pawn7", "g", "2"))
        self.pieces_list.append(Pieces("white_pawn8", "h", "2"))
        self.pieces_list.append(Pieces("white_rook1", "a", "1", "R"))
        self.pieces_list.append(Pieces("white_rook2", "h", "1", "R"))
        self.pieces_list.append(Pieces("white_knight1", "b", "1", "N"))
        self.pieces_list.append(Pieces("white_knight2", "g", "1", "N"))
        self.pieces_list.append(Pieces("white_bishop1", "c", "1", "B"))
        self.pieces_list.append(Pieces("white_bishop2", "f", "1", "B"))
        self.pieces_list.append(Pieces("white_king", "e", "1", "K"))
        self.pieces_list.append(Pieces("white_queen", "d", "1", "Q"))

        self.pieces_list.append(Pieces("black_pawn1", "a", "7"))
        self.pieces_list.append(Pieces("black_pawn2", "b", "7"))
        self.pieces_list.append(Pieces("black_pawn3", "c", "7"))
        self.pieces_list.append(Pieces("black_pawn4", "d", "7"))
        self.pieces_list.append(Pieces("black_pawn5", "e", "7"))
        self.pieces_list.append(Pieces("black_pawn6", "f", "7"))
        self.pieces_list.append(Pieces("black_pawn7", "g", "7"))
        self.pieces_list.append(Pieces("black_pawn8", "h", "7"))
        self.pieces_list.append(Pieces("black_rook1", "a", "8", "R"))
        self.pieces_list.append(Pieces("black_rook2", "h", "8", "R"))
        self.pieces_list.append(Pieces("black_knight1", "b", "8", "N"))
        self.pieces_list.append(Pieces("black_knight2", "g", "8", "N"))
        self.pieces_list.append(Pieces("black_bishop1", "c", "8", "B"))
        self.pieces_list.append(Pieces("black_bishop2", "f", "8", "B"))
        self.pieces_list.append(Pieces("black_king", "e", "8", "K"))
        self.pieces_list.append(Pieces("black_queen", "d", "8", "Q"))

    def set_pieces(self):
        for piece in self.pieces_list:
            row ,column = piece.get_row_column()
            self.display_piece_on_board(piece.name, row, column)

    def display_piece_on_board(self, piece_name, row, column):
        position_on_chessboard =((column * self.square_dimensions) + self.borderline*2, 
                (row * self.square_dimensions) + self.borderline*2)
        path = r'C:\Users\Shrikant\projects\chess\images'
        piece_image = pygame.image.load(path + "\\" + piece_name + ".png")
        piece_image = pygame.transform.scale(piece_image, (67, 67))
        self.window.blit(piece_image, position_on_chessboard)

    def is_there_piece_on_position(self, row, column):
        rank = 8 - int(row)
        file = ord(column) - 49
        for piece in self.pieces_list:
            if piece.current_rank == rank and piece.current_file == file:
                return True
        return False
    
    def get_piece_from_position(self, row, column):
        rank = 8 - int(row)
        file = ord(column) - 49
        for piece in self.pieces_list:
            if piece.current_rank == rank and piece.current_file == file:
                return piece
        return None


