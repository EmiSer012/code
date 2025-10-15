from PIL import Image
import pygame
pygame.init

CHAR_WIDTH = 7
CHAR_HEIGHT = 9

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
RED = (255, 0, 0)

S_PIXEL = 10
MARGIN = 1

W_SCREEN = 70
H_SCREEN = 1*CHAR_HEIGHT

screen = pygame.display.set_mode((W_SCREEN * S_PIXEL, H_SCREEN * S_PIXEL))

char = Image.open('/Users/piniuf300iq/Desktop/char.png')

l = []
for h in range(CHAR_HEIGHT):
    for w in range(CHAR_WIDTH):
        c = (char.getpixel((w+3*CHAR_WIDTH, h+2*CHAR_HEIGHT))[0])//255
        l.append(c)

while True:
    #for a in range(W_SCREEN+len(message[0])):

    screen.fill(GREY)

    for i,q in enumerate(l):
        if q == 0:
            color = GREY
        elif q == 1:
            color = RED
        print(q, i%7, i//9)
        pygame.draw.rect(screen, color, pygame.Rect(i%CHAR_WIDTH*S_PIXEL, i//CHAR_WIDTH*S_PIXEL, S_PIXEL, S_PIXEL))

    for i in range(H_SCREEN):
        for j in range(W_SCREEN):
            pygame.draw.rect(screen, BLACK, pygame.Rect(j*S_PIXEL, i*S_PIXEL, S_PIXEL, S_PIXEL), MARGIN)
            
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.time.delay(200)