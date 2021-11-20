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
            self.movement_without_interruption(board, row , column)
        return 0
    
    def movement_with_piece(self, board, row, column):
        piece = board.get_piece_from_position(row, column)
        if piece.color != self.color:
            piece.inpath = True
            square = board.get_square_from_position(row, column)
            square.possible_position = True

    def movement_without_interruption(self, board, row, column):
        if not board.is_there_piece_on_position(row, column) and board.is_there_square_on_position(row, column):
                square = board.get_square_from_position(row, column)
                square.possible_position = True
    
class King(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        positions = [[self.row - 1, self.column - 1],
                    [self.row - 1, self.column],
                    [self.row - 1, self.column + 1],
                    [self.row, self.column + 1],
                    [self.row + 1, self.column + 1],
                    [self.row + 1, self.column],
                    [self.row + 1, self.column - 1],
                    [self.row, self.column - 1],
                    ]
        for row, column in positions:
            self.movements(board, row, column)

class Queen(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        self.vertical_horizontal_moves(board)
        self.diagonal_moves(board)

class Rook(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)
    
    def set_moves(self, board):
        self.vertical_horizontal_moves(board)

class Knight(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        positions = [[ self.row - 1, self.column -2], # upward - left - 1 step
        [self.row + 1 , self.column -2],  # downward - right - 1 step 
        [self.row - 1 , self.column + 2], # upward - right - 1 step
        [self.row + 1 , self.column + 2],# downward - right - 1 step
        [self.row - 2 , self.column -1], # upward - left - 2 step,
        [self.row - 2 , self.column + 1],  # upward - right - 2 step
        [self.row + 2 , self.column  - 1],    # downward - left - 2 step
        [self.row + 2 , self.column  + 1]# downward - right - 2 step
        ]

        for row, column in positions:
            self.movements(board, row, column, False)

class Bishop(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):
        self.diagonal_moves(board)

class Pawn(Pieces):
    def __init__(self, name, row, column, color):
        super().__init__(name, row, column, color)

    def set_moves(self, board):

        if self.color == 'white':
            diagonal_movements = [[self.row - 1, self.column - 1], [self.row - 1, self.column + 1]]
            if self.row == 6:
                row = self.row - 1
                row2 = self.row -2
                column = self.column
                self.straight_movement_beginning(board, row, row2, column)
            else:
                row = self.row - 1
                column = self.column
                self.movement_without_interruption(board, row, column)

        else: 
            if self.color == 'black':
                diagonal_movements = [[self.row + 1, self.column - 1], [self.row + 1, self.column + 1]]
                if self.row == 1:
                    row = self.row + 1
                    row2 = self.row + 2
                    column = self.column
                    self.straight_movement_beginning(board, row, row2, column)
                else:
                    row = self.row + 1
                    column = self.column
                    self.movement_without_interruption(board, row, column)

                        # diagonal movements
        for row , column in diagonal_movements:
            if board.is_there_piece_on_position(row, column)  and board.is_there_square_on_position(row, column):    
                self.movement_with_piece(board, row, column)
                
    def straight_movement_beginning(self, board, row, row2, column):
        if not board.is_there_piece_on_position(row, column)  and board.is_there_square_on_position(row, column):   
            square = board.get_square_from_position(row, column)
            square.possible_position = True
            if not board.is_there_piece_on_position(row2, column)  and board.is_there_square_on_position(row2, column):
                square = board.get_square_from_position(row2 , column)
                square.possible_position = True
    
  