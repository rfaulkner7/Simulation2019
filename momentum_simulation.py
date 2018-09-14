from __future__ import division
from visual import *

#simulation only considers momentum changes due to pushing force on cart
#does not take into consideration change in momentum due to hitting gameboard

# Constants
mcart = 0.500 #mass in kg

#Objects
cart = sphere(pos=vector(0, 0, 0), radius=0.15, color=color.red)
trail = curve(color=cart.color)

#Initial Conditions
vcart=vector(-0.142, 0.416, 0)
pcart = mcart*vcart
print("cart momentum=", pcart)

deltat = 0.01
t = 0
scene.autoscale = 0 #prevents screen from zooming out

#Calculation Loop
fPush = vector(-.104, 0, 0) #pushing force acting on cart
while t <14.01:
    pcart = pcart + fPush*deltat
    vcart = pcart/mcart
    cart.pos = cart.pos + vcart*deltat
    trail.append(pos=cart.pos)
    t = t + deltat
    rate(100)
print(cart.pos)
print(vcart)
