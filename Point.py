#!/usr/bin/python


class Point:
	text = ""
	color = ""
	walkValue = 1
	
	def __init__(self,t,c,w):
		self.text = t
		self.color = c
		self.walkValue = w
		
	def setText(self,t):
		self.text = t
		
	def setColor(self,c):
		self.color = c
	
	def setWalkValue(self, w):
		self.walkValue = w
	
	def formatted(self):
		return self.color+self.text
