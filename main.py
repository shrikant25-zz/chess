import pygame
from colors import color
from items import pieces
from screen import Screen
from cases import *
dcnt = 0
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
        #for i in range(5):  
        screen = Screen(self.square_dimensions, self.rows, self.columns, self.window, self.borderline)
        screen.board.create_board(self.rows, self.columns)
        screen.update_board_display()    
        update_moves_of_all_pieces(screen.board)
        run = True
        result = False
            #depth = 1
            #print(f"depth 1 : {self.calculate(screen, depth)}")
            #depth = 2
            #print(f"depth 2 : {self.calculate(screen, depth)}")
            #depth = 3
            #print(f"depth 3 : {self.calculate(screen, depth)}")
            # global dcnt
            #dcnt = 0
            #print(f"depth {i} : {self.calculate(screen, i)}")
            #print(dcnt)    
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
                    update_moves_of_all_pieces(screen.board)
                    if not can_our_pieces_move(screen.board):
                        print("true")
                        if screen.board.is_king_under_attack():
                            print(f"{active_piece.color} won")
                            result = True
                        else:
                            print("stale mate")
                            result = True
                    if only_kings_remain(screen.board):
                        print("stale mate")
                        result = True
                screen.update_board_display()
            
                if result:
                    run = False
                    break  
                
        pygame.quit()

    def generate_moves(self, screen):
       
        moves = []
        update_moves_of_all_pieces(screen.board)
        for piece in screen.board.pieces_list:
            if piece.color == screen.board.turn and piece.alive:
                for mv in piece.possible_positions:                    
                    move = mv[:]
                    move.append(piece.row)
                    move.append(piece.column)     
                    moves.append([piece, move])
        return moves


    def calculate(self, screen, depth):
       
        if depth == 0:
            return 1
        
        moves = []
        moves = self.generate_moves(screen)
        pos = 0
        for piece, move in moves:
            rs= self.do_stuff(screen, piece, move)
            if not rs:
                break    
            pos += self.calculate(screen, depth -1)
            if screen.board.turn == 'white':
                screen.board.turn = 'black' 
            else:
                screen.board.turn = 'white'
            self.undo_move(piece, move)
            screen.update_board_display()
            
        return pos

    def undo_move(self, piece, move):
        piece.row, piece.column = move[3], move[4] 
        victim = move[2]
        if victim:
            victim.alive = True 
            global dcnt
            dcnt += 1

    def do_stuff(self, screen, piece, move):
        #piece = generate_piece(screen.board)
        if screen.select_piece(piece.row, piece.column):
        #move = generate_move(piece)
            active_piece = screen.board.get_active_piece()
            #print(f"name {active_piece.name} row {active_piece.row} column {active_piece.column} mv {move}")
            screen.make_move(move[0], move[1], active_piece, move[2])
        else:
            return False
        return True

        """update_moves_of_all_pieces(screen.board, screen.board.turn)
        if not can_our_pieces_move(screen.board, screen.board.turn):
            if is_king_under_attack(screen.board):
                print(f"{piece.color} won")
                #result = True
            else:
                print("stale mate")    
                #result = True
        if only_kings_remain(screen.board):
            print("stale mate")
            #result = True"""
        #screen.update_board_display()
        #return result
    
if __name__ == '__main__':
    game = Game(8, 8, 712, 712, 700)
    game.rungame()