import pygame
pygame.init

white = (255, 255, 255)
black = (0, 0, 0)
grey = (150, 150, 150)
red = (255, 0, 0)

s_pixel = 30
b_pixel = 1

l_screen = 30
h_screen = 5

screen = pygame.display.set_mode((l_screen * s_pixel, h_screen * s_pixel))

message = [[1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
           [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]

while True:
    for a in range(l_screen+len(message[0])):

        screen.fill(grey)

        for y,p in enumerate(message):
            for x,q in enumerate(p):
                if q == 0:
                    color = grey
                elif q == 1:
                    color = red
                pygame.draw.rect(screen, color, pygame.Rect((a+x-len(p))*s_pixel, y*s_pixel, s_pixel, s_pixel))

        for i in range(h_screen):
            for j in range(l_screen):
                pygame.draw.rect(screen, black, pygame.Rect(j*s_pixel, i*s_pixel, s_pixel, s_pixel), b_pixel)
                
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.time.delay(200)