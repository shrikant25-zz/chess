import pygame
from colors import color
from screen import Screen

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
  
    def rungame(self): 
        pygame.display.set_caption("CHESS") 
        self.window.fill(color['black']) 
        screen = Screen(self.square_dimensions, self.rows, self.columns, self.window, self.borderline)
        screen.board.create_board(self.rows, self.columns)
        screen.update_board()    
        run = True
        while run: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                active_piece = screen.board.get_active_piece()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and active_piece == None:
                    screen.mouse_down()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and active_piece != None:
                    screen.mouse_up()
            screen.update_board()
        pygame.quit()

if __name__ == '__main__':
    game = Game(8, 8, 712, 712, 700)
    game.rungame()