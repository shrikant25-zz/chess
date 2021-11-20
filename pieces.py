


class Pieces:
    def __init__(self, name, row, column, color):        
        self.name = name
        self.row = row
        self.column = column
        self.alive = True
        self.active = False
        self.color = color
        self.inpath = False
        self.blocking_piece = False

    def get_file_rank(self):
        rank = str(8 - int(self.row))
        file = chr(ord(str(self.column)) + 49)
        return file, rank
    
class King(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def get_all_moves(self, pieces_position):
        moves = []
        if self.color == 'white':
            moves.append({ 'row' : self.row - 1, 'column' : self.column, 'block_if_in_path' : True})
            moves.append({ 'row' : self.row - 1, 'column' : self.column -1, 'block_if_in_path' : False})
            moves.append({ 'row' : self.row - 1, 'column' : self.column +1, 'block_if_in_path' : False})
        if self.color == 'black':
            moves.append({'row' : self.row + 1, 'column' : self.column, 'block_if_in_path' : True})
            moves.append({'row' : self.row + 1, 'column' : self.column +1, 'block_if_in_path' : False})
            moves.append({'row' : self.row + 1, 'column' : self.column -1, 'block_if_in_path' : False})
        return moves

class Queen(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def get_all_moves(self, pieces_position):
        moves = []
        if self.color == 'white':
            moves.append({ 'row' : self.row - 1, 'column' : self.column, 'block_if_in_path' : True})
            moves.append({ 'row' : self.row - 1, 'column' : self.column -1, 'block_if_in_path' : False})
            moves.append({ 'row' : self.row - 1, 'column' : self.column +1, 'block_if_in_path' : False})
        if self.color == 'black':
            moves.append({'row' : self.row + 1, 'column' : self.column, 'block_if_in_path' : True})
            moves.append({'row' : self.row + 1, 'column' : self.column +1, 'block_if_in_path' : False})
            moves.append({'row' : self.row + 1, 'column' : self.column -1, 'block_if_in_path' : False})
        return moves

class Rook(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)
    
    def get_all_moves(self, pieces_position):
        moves = []
        if self.color == 'white':
            moves.append({ 'row' : self.row - 1, 'column' : self.column, 'block_if_in_path' : True})
            moves.append({ 'row' : self.row - 1, 'column' : self.column -1, 'block_if_in_path' : False})
            moves.append({ 'row' : self.row - 1, 'column' : self.column +1, 'block_if_in_path' : False})
        if self.color == 'black':
            moves.append({'row' : self.row + 1, 'column' : self.column, 'block_if_in_path' : True})
            moves.append({'row' : self.row + 1, 'column' : self.column +1, 'block_if_in_path' : False})
            moves.append({'row' : self.row + 1, 'column' : self.column -1, 'block_if_in_path' : False})
        return moves

class Knight(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def get_all_moves(self, pieces_position):
        moves = []
        if self.color == 'white':
            moves.append({ 'row' : self.row - 1, 'column' : self.column, 'block_if_in_path' : True})
            moves.append({ 'row' : self.row - 1, 'column' : self.column -1, 'block_if_in_path' : False})
            moves.append({ 'row' : self.row - 1, 'column' : self.column +1, 'block_if_in_path' : False})
        if self.color == 'black':
            moves.append({'row' : self.row + 1, 'column' : self.column, 'block_if_in_path' : True})
            moves.append({'row' : self.row + 1, 'column' : self.column +1, 'block_if_in_path' : False})
            moves.append({'row' : self.row + 1, 'column' : self.column -1, 'block_if_in_path' : False})
        return moves

class Bishop(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        moves = []
        col = self.column - 1 
        row = self.row - 1
        while col >=0 and row >= 0:
            moves.append({ 'row' : row , 'column' : col , 'block_if_in_path' : False})
            col -= 1
            row -= 1

        col = self.column + 1 
        row = self.row - 1

        while col >=7 and row >= 0:
            moves.append({ 'row' : row , 'column' : col , 'block_if_in_path' : False})
            col += 1
            row -= 1

        col = self.column - 1 
        row = self.row + 1

        while col >=0 and row >= 7:
            moves.append({ 'row' : row , 'column' : col , 'block_if_in_path' : False})
            col -= 1
            row += 1

        col = self.column + 1 
        row = self.row + 1
        
        while col >=7 and row >= 7:
            moves.append({ 'row' : row , 'column' : col , 'block_if_in_path' : False})
            col += 1
            row += 1

        return moves

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

