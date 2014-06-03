#!/ usr/binenv python
# -*- coding : utf -8 -*-

#ACHTUNG: Das ist eine billige Nachmache der beliebten Spiele-APP: 2048

import tkinter
import random as r

########## Konsolen-Programm-Teile ###############
##################################################

#Hilfsfunktionen

def neuerStein():
	global feld
	passt = False
	while passt == False:
		x = r.randint(0,3)
		y = r.randint(0,3)
		if (feld[x][y] == 0):
			feld[x][y] = 2
			passt = True

def entferneNull(hilfsfeld):
	global steinBewegt
	for start in [3,2,1]:							
		if (hilfsfeld[start] == 0):
			i = start
			while (hilfsfeld[i] == 0 and i > 0):	
				i -= 1
			hilfsfeld[start] = hilfsfeld[i]
			hilfsfeld[i] = 0
			if (hilfsfeld[start] != 0):
				steinBewegt = True
	return hilfsfeld

def addiere(hilfsfeld):
	global steinBewegt
	for i in [3,2,1]:
		if (hilfsfeld[i] == hilfsfeld[i-1]):
			hilfsfeld[i] *= 2
			if (hilfsfeld[i] != 0):
				steinBewegt = True
			hilfsfeld[i-1] = 0
			hilfsfeld = entferneNull(hilfsfeld)
	return hilfsfeld
	
#Ausfuehrung Zug

def zugRechts():
	for y in range(4):
		hilfsfeld = []
		for x in range(4):
			hilfsfeld.append(feld[y][x])
		hilfsfeld = entferneNull(hilfsfeld)
		hilfsfeld = addiere(hilfsfeld)
		for x in [3,2,1,0]:
			feld[y][x] = hilfsfeld[x]

def zugLinks():
	for y in range(4):
		hilfsfeld = []
		for x in range(4):
			hilfsfeld.append(feld[y][3-x])		
		hilfsfeld = entferneNull(hilfsfeld)
		hilfsfeld = addiere(hilfsfeld)
		for x in [3,2,1,0]:
			feld[y][x] = hilfsfeld[3-x]

def zugOben():
	for x in range(4):
		hilfsfeld = []
		for y in range(4):
			hilfsfeld.append(feld[3-y][x])		
		hilfsfeld = entferneNull(hilfsfeld)
		hilfsfeld = addiere(hilfsfeld)
		for y in [3,2,1,0]:
			feld[y][x] = hilfsfeld[3-y]
			
def zugUnten():
	for x in range(4):
		hilfsfeld = []
		for y in range(4):
			hilfsfeld.append(feld[y][x])		
		hilfsfeld = entferneNull(hilfsfeld)
		hilfsfeld = addiere(hilfsfeld)
		for y in [3,2,1,0]:
			feld[y][x] = hilfsfeld[y]

######### Schnittstelle ##########################
##################################################

def bearbeiteLabel(x, y, zahl):
	global C
	global label
	C.itemconfigure(label[y][x], text = str(zahl))

def ausgabeFeld(feld):
	for y in range(4):
		for x in range(4):
			if (feld[y][x] == 0):
				tmp = ""
			else:
				tmp = feld[y][x]
			bearbeiteLabel(x,y,tmp)

################# Key-Events ######################
###################################################

def left_key(event):
	global steinBewegt
	steinBewegt = False
	zugLinks()
	if (steinBewegt):
		neuerStein()
	ausgabeFeld(feld)
	print(steinBewegt)
	
def right_key(event):
	global steinBewegt
	steinBewegt = False
	zugRechts()
	if (steinBewegt):
		neuerStein()
	ausgabeFeld(feld)
	print(steinBewegt)
	
def up_key(event):
	global steinBewegt
	steinBewegt = False
	zugOben()
	if (steinBewegt):
		neuerStein()
	ausgabeFeld(feld)
	print(steinBewegt)
	
def down_key(event):
	global steinBewegt
	steinBewegt = False
	zugUnten()
	if (steinBewegt):
		neuerStein()
	ausgabeFeld(feld)
	print(steinBewegt)


##############################################
##############################################

#INIT
#1) Tkinter-Zeugs
root = tkinter.Tk()
root.geometry("440x440+500+200")
C = tkinter.Canvas(root, height=440, width=440)
label = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for y in range(4):
	for x in range(4):
		square = C.create_rectangle(5+110*x,5+110*y,110*x+105,110*y+105, width=5)
		label[y][x] = C.create_text(55+x*110, 55+y*110, text = "", font=("Courier",25,"bold"))
		C.pack()
		

root.bind("<Left>", left_key)
root.bind("<Right>", right_key)
root.bind("<Up>", up_key)
root.bind("<Down>", down_key)

#2) Konsolen-Zeugs
feld = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
neuerStein()
neuerStein()
ausgabeFeld(feld)
steinBewegt = False				#zeigt an, ob ein Stein bewegt wurde --> Auswirkungen auf "neuerStein()"

#MAIN
root.mainloop()
