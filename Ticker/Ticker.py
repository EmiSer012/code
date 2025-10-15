#import
from PIL import Image
import pygame
pygame.init

#define variables, constants & list
message = "Hello World"
CHAR_WIDTH = 7
CHAR_HEIGHT = 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
RED = (255, 0, 0)
S_PIXEL = 15
MARGIN = 1
W_SCREEN = 90
H_SCREEN = 1*CHAR_HEIGHT
screen = pygame.display.set_mode((W_SCREEN * S_PIXEL, H_SCREEN * S_PIXEL))
char = Image.open('/Users/piniuf300iq/Projects/code/Ticker/char.png')
l = []

#translate the message in a list of pixel
for x in range(len(message)):
    for h in range(CHAR_HEIGHT):
        for w in range(CHAR_WIDTH):
            c = (char.getpixel((w+((ord(message[x])-32)%18)*CHAR_WIDTH, h+((ord(message[x])-32)//18)*CHAR_HEIGHT))[0])//255
            l.append(c)

#backround
screen.fill(GREY)

#main loop
while True:

    #move of message
    for a in range(W_SCREEN+len(l)//CHAR_WIDTH):

        #draw the message
        for p,q in enumerate(l):

            #grey or red
            if q == 0:
                color = GREY
            elif q == 1:
                color = RED

            #put the lettre to form the message
            pygame.draw.rect(screen, color, pygame.Rect((p//(CHAR_WIDTH*CHAR_HEIGHT)*CHAR_WIDTH+p%CHAR_WIDTH+a-len(message)*CHAR_WIDTH)*S_PIXEL, (p%(CHAR_WIDTH*CHAR_HEIGHT)//CHAR_WIDTH)*S_PIXEL, S_PIXEL, S_PIXEL))
        
        #draw the grid
        for i in range(H_SCREEN):
            for j in range(W_SCREEN):
                pygame.draw.rect(screen, BLACK, pygame.Rect(j*S_PIXEL, i*S_PIXEL, S_PIXEL+1, S_PIXEL+1), width=1)
        
        #update the screen
        pygame.display.update()

        #quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #delay
        pygame.time.delay(50)