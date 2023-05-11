#!/usr/bin/python3

import random

class Enemy:
	def __init__ (self, name, health, strength, description = ""):
		self.name = name
		self.health = health
		self.strength = strength
		self.description = description
		
		print(self.name+": "+self.description)
	
	def atack (self, strength):
		return random.radiant(0,self.strength)

	def hurt (self, damage):
	
		if health >= 0:
			health-=damage
			return false
		if health  <= 0:
			return true

	def show_info (self):
		print("Name"+(self.name))
		print("Health"+str(self.health))
		print("Strength"+str(self.strength))
		if self.description != "":
			print("Description"+(self.description))


if __name__ == "__main__":

	enemigo = Enemy("Jacinto", 33, 10, "Simplemente Jacinto"); 
	
	enemigo.show_info()
	print(enemigo.hurt(enemigo.attack())

	enemigo.show_info()

