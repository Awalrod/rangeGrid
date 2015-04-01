#!/usr/bin/python

from Grid import Grid

def main():
	g = Grid("example")
	print(g.formatGrid())
	g.addSource(0,0,5,"Alberto")
	g.fillRange("Alberto")
	print(g.formatGrid())
main()
