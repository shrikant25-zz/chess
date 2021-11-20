
from squares import Square


class Pieces:
    def __init__(self, name, row, column, color):        
        self.name = name
        self.row = row
        self.column = column
        self.alive = True
        self.active = False
        self.color = color
        self.inpath = False

    def get_file_rank(self):
        rank = str(8 - int(self.row))
        file = chr(ord(str(self.column)) + 49)
        return file, rank
    
class King(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        pass

class Queen(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        pass

class Rook(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)
    
    def set_moves(self, board):
        pass

class Knight(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
       pass
        

class Bishop(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
                                # upwards - left - diagonal
        column = self.column - 1 
        row = self.row - 1
        
        while column >=0 and row >= 0:
            if board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                piece = board.get_piece_from_position(row, column)
                if piece.color != self.color:
                    piece.inpath = True
                    square = board.get_square_from_position(row, column)
                    square.possible_position = True
                break
            else:
                if not board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                    square = board.get_square_from_position(row, column)
                    square.possible_position = True
            column -= 1
            row -= 1

                                # upwards - right - diagonal 
        column = self.column + 1 
        row = self.row - 1

        while column <=7 and row >= 0:
            if board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                piece = board.get_piece_from_position(row, column)
                if piece.color != self.color:
                    piece.inpath = True
                    square = board.get_square_from_position(row, column)
                    square.possible_position = True
                break
            else:
                if not board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                    square = board.get_square_from_position(row, column)
                    square.possible_position = True
            column += 1
            row -= 1

                                # downwards - left - diagonal 
        column = self.column - 1 
        row = self.row + 1

        while column >=0 and row <= 7:
            if board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                piece = board.get_piece_from_position(row, column)
                if piece.color != self.color:
                    piece.inpath = True
                    square = board.get_square_from_position(row, column)
                    square.possible_position = True
                break
            else:
                if not board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                    square = board.get_square_from_position(row, column)
                    square.possible_position = True
            column -= 1
            row += 1

                                # downwards - right - diagonal 
        column = self.column + 1 
        row = self.row + 1
        
        while column <=7 and row <= 7:
            if board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                piece = board.get_piece_from_position(row, column)
                if piece.color != self.color:
                    piece.inpath = True
                    square = board.get_square_from_position(row, column)
                    square.possible_position = True
                break
            else:
                if not board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                    square = board.get_square_from_position(row, column)
                    square.possible_position = True
            column += 1
            row += 1

class Pawn(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        if self.color == 'white':
            if self.row == 6:
                if not board.is_there_piece_on_position(self.row - 1, self.column)  and board.is_there_square_on_position(self.row - 1, self.column):   
                    square = board.get_square_from_position(self.row -1 , self.column)
                    square.possible_position = True
                    if not board.is_there_piece_on_position(self.row - 2, self.column)  and board.is_there_square_on_position(self.row - 2, self.column):
                        square = board.get_square_from_position(self.row - 2 , self.column)
                        square.possible_position = True
                    
                        # straight movement from default position
            else:
                        # straight movement from other position
                if not board.is_there_piece_on_position(self.row - 1, self.column)  and board.is_there_square_on_position(self.row - 1, self.column):
                    square = board.get_square_from_position(self.row -1 , self.column)
                    square.possible_position = True
                    
                        # diagonal movements
            if board.is_there_piece_on_position(self.row - 1, self.column - 1)  and board.is_there_square_on_position(self.row - 1, self.column - 1):    
                piece = board.get_piece_from_position(self.row - 1, self.column - 1)
                if piece.color != self.color:
                    piece.inpath = True
                    square = board.get_square_from_position(self.row -1 , self.column - 1)
                    square.possible_position = True
                    
            if board.is_there_piece_on_position(self.row - 1, self.column + 1)  and board.is_there_square_on_position(self.row - 1, self.column + 1):    
                piece = board.get_piece_from_position(self.row - 1, self.column + 1)
                if piece.color != self.color:
                    piece.inpath = True
                    square = board.get_square_from_position(self.row -1 , self.column + 1)
                    square.possible_position = True
                    
        
        if self.color == 'black':
            if self.row == 1:
                if not board.is_there_piece_on_position(self.row + 1, self.column) and board.is_there_square_on_position(self.row + 1, self.column):   
                    square = board.get_square_from_position(self.row +1 , self.column)
                    square.possible_position = True
                    if not board.is_there_piece_on_position(self.row + 2, self.column)  and board.is_there_square_on_position(self.row + 2, self.column):
                        square = board.get_square_from_position(self.row + 2 , self.column)
                        square.possible_position = True
                        # for straight movement from default position
            else:
                        # for straight movement from other position
                if not board.is_there_piece_on_position(self.row + 1, self.column)  and board.is_there_square_on_position(self.row + 1, self.column):
                    square = board.get_square_from_position(self.row + 1 , self.column)
                    square.possible_position = True

                        # diagonal movements
            if board.is_there_piece_on_position(self.row + 1, self.column - 1)  and board.is_there_square_on_position(self.row + 1, self.column -1):    
                piece = board.get_piece_from_position(self.row + 1, self.column - 1)
                if piece.color != self.color:
                    piece.inpath = True
                    square = board.get_square_from_position(self.row + 1 , self.column - 1)
                    square.possible_position = True
            if board.is_there_piece_on_position(self.row + 1, self.column + 1)  and board.is_there_square_on_position(self.row + 1, self.column + 1):    
                piece = board.get_piece_from_position(self.row + 1, self.column + 1)
                if piece.color != self.color:
                    piece.inpath = True
                    square = board.get_square_from_position(self.row + 1 , self.column + 1)
                    square.possible_position = True