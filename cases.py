import random

def only_kings_remain(board):
    for piece in board.pieces_list:
        if piece.piece_type != "King" and piece.alive:
            return False
    return True

def can_our_pieces_move(board):
    pieces_can_move = False
    for piece in board.pieces_list:
        if piece.color == board.turn and piece.alive:
            if len(piece.possible_positions) > 0:
                pieces_can_move = True
                break
    return pieces_can_move

def update_moves_of_all_pieces(board):

    our_king = None
    pieces_attacking_king = []
    pieces_under_attack = []
    path_of_pieces_attacking_king = []

    for piece in board.pieces_list:
        piece.possible_positions = []
        if piece.color != board.turn and piece.alive:
            piece.set_moves(board)
            for row, column, our_piece_under_attack in piece.possible_positions:
                if our_piece_under_attack:
                    if piece.piece_type == "Queen" or piece.piece_type == "Bishop" or piece.piece_type == "Rook":
                        pieces_under_attack.append([our_piece_under_attack, piece])

                    if our_piece_under_attack.piece_type == "King":
                        if board.turn == "white":
                            board.white_king_in_check = True
                        else:
                            if board.turn == "black":
                                board.black_king_in_check = True
                        pieces_attacking_king.append(piece)
                        #our_king = our_piece_under_attack

                        path_of_pieces_attacking_king.append([piece.row, piece.column])

                        if piece.row == our_piece_under_attack.row and piece.column != our_piece_under_attack.column: # slide horizontally
                            if piece.piece_type == "Rook" or piece.piece_type == "Queen":
                                
                                if piece.column > our_piece_under_attack.column: # slide left
                                    temp_column = piece.column
                                    while temp_column > our_piece_under_attack.column:
                                        path_of_pieces_attacking_king.append([piece.row, temp_column])
                                        temp_column -= 1

                                if piece.column < our_piece_under_attack.column: # slide right
                                    temp_column = piece.column
                                    while temp_column < our_piece_under_attack.column:
                                        path_of_pieces_attacking_king.append([piece.row, temp_column])
                                        temp_column += 1

                        if piece.column == our_piece_under_attack.column and piece.row != our_piece_under_attack.row: # slide vertically
                            if piece.piece_type == "Rook" or piece.piece_type == "Queen":

                                if piece.row > our_piece_under_attack.row: # slide upwards
                                    temp_row = piece.row
                                    while temp_row > our_piece_under_attack.row:
                                        path_of_pieces_attacking_king.append([temp_row, piece.column])
                                        temp_row -= 1

                                if piece.row < our_piece_under_attack.row: # slide downwards
                                    temp_row = piece.row
                                    while temp_row < our_piece_under_attack.row:
                                        path_of_pieces_attacking_king.append([temp_row, piece.column])
                                        temp_row += 1

                        if piece.piece_type == "Queen" or piece.piece_type == "Bishop":
                            
                            # slide upwards left diagonally
                            if ((piece.row - our_piece_under_attack.row) > 0 and (piece.column - our_piece_under_attack.column) > 0) and (piece.row - our_piece_under_attack.row) == (piece.column - our_piece_under_attack.column):
                                temp_row = piece.row
                                temp_column = piece.column
                                while temp_column > our_piece_under_attack.column and temp_row > our_piece_under_attack.row:
                                    path_of_pieces_attacking_king.append([temp_row, temp_column])
                                    temp_row -= 1
                                    temp_column -= 1

                            # slide upwards right diagonally
                            if ((piece.row - our_piece_under_attack.row) > 0 and (our_piece_under_attack.column - piece.column) > 0) and (piece.row - our_piece_under_attack.row) == (our_piece_under_attack.column - piece.column):
                                temp_row = piece.row
                                temp_column = piece.column
                                while temp_column < our_piece_under_attack.column and temp_row > our_piece_under_attack.row:
                                    path_of_pieces_attacking_king.append([temp_row, temp_column])
                                    temp_row -= 1
                                    temp_column += 1
                            
                            # slide downwards left diagonally
                            if ((our_piece_under_attack.row - piece.row) > 0 and (piece.column - our_piece_under_attack.column) > 0) and (our_piece_under_attack.row - piece.row) == (piece.column - our_piece_under_attack.column):
                                temp_row = piece.row
                                temp_column = piece.column
                                while temp_column > our_piece_under_attack.column and temp_row < our_piece_under_attack.row:
                                    path_of_pieces_attacking_king.append([temp_row, temp_column])
                                    temp_row += 1
                                    temp_column -= 1

                            # slide downwards right diagonally
                            if ((our_piece_under_attack.row - piece.row) > 0 and (our_piece_under_attack.column - piece.column) > 0) and (our_piece_under_attack.row - piece.row) == (our_piece_under_attack.column - piece.column):
                                temp_row = piece.row
                                temp_column = piece.column
                                while temp_column < our_piece_under_attack.column and temp_row < our_piece_under_attack.row:
                                    path_of_pieces_attacking_king.append([temp_row, temp_column])
                                    temp_row += 1
                                    temp_column += 1

    for piece in board.pieces_list:
        if piece.color == board.turn and piece.alive:
            if piece.piece_type == 'King':
                piece.possible_positions = []
                piece.set_moves(board)
                available_positions_for_king = []
                for row, column, opposite_piece in piece.possible_positions:
                    position_available = True
                    #print(f"possible possible row {row} column {column}")
                    square = board.get_square_from_position(row, column)
                    if square in board.squares_under_attack:
                        #if square.row == row and square.column == column:
                            #print(f"not possible row {row} column {column}")
                            position_available = False
        
                    if position_available:
                        #print(f"added position row : {row} column : {column}")
                        available_positions_for_king.append([row, column,  opposite_piece])
                piece.possible_positions = available_positions_for_king
                break

    if len(pieces_attacking_king) > 0:
        if len(pieces_attacking_king) == 1:
            for piece in board.pieces_list:
                if piece.color == board.turn and piece.alive:
                    if piece.piece_type == 'King':
                        our_king = piece
                        continue
                    piece.set_moves(board)
                    temp_positions = []
                    for row, column, opposite_piece in piece.possible_positions:
                        for attacking_row, attacking_column in path_of_pieces_attacking_king:
                            if row == attacking_row and column == attacking_column:
                                temp_positions.append([row, column, opposite_piece])
                    piece.possible_positions = temp_positions
            
    else:
        for piece in board.pieces_list:
            if piece.color == board.turn and piece.alive:
                if piece.piece_type == 'King':
                    our_king = piece
                    continue
                piece.set_moves(board)
                        
        if board.turn == "white":
                board.white_king_in_check = False
        else:
            if board.turn == "black":
                board.black_king_in_check = False
    
    update_protecting_pieces(board, our_king, pieces_under_attack)

def generate_piece(board):
    cur_piece = None
    while(1):
        cur_piece = random.choice(board.pieces_list)
        if cur_piece.color == board.turn and cur_piece.alive and cur_piece.possible_positions:
            break
    return cur_piece
    
def generate_move(piece):
    cur_move = random.choice(piece.possible_positions)
    return cur_move

def update_protecting_pieces(board, our_king, pieces_under_attack):
   
    for our_piece, opposite_piece in pieces_under_attack:
                            # upwards - left - diagonal 
        row = our_king.row - 1
        column = our_king.column - 1
        while column >=0 and row >= 0:
            piece =  board.get_piece_from_position(row, column)
            if piece: # need to know if there is a piece
                if our_piece == piece:     # if there is then is it our piece
                    if ((piece.row - opposite_piece.row) > 0 and (piece.column - opposite_piece.column) > 0) and (piece.row - opposite_piece.row) == (piece.column - opposite_piece.column):
                        temp_possible_positions = []
                        if piece.piece_type == 'Bishop' or piece.piece_type == 'Queen':
                            for pos_row, pos_column, attacked_piece in piece.possible_positions:
                                if (piece.row - pos_row) == (piece.column - pos_column):
                                    temp_possible_positions.append([pos_row, pos_column, attacked_piece])
                        
                        piece.possible_positions = temp_possible_positions
                break
            column -= 1
            row -= 1
                            
                            # upwards - right - diagonal 
        row = our_king.row - 1
        column = our_king.column + 1
        while column <=7 and row >= 0:
            piece =  board.get_piece_from_position(row, column)
            if piece: # need to know if there is a piece
                if our_piece == piece:     # if it is then is it our piece
                    if ((piece.row - opposite_piece.row) > 0 and (opposite_piece.column - piece.column) > 0) and (piece.row - opposite_piece.row) == (opposite_piece.column - piece.column):
                        temp_possible_positions = []
                        if piece.piece_type == 'Bishop' or piece.piece_type == 'Queen':
                            for pos_row, pos_column, attacked_piece in piece.possible_positions:
                                if (piece.row - pos_row) == (pos_column - piece.column):
                                    temp_possible_positions.append([pos_row, pos_column, attacked_piece])
                        
                        piece.possible_positions = temp_possible_positions
                break
            column += 1
            row -= 1

                                # downwards - left - diagonal
        row = our_king.row + 1
        column = our_king.column - 1
        while column >=0 and row <= 7:
            piece =  board.get_piece_from_position(row, column)
            if piece: # need to know if there is a piece
                if our_piece == piece:     # if it is then is it our piece
                    if ((opposite_piece.row - piece.row) > 0 and (piece.column - opposite_piece.column) > 0) and (opposite_piece.row - piece.row) == (piece.column - opposite_piece.column):
                        temp_possible_positions = []
                        if piece.piece_type == 'Bishop' or piece.piece_type == 'Queen':
                            for pos_row, pos_column, attacked_piece in piece.possible_positions:
                                if (pos_row - piece.row) == (piece.column - pos_column):
                                    temp_possible_positions.append([pos_row, pos_column, attacked_piece])
                        
                        piece.possible_positions = temp_possible_positions
                break
            column -= 1
            row += 1

                                # downwards - right - diagonal 
        row = our_king.row + 1
        column = our_king.column + 1
        while column <=7 and row <= 7:
            piece =  board.get_piece_from_position(row, column)
            if piece: # need to know if there is a piece
                if our_piece == piece:     # if it is then is it our piece
                    if ((opposite_piece.row - piece.row) > 0 and (opposite_piece.column - piece.column) > 0) and (opposite_piece.row - piece.row) == (opposite_piece.column - piece.column):
                        temp_possible_positions = []
                        if piece.piece_type == 'Bishop' or piece.piece_type == 'Queen':
                            for pos_row, pos_column, attacked_piece in piece.possible_positions:
                                if (pos_row - piece.row) == (pos_column - piece.column):
                                    temp_possible_positions.append([pos_row, pos_column, attacked_piece])
                        
                        piece.possible_positions = temp_possible_positions
                break
            column += 1
            row += 1

                                                # upwards 
        row = our_king.row - 1
        column = our_king.column
        while column >=0 and row >= 0:
            piece =  board.get_piece_from_position(row, column)
            if piece: # need to know if there is a piece
                if our_piece == piece:     # if it is then is it our piece
                    if piece.row > opposite_piece.row  and opposite_piece.column == piece.column:
                        temp_possible_positions = []
                        if piece.piece_type == 'Rook' or piece.piece_type == 'Queen' or piece.piece_type == 'Pawn':
                            for pos_row, pos_column, attacked_piece in piece.possible_positions:
                                if pos_column == piece.column: # stays in the path between king and attacking piece
                                    temp_possible_positions.append([pos_row, pos_column, attacked_piece])
                        
                        piece.possible_positions = temp_possible_positions
                break
            row -= 1

                                #  right 
        column = our_king.column + 1 
        row = our_king.row
        while column <=7 and row >= 0:
            piece =  board.get_piece_from_position(row, column)
            if piece: # need to know if there is a piece
                if our_piece == piece:     # if it is then is it our piece
                    if piece.row == opposite_piece.row  and piece.column < opposite_piece.column:
                        temp_possible_positions = []
                        if piece.piece_type == 'Rook' or piece.piece_type == 'Queen':
                            for pos_row, pos_column, attacked_piece in piece.possible_positions:
                                if pos_row == piece.row: # stays in the path between king and attacking piece
                                    temp_possible_positions.append([pos_row, pos_column, attacked_piece])
                        
                        piece.possible_positions = temp_possible_positions
                break
            column += 1

                                #  left 
        column = our_king.column - 1 
        row = our_king.row
        while column >=0 and row <= 7:
            piece =  board.get_piece_from_position(row, column)
            if piece: # need to know if there is a piece
                if our_piece == piece:     # if it is then is it our piece
                    if piece.row == opposite_piece.row  and piece.column > opposite_piece.column:
                        temp_possible_positions = []
                        if piece.piece_type == 'Rook' or piece.piece_type == 'Queen':
                            for pos_row, pos_column, attacked_piece in piece.possible_positions:
                                if pos_row == piece.row: # stays in the path between king and attacking piece
                                    temp_possible_positions.append([pos_row, pos_column, attacked_piece])
                        
                        piece.possible_positions = temp_possible_positions
                break
            column -= 1
            

                                # downwards 
        column = our_king.column  
        row = our_king.row + 1
        while column <=7 and row <= 7:
            piece =  board.get_piece_from_position(row, column)
            if piece: # need to know if there is a piece
                if our_piece == piece:     # if it is then is it our piece
                    if opposite_piece.row > piece.row  and opposite_piece.column == piece.column:
                        temp_possible_positions = []
                        if piece.piece_type == 'rook' or piece.piece_type == 'Queen' or piece.piece_type == 'Pawn':
                            for pos_row, pos_column, attacked_piece in piece.possible_positions:
                                if pos_column == piece.column: # stays in the path between king and attacking piece
                                    temp_possible_positions.append([pos_row, pos_column, attacked_piece])
                        
                        piece.possible_positions = temp_possible_positions
                break
            row += 1
        
        