import math
from turtle import *

# calcoli
def check_x(x1, x2, x3):
    if(x1 == x2 == x3):
        return False
    
    return True
    
def check_y(y1, y2, y3):
    if(y1 == y2 == y3):
        return False
    
    return True
    
def check_punti(p1, p2, p3):
    if(p1 == p2 or p1 == p3 or p2 == p3):
        return False
    
    return True

def area_triangolo(l1, l2, l3):
    # Calcolo il semiperimetro
    s = (l1 + l2 + l3) / 2
    # Controllo che i dati non siano negativi
    if s <= 0 or s - l1 <= 0 or s - l2 <= 0 or s - l3 <= 0:
        return 0  # Area non valida
    return math.sqrt(s * (s - l1) * (s - l2) * (s - l3))


# disegno
def imposta_finestra(width, height):
    setup(width, height)
    wn = Screen()

    # faccio in modo che il nord punti a 0 gradi così posso orientare il puntatore
    mode('logo')

def disegna_assi(width, height):
    penup()
    hideturtle()
    goto(-(width/2), 0)
    pendown()
    goto(width/2, 0)

    penup()
    goto(0, -(height/2))
    pendown()
    goto(0, height/2)
    penup()

def disegna_triangolo_e_punti(x1, y1, x2, y2, x3, y3, x4, y4):
    goto(x1, y1)
    pendown()
    dot()
    pendown()
    setheading(towards(x2, y2))

    goto(x2, y2)
    dot()
    setheading(towards(x3, y3))

    goto(x3, y3)
    dot()
    setheading(towards(x1, y1))

    goto(x1, y1)
    penup()

    goto(x4, y4)
    pendown()
    dot()