#!/ usr/binenv python
# -*- coding : utf -8 -*-

#ACHTUNG: Das ist eine billige Nachmache der beliebten Spiele-APP: 2048

import tkinter

def left_key(event):
	print("Left key pressed")
	
def right_key(event):
	print("Right key pressed")
	
def up_key(event):
	print("Up key pressed")
	
def down_key(event):
	print("Down key pressed")

root = tkinter.Tk()
root.geometry("440x440+500+200")
C = tkinter.Canvas(root, height=440, width=440)
for y in range(5, 400, 110):
	for x in range(5, 400, 110):
		square = C.create_rectangle(x,y,x+100,y+100, width=5)
		C.pack()

label = C.create_text(55, 55, text = "1024", font=("Courier",25,"bold"))
C.pack()		


root.bind("<Left>", left_key)
root.bind("<Right>", right_key)
root.bind("<Up>", up_key)
root.bind("<Down>", down_key)


root.mainloop()
