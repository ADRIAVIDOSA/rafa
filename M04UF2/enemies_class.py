#!/usr/bin/python3

import xmltodict
from enemy_class import Enemy

class Enemies:
	def __init__(self):
		xml_file = open("enemy_xml", "r")
		enemies_tmp = xmltodict.parse(xml_file.read())
		
		enemies_list = enemies_tmp['enemies']['enemy']
		
		self.enemies = []
		for e in enemies_list:
			 self.enemies.append(Enemy(e["name"], e["health"], e["damage"], "TE"))

if __name__ == "__main__":
	enemies = Enemies()
