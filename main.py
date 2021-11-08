import pygame

# colors and thier hex values
color = {'green' : [0, 128, 0],  
         'red' : [255, 0, 0],  
         'black' : [0, 0, 0],  
         'white' : [250, 250, 250]}  

ROWS = COLUMNS = 8
WIDTH = HEIGHT = 700
SQUARE_DIMENSIONS = WIDTH // ROWS

class Game:
    def __init__(self):
        pygame.init()
        self.Window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.rungame()

    def create_grid(self):
        for row in range(ROWS):
            for column in range(COLUMNS):
                square_color = (('white', 'black') [(row+column) & 1])
                pygame.draw.rect(self.Window, color[square_color], (column * SQUARE_DIMENSIONS, row * SQUARE_DIMENSIONS, SQUARE_DIMENSIONS, SQUARE_DIMENSIONS))
             

    def rungame(self):
        
        pygame.display.set_caption("CHESS")    
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
    