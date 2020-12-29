
import pygame
from life import GameofLife

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
n=100

width, height = 5, 5
margin = 2
#size = (n*width+margin*4,n*height+margin*4) #(205,205)
print((margin + width) * n + margin)
#size= (n*width+margin*5,n*height+2*margin) #(125,110)
size= ((margin + width) * n + margin, (margin + height) * n + margin)
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("grid life")


pygame.init()
done=False
game = GameofLife(n)


clock = pygame.time.Clock()
ct = 0
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  
            break
    

    game.update()
    screen.fill(BLACK)
    grid = game.returnGrid()
    for row in range(n):
        for column in range(n):
            color = BLACK
            if grid[row][column] == 1:
                color = WHITE

            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])
    
    clock.tick(60)
    pygame.display.flip()


pygame.quit()
    
