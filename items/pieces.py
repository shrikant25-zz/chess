
class Pieces:
    def __init__(self, name, row, column, color, piece_type):        
        self.name = name
        self.piece_type = piece_type
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
                #print(f"appended row {row} {column}")
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
    
        
    def add_castling_info(self, board, possible_row=None, possible_column=None, castle=False):
        castling_positions_white =  [
                                    {"side" : "left", "king":[7, 4], "rook":[7, 0], "square1": [7, 3], "square2" : [7, 2], "square3" : [7, 1], "possible_position_king": [7, 2], "possible_position_rook": [7, 3]},
                                    {"side" : "right", "king":[7, 4], "rook":[7, 7], "square1": [7, 5], "square2" : [7, 6], "possible_position_king": [7, 6], "possible_position_rook": [7, 5]}
                                    ]
                                    
        castling_positions_black =  [
                                    {"side" : "left", "king":[0, 4], "rook":[0, 0], "square1": [0, 3], "square2" : [0, 2], "square3" : [0, 1], "possible_position_king": [0, 2], "possible_position_rook": [0, 3]},
                                    {"side" : "right", "king":[0, 4], "rook":[0, 7], "square1": [0, 5], "square2" : [0, 6], "possible_position_king": [0, 6], "possible_position_rook": [0, 5]}
                                    ]

        if self.color == 'white':
            castling_positions = castling_positions_white
        else:
            castling_positions = castling_positions_black

        if castle:
            if self.piece_type == 'King' and not self.moved:
                for pos in castling_positions:
                    if (pos["side"] == "left" and self.left_castle_possible) or (pos["side"] == "right" and self.right_castle_possible): 
                        if pos["possible_position_king"][0] == possible_row and pos["possible_position_king"][1] == possible_column:
                            rook = board.get_piece_from_position(pos["rook"][0], pos["rook"][1])
                            if rook.moved:
                                return
                        
                            rook.row = pos["possible_position_rook"][0]
                            rook.column = pos["possible_position_rook"][1]
                            rook.moved = True
                            break

            """ 
                if self.piece_type == 'Rook' and not self.moved:
                    for pos in castling_positions:
                        if (pos["side"] == "left" and self.left_castle_possible) or (pos["side"] == "right" and self.right_castle_possible):
                            if pos["possible_position_rook"][0] == possible_row and pos["possible_position_rook"][1] == possible_column:
                                king = board.get_piece_from_position(pos["king"][0], pos["king"][1])
                                if king.moved:
                                    return
                            
                                king.row = pos["possible_position_king"][0]
                                king.column = pos["possible_position_king"][1]
                                king.moved = True """

        else:    
            if self.piece_type == 'King' and not self.moved:
                for pos in castling_positions:
                    other_piece = board.get_piece_from_position(pos["rook"][0], pos["rook"][1])
                    if other_piece:
                        if other_piece.piece_type == 'Rook' and other_piece.color == self.color: 
                            if not other_piece.moved:
                                if board.is_the_square_safe(self, pos["square1"]) and board.is_the_square_safe(self, pos["square2"]):
                                    if pos["side"] == "left":
                                        if not board.is_there_piece_on_position(pos["square3"][0], pos["square3"][1]):
                                            self.possible_positions.append([pos["possible_position_king"][0], pos["possible_position_king"][1], None])
                                            self.left_castle_possible = True
                                            #other_piece.left_castle_possible = True
                                
                                    else:
                                        if pos["side"] == "right":
                                            self.possible_positions.append([pos["possible_position_king"][0], pos["possible_position_king"][1], None])
                                            self.right_castle_possible = True
                                            #other_piece.right_castle_possible = True

                                else:
                                    if pos["side"] == "left":
                                        self.left_castle_possible = False
                                        #other_piece.left_castle_possible = False
                                    
                                    else:
                                        if pos["side"] == "right":
                                            self.right_castle_possible = False
                                            #other_piece.right_castle_possible = False

        """ else:
                if self.piece_type == 'Rook' and not self.moved:
                    for pos in castling_positions:
                        other_piece = board.get_piece_from_position(pos["king"][0], pos["king"][1])
                        if other_piece:
                            if other_piece.piece_type == 'King' and other_piece.color == self.color: 
                                if not other_piece.moved:
                                    if board.is_the_square_safe(self, pos["square1"]) and board.is_the_square_safe( self, pos["square2"]):
                                        self.possible_positions.append([pos["possible_position_rook"][0], pos["possible_position_rook"][1], None])
                                        if pos["side"] == "left":
                                            self.left_castle_possible = True
                                            other_piece.left_castle_possible = True
                                    
                                        else:
                                            if pos["side"] == "right":
                                                self.right_castle_possible = True
                                                other_piece.right_castle_possible = True
                                    else:
                                        if pos["side"] == "left":
                                            self.left_castle_possible = False
                                            other_piece.left_castle_possible = False
                                        else:
                                            if pos["side"] == "right":
                                                self.right_castle_possible = False
                                                other_piece.right_castle_possible = False """
