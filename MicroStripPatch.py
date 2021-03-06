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

def Lambda():
    return c/(Fr * sqrt(Er))

print ("Longueur d'onde corrig�e (m): ", Lambda())

print ("Longueur d'onde (m): ", c/Fr)

W = (c/(2 * Fr)) * sqrt(2 / (Er + 1))

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

# calcul suivant tir�s de
# cours_antennes_outils_modeles_transmission_oct14_v3
# Alexandre Boyer

Wrelle = W - 0.060 # modification pour adaptation
G1 = Wrelle/(120.0 * Lambda())
Rin = 1/(2 * G1)
print ("Impedance d'entr�e Rin (avec W - 0.06m): ",Rin)

Rpos = 50.0 # calcul du point d'insersion pour Z = 50 ohms
Xf = (L/pi * acos(sqrt(Rpos/Rin)))
print ("position de l'insersion en mm sur axe L (Xf) a partir du milieu :", Xf * 1000)

X = 0.083
Rpos = Rin * (cos((pi * X)/L) * cos((pi * X)/L))
print ("Resistance fct du point d'insersion :", Rpos)

#impedance de la ligne de transmission
Z1 = sqrt(50 * Rin)
print ("Impedance de la ligne: ", Z1)

Yf = W / 2
print ("position de l'insersion en mm sur axe W (Yf) W/2 : ", Yf * 1000)
