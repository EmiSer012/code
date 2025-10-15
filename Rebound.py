import pygame
import random

pygame.init()

l_écran = 1000
h_écran = 700

x1 = random.randint(50, l_écran-50)
y1 = random.randint(50, h_écran-50)

x2 = random.randint(50, l_écran-50)
y2 = random.randint(50, h_écran-50)

x1_ = 2
y1_ = 3

x2_ = -1
y2_ = 2

screen = pygame.display.set_mode((l_écran,h_écran))

while True:

    screen.fill((0,0,0))
    
    pygame.draw.line(screen, (255,0,0), (x1,y1), (x2,y2), (7))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    x1 = x1 + x1_
    x2 = x2 + x2_

    y1 = y1 + y1_
    y2 = y2 + y2_

    if x1 not in range(0, l_écran):
        x1_ = x1_ * -1

    if x2 not in range(0, l_écran):
        x2_ = x2_ * -1
    
    if y1 not in range(0, h_écran):
        y1_ = y1_ * -1

    if y2 not in range(0, h_écran):
        y2_ = y2_ * -1        
    
    pygame.time.delay(10)