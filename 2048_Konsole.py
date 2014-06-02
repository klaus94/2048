#!/ usr/binenv python
# -*- coding : utf -8 -*-

import random as r

#Wirft zufaellig einen neuen Stein an eine Freie Position
def neuerStein():
	global feld
	passt = False
	while passt == False:
		x = r.randint(0,3)
		y = r.randint(0,3)
		if (feld[x][y] == 0):
			feld[x][y] = 2
			passt = True
			

#z.B.: aus [0,2,0,2] mache [0,0,2,2]
#oder anders gesagt: Klatsche alle Nicht-Nullen an den rechten Rand
def entferneNull(hilfsfeld):
	for start in [3,2,1]:							#Ende der Liste
		if (hilfsfeld[start] == 0):
			i = start
			while (hilfsfeld[i] == 0 and i > 0):	#so lange nach links, bis Nicht-Null-Feld oder Anfang
				i -= 1
			hilfsfeld[start] = hilfsfeld[i]
			hilfsfeld[i] = 0
	return hilfsfeld


#z.B.: aus [0,0,2,2] mache [0,0,0,4]
#oder anders: Rechne die gleichen Felder, die nebeneinander stehen zusammen
def addiere(hilfsfeld):
	for i in [3,2,1]:
		if (hilfsfeld[i] == hilfsfeld[i-1]):
			hilfsfeld[i] *= 2
			hilfsfeld[i-1] = 0
			hilfsfeld = entferneNull(hilfsfeld)
	return hilfsfeld
	


################## es folgen moegliche Zuege ##################
###############################################################

def zugRechts():
	for y in range(4):
		#Hilfsfeld erstellen
		hilfsfeld = []
		for x in range(4):
			hilfsfeld.append(feld[y][x])
			
		#Nullen entfernen
		hilfsfeld = entferneNull(hilfsfeld)
		
		#gleiche, nebeneinanderliegende Felder zusammenfassen
		hilfsfeld = addiere(hilfsfeld)
		
		#Zeile in feld zurueck ueberfuehren
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
		

#Diese Funktion kann etwas ganz tolles: Sie gibt das Feld aus ;)			
def ausgabeFeld():
	ausgabe = ""
	for y in range(4):
		ausgabe += "\t\t%i | %i | %i | %i\n"%(feld[y][0], feld[y][1], feld[y][2], feld[y][3])
	print(ausgabe)
	
####################################################################
####################################################################
		
#INIT (haha, du hast es nicht in das Hauptprogramm geschafft)
feld = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
neuerStein()
neuerStein()
eingabe = ""
ausgabeFeld()


#MAIN (- die Wichtigste aller Funktionen )
while eingabe != "x":			#x... Aufgeben
	eingabe = raw_input("neuer Zug mit 'w','a','s','d' oder 'x' zum aufgeben ")
	if (eingabe == "w"):
		zugOben()
		neuerStein()
		ausgabeFeld()
	elif (eingabe == "a"):
		zugLinks()
		neuerStein()
		ausgabeFeld()
	elif (eingabe == "s"):
		zugUnten()
		neuerStein()
		ausgabeFeld()
	elif (eingabe == "d"):
		zugRechts()
		neuerStein()
		ausgabeFeld()
	elif (eingabe == "x"):
		print("aufgegeben")
	else:
		print("nur die Buchstaben: w,a,s,d oder x verwenden!")
