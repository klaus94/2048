#!/ usr/binenv python
# -*- coding : utf -8 -*-

#ACHTUNG: Das ist eine billige Nachmache der beliebten Spiele-APP: 2048

import tkinter
import random as r
from tkinter import Menu
import os
import sys

########## Konsolen-Programm-Teile ###############
##################################################

#Hilfsfunktionen

def neuerStein():
	global feld
	global punkte

	passt = False
	while passt == False:
		x = r.randint(0,3)
		y = r.randint(0,3)
		if (feld[x][y] == 0):
			feld[x][y] = 2
			passt = True
	punkte += 2
	if (punkte >= 0):
		print("Aktuelle Punktzahl: " + str(punkte))

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
	global square
	C.itemconfigure(square[y][x], fill="#00FF00")
	C.itemconfigure(label[y][x], text = str(zahl))

def ausgabeFeld(feld):
	for y in range(4):
		for x in range(4):
			if (feld[y][x] == 0):			#Zahl
				tmp = ""
			else:
				tmp = feld[y][x]
			bearbeiteLabel(x,y,tmp)

			if (feld[y][x] == 0):			#Farbe
				color = "#FFFFFF"
			elif (feld[y][x] == 2):
				color = "#FFFF33"
			elif (feld[y][x] == 4):
				color = "#E8EC41"
			elif (feld[y][x] == 8):
				color = "#D1DA4F"
			elif (feld[y][x] == 16):
				color = "#B9C75D"
			elif (feld[y][x] == 32):
				color = "#A2B56B"
			elif (feld[y][x] == 64):
				color = "#8BA279"
			elif (feld[y][x] == 128):
				color = "#749086"
			elif (feld[y][x] == 256):
				color = "#5D7D94"
			elif (feld[y][x] == 512):
				color = "#466BA2"
			elif (feld[y][x] == 1024):
				color = "#2E58B0"
			elif (feld[y][x] == 2048):
				color = "#1746BE"
			C.itemconfigure(square[y][x], fill=color)

################# Key-Events ######################
###################################################

def left_key(event):
	global steinBewegt
	steinBewegt = False
	zugLinks()
	if (steinBewegt):
		neuerStein()
	ausgabeFeld(feld)
	#print(steinBewegt)
	
def right_key(event):
	global steinBewegt
	steinBewegt = False
	zugRechts()
	if (steinBewegt):
		neuerStein()
	ausgabeFeld(feld)
	#print(steinBewegt)
	
def up_key(event):
	global steinBewegt
	steinBewegt = False
	zugOben()
	if (steinBewegt):
		neuerStein()
	ausgabeFeld(feld)
	#print(steinBewegt)
	
def down_key(event):
	global steinBewegt
	steinBewegt = False
	zugUnten()
	if (steinBewegt):
		neuerStein()
	ausgabeFeld(feld)
	#print(steinBewegt)

############### Menu - Funktionen ############
##############################################

def saveAndQuit():
	os.system("clear")
	name = input("Gib deinen Namen ein: ")
	my_file = open("highscore", "a")
	my_file.write(str(punkte) + " " + name + "\n")
	my_file.close()
	root.quit()

def control():
	os.system("clear")
	print("Klicke eine Pfeiltaste und bestimmt damit die Richtung, in die du die Steine bewegen willst!")
	
def about():
	os.system("clear")
	print("Bei diesem Spiel geht es darum, moeglichst viele Runden zu 'ueberleben'.\n\
Indem du eine Richtung vorgibst, werden alle Steine versuchen, sich in diese Richtung zu bewegen.\n\
Ein Stein verschiebt sich in eine Richtung, wenn die Stelle neben ihm frei oder ein Stein mit dem gleichen Zahlenwert ist.\n\
Der Stein kann auch erst ein Stueck 'wandern' bevor er auf einen gleichartigen Stein stoesst.\n\
Treffen nun zwei gleichartige Steine aufeinander, so verbinden sie sich. Dabei addieren sich ihre Betraege.\n\
Nach jedem Zug, erscheint irgendwo auf dem Feld zufaellig ein neuer Stein mit dem Wert: 2.\n\n\
Entwickle jetzt eine Strategie, mit der du ueberlebst!!!")

def showHighscore():
	os.system("gedit highscore")

##############################################
##############################################

#INIT
#1) Tkinter-Zeugs
root = tkinter.Tk()
root.geometry("440x440+500+200")

menu = tkinter.Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Punktzahl speichern und beenden", command=saveAndQuit)
filemenu.add_command(label="Highscore anzeigen", command=showHighscore)
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Hilfe", menu=helpmenu)
helpmenu.add_command(label="Über", command=about)
helpmenu.add_command(label="steuerung", command=control)

C = tkinter.Canvas(root, height=440, width=440)
label = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
square = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for y in range(4):
	for x in range(4):
		square[y][x] = C.create_rectangle(5+110*x,5+110*y,110*x+105,110*y+105, width=5)
		label[y][x] = C.create_text(55+x*110, 55+y*110, text = "", font=("Courier",25,"bold"))
		C.pack()

punkte = -4		

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
