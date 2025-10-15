import cairo
import math
import random

Tgrille = 8

couleurs = [(231,142,163), # rose
            (59,102,170), # bleu
            (243,215,85), # jaune
            (223,96,61), # rouge
            (85,169,159)] # vert
couleurs = [(r/255, g/255, b/255) for (r,g,b) in couleurs]

Tcase = 100

# cercle
def circle(r,g,b):

    c.set_source_rgb(r,g,b)
    c.arc((ligne+1)*Tcase, (colonne+1)*Tcase, Tcase/2, 0, 2*math.pi)
    c.fill()

# page
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, Tcase*Tgrille, Tcase*Tgrille)
c = cairo.Context(surface)

# background
c.set_source_rgb(1,1,1)
c.paint()

# damier

c.set_source_rgb(0,0,0)

for colonne in range (Tgrille):

    for ligne in range (Tgrille):

        # noir / blanc
        if (ligne+colonne) % 2 == 0:
            
            c.rectangle(ligne*Tcase, colonne*Tcase, Tcase, Tcase)
            c.fill()

# ronds

for colonne in range (Tgrille-1):


    for ligne in range(Tgrille-1):


        circle(*random.choice(couleurs))


surface.write_to_png("/Users/piniuf300iq/Desktop/dessin.png")




