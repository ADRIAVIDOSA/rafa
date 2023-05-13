#!/usr/bin/python3
import xmltodict
import json
import os
import random	

ENEMY_FILES_XML = "enemy_xml.xml"
ENEMY_FILES_JSON = "enemy_json.json"
SAVE_XML = "game_save.xml"
SAVE_JSON = "game_save.json"

class Game:
    def __init__(self):
        self.enemy_dict = None
        self.player = None
        self.current_enemy = None
        self.eliminated_enemies = []
        self.load_enemy_file()
        self.load_game()

    def load_enemy_file(self):
        with open(ENEMY_FILES_XML, "r") as f:
            xml_string = f.read()
        self.enemy_dict = xmltodict.parse(xml_string)

    def select_enemy(self, enemies):
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

    def load_game(self):
        if os.path.exists(SAVE_XML):
            with open(SAVE_XML, "r") as f:
                game_dict = xmltodict.parse(f.read())
                self.player = game_dict["game"]["player"]
                self.eliminated_enemies = game_dict["game"]["eliminated_enemies"]["enemy"]
                enemy_number = game_dict["game"]["current_enemy"]["number"]
                enemy_health = game_dict["game"]["current_enemy"]["health"]
                enemies = self.enemy_dict["enemies"]["enemy"]
                self.current_enemy = enemies[int(enemy_number)]
                self.current_enemy["health"] = int(enemy_health)
        elif os.path.exists(SAVE_JSON):
            with open(SAVE_JSON, "r") as f:
                game_dict = json.loads(f.read())
                self.player = game_dict["player"]
                self.eliminated_enemies = game_dict["eliminated_enemies"]
                enemy_number = game_dict["current_enemy"]["number"]
                enemy_health = game_dict["current_enemy"]["health"]
                enemies = self.enemy_dict["enemies"]["enemy"]
                self.current_enemy = enemies[int(enemy_number)]
                self.current_enemy["health"] = int(enemy_health)
        else:
            self.create_new_game()

    def create_new_game(self):
        print("BIENVENIDO A NUESTRO JUEGO")
        self.player = {
            "name": input("Como te llamas? "),
            "difficulty": "",
            "health": 0,
            "damage": 0,
            "level": 1,
            "xp": 0
        }
        while self.player["difficulty"] not in ["facil", "intermedio", "dificil"]:
            self.player["difficulty"] = input("Seleccione dificultad (facil/intermedio/dificil): ")

        if self.player["difficulty"] == "facil":
            self.player["health"] = 5000
            self.player["damage"] = random.randint(1000, 2000)
        elif self.player["difficulty"] == "intermedio":
            self.player["health"] = 1000
            self.player["damage"] = random.randint(2000, 3000)
        elif self.player["difficulty"] == "dificil":
            self.player["health"] = 500
            self.player["damage"] = random.randint(3000, 4000)

        self.current_enemy, enemy_health,
def load_game_json():
    with open('save.json') as f:
        data = json.load(f)
    player_data = data['player']
    player = Player(player_data['health'], player_data['damage'], player_data['level'], player_data['xp'])
    enemy_data = data['current_enemy']
    current_enemy = enemies[enemy_data['number']]
    current_enemy.health = enemy_data['health']
    return player, current_enemy
