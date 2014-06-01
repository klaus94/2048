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
		
def zugRechts():
	for y in range(4):			#alle Zeilen nacheinander durchtesten
		for x in [2,1,0]:		#Felder 0 bis 2 testen, ob nach rechts-verschiebung moeglichd
			if (feld[y][x] != 0):
				if (feld[y][x+1] == 0):
					i = x			#i...Hilfsvariable
					while (i >= 0):
						feld[y][i+1] = feld[y][i]
						feld[y][0] = 0				#neues Feld am Zeilenanfang
						i -= 1
				if (feld[y][x] == feld[y][x+1]):	#rechtes Feld == aktuelles Feld
					feld[y][x+1] = 2 * feld[y][x+1]
					i = x - 1		
					while (i >= 0):
						feld[y][i+1] = feld[y][i]
						feld[y][0] = 0
						i -= 1
			
def ausgabeFeld():
	ausgabe = ""
	for y in range(4):
		ausgabe += "\t\t%i | %i | %i | %i\n"%(feld[y][0], feld[y][1], feld[y][2], feld[y][3])
	print(ausgabe)
	print(feld)
		
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
	elif (eingabe == "d"):
		zugRechts()
		neuerStein()
		ausgabeFeld()
	elif (eingabe == "x"):
		print("aufgegeben")
	else:
		print("nur die Buchstaben: w,a,s,d oder x verwenden!")
