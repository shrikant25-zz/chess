import pygame
from chessboard import Board
from colors import color

class Game:
    def __init__(self, rows, columns, width, height, board_dimensions):
        pygame.init()
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.board_dimensions = board_dimensions
        self.square_dimensions = self.board_dimensions // self.rows 
        self.borderline = self.width // self.square_dimensions
        self.window = pygame.display.set_mode((self.width, self.height))
  
    def get_row_col_from_pos(self, pos): # gets cursor position
        x, y = pos
        row = y // self.square_dimensions 
        col = x // self.square_dimensions 
        if row >= self.rows or col >= self.columns:
            return None, None
        return row, col

    def mouse_down(self, board):
        pos = pygame.mouse.get_pos()
        row, column = self.get_row_col_from_pos(pos)
        if row != None and column!= None:
            active_piece = board.get_piece_from_position(row, column)
            if active_piece:
                active_piece.active = True
                square = board.get_square_from_position(row, column)
                square.active = True
                active_piece.set_moves(board)

    def mouse_up(self, board):
        pos = pygame.mouse.get_pos()
        row, column = self.get_row_col_from_pos(pos)
        active_piece = board.get_active_piece()
        if (row != None and column != None) and (row!= active_piece.row or column != active_piece.column):
            possible_squares = board.get_possible_squares()
            pieces_inpath = board.get_pieces_inpath()
            for square in possible_squares:
                square.possible_position = False
                if square.row == row and square.column == column:
                    active_piece.row = row
                    active_piece.column = column
                    for piece in pieces_inpath:
                        if piece.row == row and piece.column == column:
                            piece.alive = False
            for piece in pieces_inpath:
                piece.inpath = False
            active_piece.active = False
            active_square = board.get_active_square()
            active_square.active = False
                    
    def update_board(self, board):
        for square in board.squares_list:
            if square.possible_position is True:
                square.color = 'faint_blue'
            if square.color == 'faint_blue' and square.possible_position is False:
                square.color =  (('dark_silver', 'dark_red') [(square.row+square.column) & 1])
            if square.active is True:
                square.color = 'faint_green'
            if square.color == 'faint_green' and square.active is False:
                square.color =  (('dark_silver', 'dark_red') [(square.row+square.column) & 1])
            board.draw_square(square.color, square.row, square.column)
        for piece in board.pieces_list:
            if piece.alive == False:
                continue
            board.display_piece_on_board(piece, piece.row, piece.column)
        pygame.display.update()     

    def rungame(self): 
        pygame.display.set_caption("CHESS") 
        self.window.fill(color['black'])  
        board = Board(self.window, self.square_dimensions, self.borderline, 'white')
        board.create_board(self.rows, self.columns)
        self.update_board(board)    
        run = True
        while run: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                active_piece = board.get_active_piece()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and active_piece == None:
                    self.mouse_down(board)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and active_piece != None:
                    self.mouse_up(board)
            self.update_board(board)
        pygame.quit()

if __name__ == '__main__':
    game = Game(8, 8, 712, 712, 700)
    game.rungame()