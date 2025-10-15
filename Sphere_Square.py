#import
import cairo
from operator import itemgetter

#variables
Length = 2000
Height = 2000
X_per = 0.8
Y_per = 0.5
Size_cube = 10
Am = 40

#liste
coordinates = [(0,0,0),]

#contexte
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, Length, Height)
c = cairo.Context(surface)

#fonctions
def draw_square(size):
    c.rectangle(0, 0, size, size)
    c.fill_preserve()
    c.set_source_rgb(0,0,0)
    c.set_line_width(size/50)
    c.stroke()

def draw_cube(r, g, b, size, X, Y, Z):
    c.save()

    c.translate(Length/2 + X*-X_per*size + Y*X_per*size, Height/2 + X*Y_per*size + Y*Y_per*size + Z*-2*Y_per*size)

    #matrices
    left = cairo.Matrix( -X_per, -Y_per,
                         0    ,     1,
                         0    ,     0)
    right = cairo.Matrix(X_per , -Y_per,
                         0    ,     1,
                         0    ,     0)
    top = cairo.Matrix(  X_per , -Y_per,
                         -X_per, -Y_per,
                         0    ,     0)

    #face du haut
    c.save()
    c.set_source_rgb(r, g, b)
    c.transform(top)
    draw_square(size)
    c.restore()

    #face de gauche
    c.save()
    c.set_source_rgb(r-0.2, g-0.2, b-0.2)
    c.transform(left)
    draw_square(size)
    c.restore()

    #face de droite
    c.save()
    c.set_source_rgb(r-0.5, g-0.5, b-0.5)
    c.transform(right)
    draw_square(size)
    c.restore()

    c.restore()

#fond
c.set_source_rgb(1, 1, 1)
c.paint()

#placer cubes
for i in range(-Am+1,Am):
    for j in range(-Am+1,Am):
        for k in range(-Am+1,Am):
            if i*i + j*j + k*k < Am*Am:
                coordinates += [(i,j,k)]

#cubes dans l'ordre
coordinates.sort(key=itemgetter(2,1,0))

#dessiner cubes
for (x,y,z) in coordinates:
    draw_cube(1/Am*abs(x), 1/Am*abs(y), 1/Am*abs(z), Size_cube, x, y, z)

#Créer le fichier
surface.write_to_png("test.png")
