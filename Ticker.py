from PIL import Image
import pygame
pygame.init

CHAR_WIDTH = 4
CHAR_HEIGHT = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
RED = (255, 0, 0)

S_PIXEL = 30
MARGIN = 1

W_SCREEN = 30
H_SCREEN = 5

screen = pygame.display.set_mode((W_SCREEN * S_PIXEL, H_SCREEN * S_PIXEL))

img = Image.open('/Users/piniuf300iq/Desktop/font.png')

l = []
for s in range(CHAR_HEIGHT):
    for r in range(CHAR_WIDTH):
        c = (img.getpixel((r+2*CHAR_WIDTH, s+0*CHAR_HEIGHT))[0])//255
        l.append(c)

while True:
    #for a in range(W_SCREEN+len(message[0])):

    screen.fill(GREY)

    for i,q in enumerate(l):
        if q == 1:
            color = GREY
        elif q == 0:
            color = RED
        pygame.draw.rect(screen, color, pygame.Rect(i%4*S_PIXEL, i//4*S_PIXEL, S_PIXEL, S_PIXEL))

    for i in range(H_SCREEN):
        for j in range(W_SCREEN):
            pygame.draw.rect(screen, BLACK, pygame.Rect(j*S_PIXEL, i*S_PIXEL, S_PIXEL, S_PIXEL), MARGIN)
            
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.time.delay(200)