
def check_if_under_attack(board):
        for piece in board.pieces_list:
            if piece.color != board.turn and piece.alive:
                piece.set_moves(board)
                for _, _, piece_under_attack in piece.possible_positions:
                    if piece_under_attack.__class__.__name__ == 'King':
                        return True
        return False
    
def check_game_status(board):
    for piece in board.pieces_list:
        if piece.color == board.turn and piece.alive:
            update_available_positions(board, piece)

    pieces_can_move = False
    for piece in board.pieces_list:
        if piece.color == board.turn and piece.alive:
            if piece.possible_positions:
                pieces_can_move = True
            else:
                pieces_can_move = False
    return pieces_can_move

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

def update_enpassant_info(active_piece, board):
    
    target_piece = None
    board.enpassant_possible = False
    for piece in board.pieces_list:
            if piece.__class__.__name__ == 'Pawn':
                if piece.passed and piece.color != active_piece.color and piece.alive:
                    target_piece = piece
                    target_piece.passed = False
                    
    if active_piece.__class__.__name__ == 'Pawn' and active_piece.can_do_enpassant:
        if active_piece.color == 'white':
            if not board.is_there_piece_on_position(target_piece.row - 1, target_piece.column):
                active_piece.possible_positions.append([target_piece.row - 1, target_piece.column, target_piece])
                print(target_piece)
        else:
            if active_piece.color == 'black':
                if not board.is_there_piece_on_position(target_piece.row + 1, target_piece.column):
                    active_piece.possible_positions.append([target_piece.row + 1, target_piece.column, target_piece])
                    print(target_piece)

    for piece in board.pieces_list:
        if piece.__class__.__name__ == 'Pawn':
            if piece.can_do_enpassant and piece.color == active_piece.color and piece.alive:
                piece.can_do_enpassant = False

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
                
    
   