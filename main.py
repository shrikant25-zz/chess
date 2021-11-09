import pygame

# colors and thier hex values
color = {'green' : [0, 128, 0],  
         'red' : [255, 0, 0],
         'dark_red' : [150, 0, 0], 
         'black' : [0, 0, 0],  
         'white' : [250, 250, 250],
         'dark_grey' : [42, 53, 61],
         'silver' : [200, 200, 200],
         'blue' : [0, 0, 128],
         'yellow' :[255, 255, 0] }  


ROWS = COLUMNS = 8
WIDTH = HEIGHT = 712
SQUARE_DIMENSIONS = (WIDTH - 12) // ROWS # 87
BORDERLINE = WIDTH // SQUARE_DIMENSIONS # 8

class Game:
    def __init__(self):
        pygame.init()
        self.Window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.rungame()

    def create_grid(self):
        for row in range(ROWS):
            for column in range(COLUMNS):
                square_color = (('white', 'black') [(row+column) & 1]) 
                # adding distance equal to borderline in starting points of sqaure shifts them enough to have place for a borderline 
                pygame.draw.rect(self.Window, color[square_color], ((column * SQUARE_DIMENSIONS)+BORDERLINE, (row * SQUARE_DIMENSIONS)+BORDERLINE, SQUARE_DIMENSIONS, SQUARE_DIMENSIONS))
             

    def rungame(self):
        
        pygame.display.set_caption("CHESS") 
        self.Window.fill(color['dark_red'])  
        run = True
        self.create_grid()
        pygame.display.update()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    