# -*- coding: cp1252 -*-
# -*- coding: cp1252 -*-
import math
c = 3.0 * pow(10,8)
#Er = 2.5
print("entrer la constante Dielectrique (4.35 pour FR4) ")
Er = float(input())
#Fr = 440000000.0
print("entrer la frequence en MHz")
Fr = float(input()) * 1000000.0
print("entrer l'epaisseur du dielectrique en mm")
h = float(input()) / 1000 # h = 0.0016 epaisseur du dielectric FR4

def Lamda():
    return c/(Fr * math.sqrt(Er))

print "Longueur d'onde corrigée (m): ", Lamda()
W = (c/(2 * Fr)) * math.sqrt(2 / (Er + 1))


Ereff = ((Er + 1)/2.0) + (((Er - 1)/2.0) * pow (1 + ((12.0 * h)/W), -(0.5)))
print "Effective Dielectric Ereff", Ereff

Leff = c/(2 * Fr * math.sqrt(Ereff))
print "L efficace Leff", Leff

DeltaL = 0.412 * h * ((Ereff + 0.3) / (Ereff - 0.258)) * (((W / h) + 0.264) / ((W / h) + 0.8))
print "Delta L : ", DeltaL

L = Leff - (2* DeltaL)
print "dimension L (m) : ", L
print "dimension W (m): ", W

Lg = 6 * h + L
print "Lg : ", Lg

Wg = 6 * h + W
print "Wg : ", Wg

Xf1 = L * 0.15
print "position du via en m sur axe L (Xf) a partir du milieu (L/2): ", Xf1
Xf2 = L / (2 * math.sqrt(Ereff))
print "position du via en m sur axe L (Xf) a partir du bord : ", Xf2

# Impedance Z0 = 300 * cos^2 ((pi * x) / L)
# pour Z0 = 50 ohms

Z = 300 * (math.cos((3.14 * Xf2)/L) * math.cos((3.14 * Xf2)/L))
print "Impedance : ", Z

Yf = W / 2
print "position du via en m sur axe W (Yf) W/2 : ", Yf
