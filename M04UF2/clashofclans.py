import xmltodict
import random


enemy_files = ["enemy.xml"]
enemy_file = random.choice(enemy_files)

with open(enemy_file, "r") as f:
	xml_string = f.read()

enemy_dict = xmltodict.parse(xml_string)


name = enemy_dict["enemy"]["name"]
description = enemy_dict["enemy"]["description"]
health = int(enemy_dict["enemy"]["health"])
strength = int(enemy_dict["enemy"]["strength"])


player_health = 20


while True:

	print(f"Your heatlth: {player_health}")
	print(f"\n{name}: {description}")
	print(f"Health: {health}, Strength: {strength}")


	action = input("¿Qué quieres hacer? (ataca/nothing)")

	if action == "ataca":
		damage = random.randint(0, 5)
		health -= damage
		print(f"Has quitado {damage} puntos de vida al enemigo.")
	else:
		print("Espabila que te matan")

	player_damage = random.randint(0, 2)
	player_health -= player_damage
	print(f"El enemigo te ha quitado {player_damage} puntos de vida.")

	if health <= 0:
		print("Acabaste con él. ¡Felicidades!")
		break
    
	if player_health <= 0:
		print("Mala suerte papu, has perdido.")
		break
