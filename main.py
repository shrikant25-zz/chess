import pygame
from colors import color
from chessboard import Board

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
        if row > self.rows or col > self.columns:
            return None
        return row, col

    def rungame(self): 
        pygame.display.set_caption("CHESS") 
        self.window.fill(color['black'])  
        board = Board(self.rows, self.columns, self.window, self.square_dimensions, self.borderline)
        board.create_board()
        board.create_pieces()
        board.set_pieces()
        pygame.display.update()     
        run = True
        while run: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and board.active_piece == None:
                    pos = pygame.mouse.get_pos()
                    row, column = self.get_row_col_from_pos(pos)
                    if row != None and column!= None:
                        piece =  board.get_piece_from_position(row, column)
                        board.active_piece = piece
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and board.active_piece != None:
                    pos = pygame.mouse.get_pos()
                    row, column = self.get_row_col_from_pos(pos)
                    if row != None and column!= None:
                        board.remove_piece_from_board(board.active_piece)
                        board.active_piece.update_piece_position(row, column)
                        board.display_piece_on_board(board.active_piece.name, row, column)
                        pygame.display.update() 
                        board.active_piece = None
                        
        pygame.quit()

if __name__ == '__main__':
    game = Game(8, 8, 712, 712, 700)
    game.rungame()
    