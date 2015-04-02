#!/usr/bin/python
import os
from Grid import Grid

def main():
	g = Grid("example")
	g.addSource(0,0,5,"a")
	g.fillRange("a")
	clear()
	print(g.formatGrid())
	inp = ""
	while inp != "done":
		inp = raw_input("Move(x y)")
		xy = inp.split(" ")
		x = xy[0]
		y = xy[1]
		g.moveSource("a",int(x),int(y))
		clear()
		g.fillRange("a")
		print(g.formatGrid())
	
	
def clear():
	os.system("clear")	
main()
