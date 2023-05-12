#!/usr/bin/python3
import xmltodict
import os
import random	

enemy_files = "enemy_xml"

print("BIENVENIDO A NUESTRO JUEGO")

nombre = input("Como te llamas? ")
difficulty = ""
player_health = 0
player_damage = 0

while difficulty not in ["facil", "intermedio", "dificil"]:
    difficulty = input("Seleccione dificultad (facil/intermedio/dificil): ")

if difficulty == "facil":
    player_health = 5000
    player_damage = random.randint(1000, 2000)
elif difficulty == "intermedio":
    player_health = 1000
    player_damage = random.randint(2000, 3000)
elif difficulty == "dificil":
    player_health = 500
    player_damage = random.randint(3000, 4000)

with open(enemy_files, "r") as f:
    xml_string = f.read()

enemy_dict = xmltodict.parse(xml_string)

def select_enemy(enemies):
    enemy = random.choice(enemies)
    name = str(enemy["name"])
    description = str(enemy["description"])
    health = int(enemy["health"])
    strength = int(enemy["damage"])
    print("\n***************************************")
    print(name)
    print(description)
    print("***************************************\n")
    return enemy, health, strength

eliminated_enemies = []
while True:
    remaining_enemies = [enemy for enemy in enemy_dict["enemies"]["enemy"] if enemy not in eliminated_enemies]
    if not remaining_enemies:
        print("¡Felicidades! ¡Has eliminado a todos los enemigos!")
        break
    juego, enemy_health, enemy_damage = select_enemy(remaining_enemies)	
    print(f"\nVida del jugador: {player_health}")
    print(f"Daño del jugador: {player_damage}")

    print("\nEs el turno del jugador")
    action = input("¿Qué quieres hacer? (ataca)")

    if action == "ataca":
        damage = random.randint(player_damage-1000, player_damage+1000)
        enemy_health -= damage
        print(f"Has quitado {damage} puntos de vida al enemigo.")
    else:
        print("Espabila papu")
        player_health -= enemy_damage

    if enemy_health <= 0:
        print(f"{juego['name']} ha sido derrotado.")
        eliminated_enemies.append(juego)
    else:
        print(f"El enemigo te ha quitado {enemy_damage} puntos de vida.")
        player_health -= enemy_damage

    if player_health <= 0:
        print("Mala suerte papu, has perdido.")
        break
