# -*- coding: cp1252 -*-
from math import *
c = 3.0 * pow(10,8)
#Er = 4.25
print("entrer la constante Dielectrique (4.25 pour FR4) ")
Er = float(input())
print("entrer la frequence en MHz")
Fr = float(input()) * 1000000.0
print("entrer l'epaisseur du dielectrique en mm")
h = float(input()) / 1000.0 # h=0.0035 epaisseur du cuivre sur dielectric FR4
K0 = 2 * pi * (Fr/c)

def Lamda():
    return c/(Fr * sqrt(Er))

print ("Longueur d'onde corrigée (m): ", Lamda())

print ("Longueur d'onde (m): ", c/Fr)

W = (c/(2 * Fr)) * sqrt(2 / (Er + 1))

print ("Rapport W/h : ", W/h)

Ereff = ((Er + 1)/2.0) + (((Er - 1)/2.0) * pow (1 + ((12.0 * h)/W), -(0.5)))
print ("Effective Dielectric Ereff", Ereff)

DeltaL = 0.412 * h * ((Ereff + 0.3) / (Ereff - 0.258)) * (((W / h) + 0.264) / ((W / h) + 0.8))
print ("Delta L : ", DeltaL)

Leff = c/(2 * Fr * sqrt(Ereff))
print ("L effectif Leff", Leff)

L = Leff - (2 * DeltaL)
print ("dimension L (mm) : ", L * 1000)
print ("dimension W (mm): ", W * 1000)

Lg = 6.0 * h + L
print ("Lg (plan de masse)en mm : ", Lg * 1000)

Wg = 6.0 * h + W
print ("Wg (plan de masse) en mm : ", Wg * 1000)

Xf2 = (L/pi * acos(sqrt(3)/3))
print ("position de l'insersion en mm sur axe L (Xf) a partir du bord : ", Xf2 * 1000)

Z = 300.0 * (cos((pi * Xf2)/L) * cos((pi * Xf2)/L))
print ("Impedance du patch: ", Z)

#impedance de la ligne de transmission
Z1 = sqrt(50 * Z)
print ("Impedance de la ligne: ", Z1)

Yf = W / 2
print ("position de l'insersion en mm sur axe W (Yf) W/2 : ", Yf * 1000)
