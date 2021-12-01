import threading

def king_under_attack(board):
    for piece in board.pieces_list:
        if piece.color != board.turn and piece.alive:
            piece.set_moves(board)
            for _, _, opposite_piece_under_attack in piece.possible_positions:
                if opposite_piece_under_attack.__class__.__name__ == 'King':
                    piece.possible_positions = []
                    return True
                piece.possible_positions = []
    return False

def only_kings_remain(board):
    for piece in board.pieces_list:
        if piece.__class__.__name__ != 'King' and piece.alive:
            return False
    return True

def can_our_pieces_move(board, color):
    pieces_can_move = False
    for piece in board.pieces_list:
        if piece.color == color and piece.alive:
            if piece.possible_positions:
                pieces_can_move = True
    return pieces_can_move

def update_moves_of_all_pieces(board, color):
    jobs_list = []
    
    for piece in board.pieces_list:
        if piece.color == color and piece.alive:
            job = threading.Thread(target=update_available_positions, args=(board, piece))
            jobs_list.append(job)
    
    for job in jobs_list:
        job.start()

    for job in jobs_list:
        job.join()

def update_available_positions(board, our_piece):
    available_positions = []
    our_piece.set_moves(board)
    our_original_row = our_piece.row
    our_original_column = our_piece.column

    for our_possible_row, our_possible_column, opposite_piece_under_attack in our_piece.possible_positions:
        king_in_check = False
        our_piece.row = our_possible_row
        our_piece.column = our_possible_column

        if opposite_piece_under_attack:
            opposite_piece_under_attack.alive = False

        for opposite_piece in board.pieces_list:
            
            if board.turn != opposite_piece.color and opposite_piece.alive:
                opposite_piece.set_moves(board)

                for _, _, our_piece_under_attack in opposite_piece.possible_positions:
                    if our_piece_under_attack:
                        if our_piece_under_attack.__class__.__name__ == 'King':
                            king_in_check = True
                            break            
                    opposite_piece.possible_positions = []
            
            if king_in_check:
                break
        
        if opposite_piece_under_attack:
            opposite_piece_under_attack.alive = True
        
        if not king_in_check:
            available_positions.append([our_possible_row, our_possible_column, opposite_piece_under_attack])
            
    our_piece.row = our_original_row
    our_piece.column = our_original_column
    our_piece.possible_positions = available_positions

    if our_piece.__class__.__name__ == 'King' or our_piece.__class__.__name__ == 'Rook':
        if not king_under_attack(board) and not our_piece.moved:
            add_castling_info(board, our_piece)
        else:
            print("left")

def update_enpassant_info(active_piece, board):
    target_piece = None
    for piece in board.pieces_list:
        if piece.__class__.__name__ == 'Pawn':
            if piece.passed and piece.color != active_piece.color and piece.alive:
                target_piece = piece
                    
    if active_piece.__class__.__name__ == 'Pawn' and active_piece.can_do_enpassant:
        if active_piece.color == 'white':
            if not board.is_there_piece_on_position(target_piece.row - 1, target_piece.column):
                active_piece.possible_positions.append([target_piece.row - 1, target_piece.column, target_piece])
 
        else:
            if active_piece.color == 'black':
                if not board.is_there_piece_on_position(target_piece.row + 1, target_piece.column):
                    active_piece.possible_positions.append([target_piece.row + 1, target_piece.column, target_piece])
              

def remove_enpassant_data(board, active_piece):
    board.enpassant_possible = False
    for piece in board.pieces_list:
        if piece.__class__.__name__ == 'Pawn':
            if piece.can_do_enpassant and piece.color == active_piece.color and piece.alive: # finding other pieces that can do enpssant
                piece.can_do_enpassant = False
            if piece.passed and piece.color != active_piece.color and piece.alive:
                piece.passed = False

def check_if_passed(active_piece, board, new_row, new_column):

    if (active_piece.color == 'white' and active_piece.row - 2 == new_row) or (active_piece.color == 'black' and active_piece.row + 2 == new_row):
        
        if board.is_there_piece_on_position(new_row, new_column + 1):
            adjacent_piece1 = board.get_piece_from_position(new_row, new_column + 1)
            
            if adjacent_piece1.__class__.__name__ == 'Pawn' and adjacent_piece1.color != active_piece.color:
                adjacent_piece1.can_do_enpassant = True
                active_piece.passed = True
                board.enpassant_possible = True
        
        if board.is_there_piece_on_position(new_row, new_column - 1):
            adjacent_piece1 = board.get_piece_from_position(new_row, new_column - 1)
            
            if adjacent_piece1.__class__.__name__ == 'Pawn' and adjacent_piece1.color != active_piece.color:
                adjacent_piece1.can_do_enpassant = True
                active_piece.passed = True
                board.enpassant_possible = True
                

def add_castling_info(board, piece, possible_row=None, possible_column=None, castle=False):
    castling_positions_white =  [
                                {"side" : "left", "king":[7, 4], "rook":[7, 0], "square1": [7, 3], "square2" : [7, 2], "possible_position_king": [7, 2], "possible_position_rook": [7, 3]},
                                {"side" : "right", "king":[7, 4], "rook":[7, 7], "square1": [7, 5], "square2" : [7, 6], "possible_position_king": [7, 6], "possible_position_rook": [7, 5]}
                                ]
                                
    castling_positions_black =  [
                                {"side" : "left", "king":[0, 4], "rook":[0, 0], "square1": [0, 3], "square2" : [0, 2], "possible_position_king": [0, 2], "possible_position_rook": [0, 3]},
                                {"side" : "right", "king":[0, 4], "rook":[0, 7], "square1": [0, 5], "square2" : [0, 6], "possible_position_king": [0, 6], "possible_position_rook": [0, 5]}
                                ]

    if piece.color == 'white':
        castling_positions = castling_positions_white
    else:
        castling_positions = castling_positions_black

    if castle:
        if piece.__class__.__name__ == 'King' and not piece.moved:
            for pos in castling_positions:
                if (pos["side"] == "left" and piece.left_castle_possible) or (pos["side"] == "right" and piece.right_castle_possible): 
                    if pos["possible_position_king"][0] == possible_row and pos["possible_position_king"][1] == possible_column:
                        rook = board.get_piece_from_position(pos["rook"][0], pos["rook"][1])
                        if rook.moved:
                            return
                       
                        rook.row = pos["possible_position_rook"][0]
                        rook.column = pos["possible_position_rook"][1]
                        rook.moved = True

        if piece.__class__.__name__ == 'Rook' and not piece.moved:
            for pos in castling_positions:
                if (pos["side"] == "left" and piece.left_castle_possible) or (pos["side"] == "right" and piece.right_castle_possible):
                    if pos["possible_position_rook"][0] == possible_row and pos["possible_position_rook"][1] == possible_column:
                        king = board.get_piece_from_position(pos["king"][0], pos["king"][1])
                        if king.moved:
                            return
                       
                        king.row = pos["possible_position_king"][0]
                        king.column = pos["possible_position_king"][1]
                        king.moved = True

    else:    
        if piece.__class__.__name__ == 'King' and not piece.moved:
            for pos in castling_positions:
                other_piece = board.get_piece_from_position(pos["rook"][0], pos["rook"][1])
                if other_piece.__class__.__name__ == 'Rook' and other_piece.color == piece.color: 
                    if not other_piece.moved:
                        if is_the_square_safe(board, piece, pos["square1"]) and is_the_square_safe(board, piece, pos["square2"]):
                            piece.possible_positions.append([pos["possible_position_king"][0], pos["possible_position_king"][1], None])
                            
                            if pos["side"] == "left":
                                piece.left_castle_possible = True
                                other_piece.left_castle_possible = True
                           
                            else:
                                if pos["side"] == "right":
                                    piece.right_castle_possible = True
                                    other_piece.right_castle_possible = True

                        else:
                            if pos["side"] == "left":
                                piece.left_castle_possible = False
                                other_piece.left_castle_possible = False
                            
                            else:
                                if pos["side"] == "right":
                                    piece.right_castle_possible = False
                                    other_piece.right_castle_possible = False

        else:
            if piece.__class__.__name__ == 'Rook' and not piece.moved:
                for pos in castling_positions:
                    other_piece = board.get_piece_from_position(pos["king"][0], pos["king"][1])
                    if other_piece.__class__.__name__ == 'King' and other_piece.color == piece.color: 
                        if not other_piece.moved:
                            if is_the_square_safe(board, piece, pos["square1"]) and is_the_square_safe(board, piece, pos["square2"]):
                                piece.possible_positions.append([pos["possible_position_rook"][0], pos["possible_position_rook"][1], None])
                                if pos["side"] == "left":
                                    piece.left_castle_possible = True
                                    other_piece.left_castle_possible = True
                               
                                else:
                                    if pos["side"] == "right":
                                        piece.right_castle_possible = True
                                        other_piece.right_castle_possible = True
                            else:
                                if pos["side"] == "left":
                                    piece.left_castle_possible = False
                                    other_piece.left_castle_possible = False
                                else:
                                    if pos["side"] == "right":
                                        piece.right_castle_possible = False
                                        other_piece.right_castle_possible = False

def is_the_square_safe(board ,piece, square):
    row = square[0]
    column = square[1]
    for opposite_piece in board.pieces_list:
        if opposite_piece.row == row and opposite_piece.column == column:
            return False
        
        if opposite_piece.color != piece.color:
            opposite_piece.set_moves(board)
            for a_row, a_column, _ in opposite_piece.possible_positions:
                if opposite_piece.__class__.__name__ == 'Pawn': # because pawns attack diagonaly
                    if opposite_piece.color == 'white':
                        if opposite_piece.row == (row + 1) and (opposite_piece.column == (column - 1) or opposite_piece.column == (column + 1)):
                            return False       
                    
                    if opposite_piece.color == 'black':
                        if opposite_piece.row == (row - 1) and (opposite_piece.column == (column - 1) or opposite_piece.column == (column + 1)):
                            return False
                
                else:
                    if row == a_row and column == a_column:
                        return False
    return True

