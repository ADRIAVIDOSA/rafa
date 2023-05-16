#!/usr/bin/python3
import json
import os
import random
import xmltodict

class Player:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack


class Enemy:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack


class SaveGame:
    def __init__(self, filename):
        self.filename = filename

    def save(self, player, enemy):
        data = {
            "player_name": player.get_name(),
            "player_level": player.get_level(),
            "player_health": player.get_health(),
            "player_attack": player.get_attack(),
            "enemy_name": enemy.get_name(),
            "enemy_level": enemy.get_level(),
            "enemy_health": enemy.get_health(),
            "enemy_attack": enemy.get_attack()
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def set_filename(self, filename):
        self.filename = filename


class LoadGame:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            player = Player(data["player_name"], data["player_level"], data["player_health"], data["player_attack"])
            enemy = Enemy(data["enemy_name"], data["enemy_level"], data["enemy_health"], data["enemy_attack"])
            return player, enemy

    def set_filename(self, filename):
        self.filename = filename


enemy_files = "enemy_xml"
save_file = "game_save.json"

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
    action = input("¿Qué quieres hacer? (1.ataca 2.Guardar i salir)")

    if action == 1:
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

# Crear una instancia de la clase SaveGame
save_game = SaveGame("save_game.json")

# Guardar la partida actual
save_game.save(Player(nombre, difficulty, player_health, player_damage), Enemy(juego["name"], juego["level"], enemy_health, enemy_damage))

# Crear una instancia de la clase LoadGame
load_game = LoadGame("save_game.json")

# Cargar la partida guardada
player_saved, enemy_saved = load_game.load()

# Imprimir los datos del jugador y del enemigo cargados
print("\nDATOS DE LA PARTIDA CARGADA")
print(f"Nombre del jugador: {player_saved.get_name()}")
print(f"Dificultad: {player_saved.get_level()}")
print(f"Vida del jugador: {player_saved.get_health()}")
print(f"Daño del jugador: {player_saved.get_attack()}")
print(f"Nombre del enemigo: {enemy_saved.get_name()}")
print(f"Nivel del enemigo: {enemy_saved.get_level()}")
print(f"Vida del enemigo: {enemy_saved.get_health()}")
print(f"Daño del enemigo: {enemy_saved.get_attack()}")

# Colorear la casilla de la columna "health" según los valores
player_health = player_saved.get_health()
enemy_health = enemy_saved.get_health()

# Colorear la casilla de la columna "health" del jugador
if player_health >= 80:
    player_health_color = "VERDE"
elif player_health >= 50:
    player_health_color = "AMARILLO"
else:
    player_health_color = "ROJO"

# Colorear la casilla de la columna "health" del enemigo
if enemy_health >= 80:
    enemy_health_color = "VERDE"
elif enemy_health >= 50:
    enemy_health_color = "AMARILLO"
else:
    enemy_health_color = "ROJO"

# Imprimir los datos del jugador y del enemigo con colores
print("\nDATOS DE LA PARTIDA CARGADA (CON COLORES)")
print(f"Nombre del jugador: {player_saved.get_name()}")
print(f"Dificultad: {player_saved.get_level()}")
print(f"Vida del jugador: {player_health} ({player_health_color})")
print(f"Daño del jugador: {player_saved.get_attack()}")
print(f"Nombre del enemigo: {enemy_saved.get_name()}")
print(f"Nivel del enemigo: {enemy_saved.get_level()}")
print(f"Vida del enemigo: {enemy_health} ({enemy_health_color})")
print(f"Daño del enemigo: {enemy_saved.get_attack()}")
