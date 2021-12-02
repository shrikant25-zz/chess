import pygame
from colors import color
from screen import Screen
from cases import *


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
        screen.update_board_display()    
        update_moves_of_all_pieces(screen.board, "white")
        run = True
        result = False
        while run:
            #if not result:
                #result = self.do_stuff(screen, result)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                active_piece = screen.board.get_active_piece()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and active_piece == None:
                    screen.mouse_down()
    
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and active_piece != None:
                    screen.mouse_up(active_piece)
                    update_moves_of_all_pieces(screen.board, screen.board.turn)
                    if not can_our_pieces_move(screen.board, screen.board.turn):
                        if king_under_attack(screen.board):
                            print(f"{active_piece.color} won")
                        else:
                            print("stale mate")
                    if only_kings_remain(screen.board):
                        print("stale mate")
                screen.update_board_display()
 
        pygame.quit()

    def do_stuff(self, screen, result):
        piece = generate_piece(screen.board)
        screen.select_piece(piece.row, piece.column)
        move = generate_move(piece)
        screen.make_move(move[0], move[1], piece)


        update_moves_of_all_pieces(screen.board, screen.board.turn)
        if not can_our_pieces_move(screen.board, screen.board.turn):
            if king_under_attack(screen.board):
                print(f"{piece.color} won")
                result = True
            else:
                print("stale mate")    
                result = True
        if only_kings_remain(screen.board):
            print("stale mate")
            result = True
        screen.update_board_display()
        return result

if __name__ == '__main__':
    game = Game(8, 8, 712, 712, 700)
    game.rungame()