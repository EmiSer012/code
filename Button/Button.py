import random
import pygame, sys, random
from pygame.locals import *

#Pygame Init
pygame.init()
pygame.mixer.init()
 
#Colors
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
D_Grey = (150, 150, 150)
Grey = (200, 200, 200)

#Game Setup
Fps = 60
Display_width = 400
Display_height = 300
Display = pygame.display.set_mode((Display_width, Display_height))
pygame.display.set_caption('Display')
Display.fill(White)

cx = Display_width/5
cy = Display_height/2
r = Display_width/6

#Draw the Button
def Draw_Button(status, m, mx = 0, my = 0):

    color1, color2, color3 = D_Grey

    if status == 0:
        color1 = Red
        color2 = Red
        color3 = Grey
        c1 = 3
        c2 = 2

    elif status == 1:
        color1 = Green
        color2 = Green
        color3 = Grey
        c1 = 2
        c2 = 3
        
    elif status == 2:
        color1 = D_Grey
        color2 = D_Grey
        color3 = D_Grey
        c1 = 3
        c2 = 2

    pygame.draw.circle(Display, color1, (c1*cx+mx, cy+my), r+m)
    pygame.draw.rect(Display, color2, Rect(2*cx+mx, cy-r-m+my, cx+mx, r*2+m*2+my))
    pygame.draw.circle(Display, color3, (c2*cx+mx, cy+my), r+m)

#Main loop
def main ():
    
    #import sound
    Red_sound = pygame.mixer.Sound('/Users/piniuf300iq/Projects/code/interact/mixkit-game-show-wrong-answer-buzz-950.wav')
    Red_sound.set_volume(0.3)
    Green_sound = pygame.mixer.Sound('/Users/piniuf300iq/Projects/code/interact/ding-126626.mp3')
    Green_sound.set_volume(1)

    Draw_Button(2, 10)

    Button = False

    while True:
        if Button == False:
            Draw_Button(0, 0)
        else:
            Draw_Button(1, 0)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
            elif event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mouse_in_c1 = (2*cx - mx)**2 + (cy - my)**2 <= r**2
                mouse_in_c2 = (3*cx - mx)**2 + (cy - my)**2 <= r**2
                if Button == False:
                    if mouse_in_c1:
                        Button = not Button
                        Green_sound.play()

                else:
                    if mouse_in_c2:
                        Button = not Button
                        Red_sound.play()

            """
            elif event.type == MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                mouse_in_c1 = (2*cx - mx)**2 + (cy - my)**2 <= r**2
                mouse_in_c2 = (3*cx - mx)**2 + (cy - my)**2 <= r**2
                mouse_in_rect = 2*cx <= mx <= 3*cx and (cy-r) <= my <= (cy+r)
                if pygame.key.get_mods() and (mouse_in_c1 or mouse_in_c2 or mouse_in_rect):
                    if Button == False:
                        Draw_Button(0, 0, mx-Display_width, my-Display_height)
                        Display.fill(White)
                    else:
                        Draw_Button(1, 0, mx-Display_width, my-Display_height)
                        Display.fill(White)           
            """
                        
        pygame.display.update()
 
main()