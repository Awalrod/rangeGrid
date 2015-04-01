#!/usr/bin/python
from Point import Point
from Source import Source
from colorama import init
from colorama import Back
init()

class Grid:
	canWalk = Back.RESET
	cantWalk = Back.WHITE
	inRange = Back.GREEN
	outRange = Back.RED
	
	
	
	height,width = None,None
	characterValues = {}
	grid = []
	sources = {}
	
	def __init__(self,fn):
		f = open(fn,"r")
		fLines = f.readlines()
		dim = fLines.pop(0)
		dim = dim.split(" ")
		self.width = int(dim[0])
		self.height = int(dim[1])
		gridLines = []
		y = 0
		while y < self.height:
			newLine = fLines.pop(0)
			newLine = newLine.strip()
			gridLines.append(newLine)
			y+=1
		
		valueLines = []
		for line in fLines:
			print(line)
			valueLines.append(line.strip("\n"))
		
		for line in valueLines:
			splitLine = line.split(" ")
			self.characterValues[splitLine[0]] = None if splitLine[1]=="None" else int(splitLine[1])
		
		for line in gridLines:
			if len(line) != self.width:
				raise ValueError("Grid Incorrect Shape\n"+line+"\n"+str(len(line))+"\n"+str(self.width))
			lineList = []
			for c in line:
				if not(c in self.characterValues):
					raise ValueError("Invalid Grid Character\n"+c)
				color = ""
				if self.characterValues[c] == None:
					color = self.cantWalk
				else:
					color = self.canWalk
				lineList.append(Point(c,color,self.characterValues[c]))
			self.grid.append(lineList)
		
	def formatGrid(self):
		s = []
		for line in self.grid:
			for p in line:
				s.append(p.formatted())
			s.append(Back.RESET+"\n")
		return "".join(s)
	
				
		f.close()
		
	def addSource(self,x,y,movePoints,name):
		self.sources[name] = Source(x,y,movePoints,name)
		
	def removeSource(self,name):
		self.sources.pop(name)
	
	def fillRange(self,name):
		s = self.sources[name]
		movePoints = s.movePoints
		x = s.x
		y = s.y
		
		self.fill(x-1,y,movePoints)
		self.fill(x+1,y,movePoints)
		self.fill(x,y+1,movePoints)
		self.fill(x,y-1,movePoints)
					
		self.fill(x-1,y-1,movePoints)		
		self.fill(x+1,y+1,movePoints)
		self.fill(x-1,y+1,movePoints)
		self.fill(x+1,y-1,movePoints)
		
		self.grid[y][x].setColor(Back.YELLOW)	
		
	def fill(self,x,y,movePoints): 
		xIsInBounds = x>=0 and x < self.width
		yIsInBounds = y>= 0 and y < self.height
		if xIsInBounds and yIsInBounds:
			p = self.grid[y][x]
			if p.walkValue != None:
				if movePoints >= p.walkValue:
					self.grid[y][x].setColor(self.inRange)
					movePoints -= p.walkValue
					self.fill(x-1,y,movePoints)
					self.fill(x+1,y,movePoints)
					self.fill(x,y+1,movePoints)
					self.fill(x,y-1,movePoints)
					
					self.fill(x-1,y-1,movePoints)
					self.fill(x+1,y+1,movePoints)
					self.fill(x-1,y+1,movePoints)
					self.fill(x+1,y-1,movePoints)
			
				
		
			
			
				
		
		
		
			
