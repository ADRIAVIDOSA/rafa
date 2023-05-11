import xmltodict
import os
import random	
nombre = input("Como te llamas? ")
os.system("clear")

enemy_files = "enemy_xml"
print(f"BIENVENIDO {nombre} A NUESTRO JUEGO")

with open(enemy_files, "r") as f:
	xml_string = f.read()

enemy_dict = xmltodict.parse(xml_string)

def select_enemy (number):
	name = str(enemy_dict["enemies"]["enemy"][number]["name"])
	description =str(enemy_dict["enemies"]["enemy"][number]["description"])
	health = int(enemy_dict["enemies"]["enemy"][number]["health"])
	strength = int(enemy_dict["enemies"]["enemy"][number]["damage"])
	print(name)
	print(description)
	print(health)
	print(strength)

player_health = 20


while True:
	numero = 0
	juego = select_enemy(numero)	
	action = input("¿Qué quieres hacer? (ataca/nothing)")

	if action == "ataca":
		damage = random.randint(0, 5)
		juego.health -= damage
		print(f"Has quitado {damage} puntos de vida al enemigo.")
	else:
		print("Espabila que te matan")

	player_damage = random.randint(0, 2)
	player_health -= player_damage
	print(f"El enemigo te ha quitado {player_damage} puntos de vida.")

	if (juego.health <= 0) and (numero>len(enemy_dict)) :
		print("Acabaste con él. ¡Felicidades!")
		break
    
	if player_health <= 0:
		print("Mala suerte papu, has perdido.")
		break
	numero=numero+1
	select_enemy(numero)
