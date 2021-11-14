
class Pieces:
    def __init__(self, name, current_file, current_rank, possible_positions="", initial = ""):        
        self.initial = initial 
        self.name = name
        self.current_file = current_file
        self.current_rank = current_rank
        self.alive = True
        self.dead = False
        self.possible_positions = possible_positions

    def get_row_column(self):
        column = int(chr(ord(self.current_file) - 49))
        row = 8 - int(self.current_rank)
        return row, column

    def update_piece_position(self, row, column):
        self.current_rank = str(8 - int(row))
        self.current_file = chr(ord(str(column)) + 49)

