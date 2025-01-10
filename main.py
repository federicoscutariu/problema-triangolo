import math
from turtle import *
import os
import funzioni

with open("input.txt", 'r') as f:
    r = f.readline()

dati = [int(x) for x in r.split()]
datiSep = [[dati[i], dati[i + 1]] for i in range(0, len(dati), 2)]

# Coordinate dei punti
x1, y1 = datiSep[0]
x2, y2 = datiSep[1]
x3, y3 = datiSep[2]
x4, y4 = datiSep[3]

if(funzioni.check_x(x1, x2, x3) and funzioni.check_y(y1, y2, y3) and funzioni.check_punti(datiSep[0], datiSep[1], datiSep[2])):
    # Lati del triangolo principale
    l1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    l2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    l3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    # Area del triangolo principale
    A = funzioni.area_triangolo(l1, l2, l3)

    # Primo triangolo
    l1_1 = l1
    l2_1 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
    l3_1 = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
    A1 = funzioni.area_triangolo(l1_1, l2_1, l3_1)

    # Secondo triangolo
    l1_2 = math.sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2)
    l2_2 = l2
    l3_2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
    A2 = funzioni.area_triangolo(l1_2, l2_2, l3_2)

    # Terzo triangolo
    l1_3 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
    l2_3 = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
    l3_3 = l3
    A3 = funzioni.area_triangolo(l1_3, l2_3, l3_3)

    interno = abs((A1+A2+A3) - A) <= 0.0001 # Tolleranza di differenza

    if(interno): internoStr = "Sì"
    else: internoStr = "No"

    print("Punto interno:", internoStr)

    # rappresentazione grafica

    width = 800
    height = 600

    funzioni.imposta_finestra(width, height)

    funzioni.disegna_assi(width, height)
    funzioni.disegna_triangolo_e_punti(x1, y1, x2, y2, x3, y3, x4, y4)

    write(f"Punto interno: {internoStr}")
else:
    print("Triangolo invalido!")