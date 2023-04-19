import xml.etree.ElementTree as ET
import random

enemy_files = ["enemy1.xml", "enemy2.xml", "enemy3.xml"]
enemy_file = random.choice(enemy_files)
enemy_tree = ET.parse(enemy_file)
enemy_root = enemy_tree.getroot()

enemy_name = enemy_root.find("name").text
enemy_description = enemy_root.find("description").text
enemy_life = int(enemy_root.find("life").text)
enemy_strength = int(enemy_root.find("strength").text)

your_life = 10

while True:
    print("Nombre del enemigo:", enemy_name)
    print("Descripción del enemigo:", enemy_description)
    print("Vida del enemigo:", enemy_life)
    print("Fuerza del enemigo:", enemy_strength)
    print("Tu vida:", your_life)

    action = input("¿Qué acción quieres hacer? (ataca para atacar, cualquier otra cosa para no hacer nada): ")

    if action == "ataca":
        damage = random.randint(0, 5)
        enemy_life -= damage
        print("Atacaste al enemigo y le quitaste", damage, "puntos de vida.")
    else:
        print("No hiciste nada.")

    enemy_damage = random.randint(0, 2)
    your_life -= enemy_damage
    print("El enemigo te atacó y te quitó", enemy_damage, "puntos de vida.")

    if enemy_life <= 0:
        print("Acabaste con él. ¡Ganaste!")
        break
    elif your_life <= 0:
        print("Mala suerte papu. ¡Perdiste!")
        break
