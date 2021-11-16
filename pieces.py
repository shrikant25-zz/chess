
class Pieces:
    def __init__(self, name, current_row, current_column, possible_positions=""):        
        self.name = name
        self.current_row = current_row
        self.current_column = current_column
        self.alive = True
        self.dead = False
        self.possible_positions = possible_positions

    def get_file_rank(self):
        current_rank = str(8 - int(self.current_row))
        current_file = chr(ord(str(self.current_column)) + 49)
        return current_file, current_rank
# def rules():
 #       if(pawn)