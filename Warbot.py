from tkinter import *
import random
import time

#----------------------------------------------------------

fichero_luch=open("Characthers.txt","r")

luchadores=fichero_luch.readlines()

fichero_luch.close()

for i in range(len(luchadores)):
    luchadores[i]=luchadores[i].rstrip("\n")

#----------------------------------------------------------

fichero_muert=open("Deaths.txt","r")

muertes=fichero_muert.readlines()

fichero_muert.close()

for i in range(len(muertes)):
    if i!="":
        muertes[i]=muertes[i].rstrip("\n")

# print(muertes)
#----------------------------------------------------

vivos=[]
for n in luchadores:

    if n!="":
        vivos.append(n)

    # print(n+" añadido a la guerra")
    # print(str(len(vivos))+" participantes")

# print (luchadores)
# print (vivos)

muertos=[]

input("-------------Press enter to start-----------------")

while 1 < len(vivos):

    # input()

    asesino = vivos[random.randrange(len(vivos))]
    muerte = muertes[random.randrange(len(muertes))]
    cuerpo = vivos[random.randrange(len(vivos))]

    while asesino=="":
        asesino = vivos[random.randrange(len(vivos))]

    while cuerpo=="":
        cuerpo = vivos[random.randrange(len(vivos))]

    while asesino==cuerpo:
            cuerpo = vivos[random.randrange(len(vivos))]

    vivos.pop(vivos.index(cuerpo))
    muertos.append(cuerpo)

    # print(asesino+" "+muerte+" "+cuerpo+"\n\n")
    print(muerte.format(killer=asesino,dead=cuerpo))
    print(str(len(vivos))+" left alive")
    # time.sleep(3)

print("\n¡"+vivos[0]+" has won!")

