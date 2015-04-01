#!/usr/bin/python

class Source:
	x = None
	y = None
	movePoints = 0
	name = ""
	
	def __init__(self,nx,ny,nMove, nName):
		self.x = nx
		self.y = ny
		self.movePoints = nMove
		self.name = nName
