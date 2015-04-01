#!/usr/bin/python

from Grid import Grid

def main():
	g = Grid("/home/alex/Python/Smaller/rangeGrid/example")
	print(g.formatGrid())
	g.addSource(0,0,5,"Alberto")
	g.fillRange("Alberto")
	print(g.formatGrid())
main()
