#!/ usr/binenv python
# -*- coding : utf -8 -*-

import random as r


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
	for start in [3,2,1]:							#Ende der Liste
		if (hilfsfeld[start] == 0):
			i = start
			while (hilfsfeld[i] == 0 and i > 0):	#so lange nach links, bis Nicht-Null-Feld oder Anfang
				i -= 1
			hilfsfeld[start] = hilfsfeld[i]
			hilfsfeld[i] = 0
	return hilfsfeld


def addiere(hilfsfeld):
	for i in [3,2,1]:
		if (hilfsfeld[i] == hilfsfeld[i-1]):
			hilfsfeld[i] *= 2
			hilfsfeld[i-1] = 0
			hilfsfeld = entferneNull(hilfsfeld)
	return hilfsfeld
	

	
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
		
			
def ausgabeFeld():
	ausgabe = ""
	for y in range(4):
		ausgabe += "\t\t%i | %i | %i | %i\n"%(feld[y][0], feld[y][1], feld[y][2], feld[y][3])
	print(ausgabe)
	
		
#INIT
feld = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
neuerStein()
neuerStein()
eingabe = ""
ausgabeFeld()


#MAIN
while eingabe != "x":			#x... Aufgeben
	eingabe = raw_input("neuer Zug mit 'w','a','s','d' oder 'x' zum aufgeben ")
	if (eingabe == "w"):
		pass
	elif (eingabe == "a"):
		pass
	elif (eingabe == "s"):
		pass
		#print entferneNull([2,0,0,2])
	elif (eingabe == "d"):
		zugRechts()
		neuerStein()
		ausgabeFeld()
	elif (eingabe == "x"):
		print("aufgegeben")
	else:
		print("nur die Buchstaben: w,a,s,d oder x verwenden!")
