
class Pieces:
    def __init__(self, name, row, column, color):        
        self.name = name
        self.row = row
        self.column = column
        self.alive = True
        self.active = False
        self.color = color
        self.inpath = False
        self.possible_positions = []

    def get_file_rank(self):
        rank = str(8 - int(self.row))
        file = chr(ord(str(self.column)) + 49)
        return file, rank
    
    def diagonal_moves(self,board):
                                        # upwards - left - diagonal
        column = self.column - 1 
        row = self.row - 1
        while column >=0 and row >= 0:
            condition = self.movements(board, row, column, True)
            if condition:
                break
            column -= 1
            row -= 1

                                # upwards - right - diagonal 
        column = self.column + 1 
        row = self.row - 1
        while column <=7 and row >= 0:
            condition = self.movements(board, row, column, True)
            if condition:
                break
            column += 1
            row -= 1

                                # downwards - left - diagonal 
        column = self.column - 1 
        row = self.row + 1
        while column >=0 and row <= 7:
            condition = self.movements(board, row, column, True)
            if condition:
                break
            column -= 1
            row += 1

                                # downwards - right - diagonal 
        column = self.column + 1 
        row = self.row + 1
        while column <=7 and row <= 7:
            condition = self.movements(board, row, column, True)
            if condition:
                break
            column += 1
            row += 1

    def vertical_horizontal_moves(self,board):
                                                # upwards 
        column = self.column
        row = self.row - 1
        while column >=0 and row >= 0:
            condition = self.movements(board, row, column, True)
            if condition:
                break
            row -= 1

                                #  right 
        column = self.column + 1 
        row = self.row
        while column <=7 and row >= 0:
            condition = self.movements(board, row, column, True)
            if condition:
                break
            column += 1

                                #  left 
        column = self.column - 1 
        row = self.row
        while column >=0 and row <= 7:
            condition = self.movements(board, row, column, True)
            if condition:
                break
            column -= 1
            row 

                                # downwards 
        column = self.column  
        row = self.row + 1
        while column <=7 and row <= 7:
            condition = self.movements(board, row, column, True)
            if condition:
                break
            row += 1

    def movements(self, board, row, column, stop = False):
        if board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
            self.movement_with_piece(board, row, column)
            if stop:
                return 1
        else:
            if not board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                self.possible_positions.append([row, column, None])
        return 0
    
    def movement_with_piece(self, board, row, column):
        piece = board.get_piece_from_position(row, column)
        if piece.color != self.color:
            self.possible_positions.append([row, column, piece])
       
    def update_board_objects(self, board):
        for row, column, piece in self.possible_positions:
            if piece:
                piece.inpath = True
            square = board.get_square_from_position(row, column)
            square.possible_position = True
    