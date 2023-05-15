import json
import random
import xml.etree.ElementTree as ET
import os
import sys

def pcolor(texto, color="default", nueva_linea=True):
    colores = {
        "negro": "\033[30m",
        "rojo": "\033[31m",
        "verde": "\033[32m",
        "amarillo": "\033[33m",
        "azul": "\033[34m",
        "morado": "\033[35m",
        "cian": "\033[36m",
        "blanco": "\033[37m",
        "default": "\033[0m"
    }
    
    codigo_color = colores.get(color.lower(), colores["default"])
    texto_coloreado = codigo_color + texto + colores["default"]
    
    if nueva_linea:
        print(texto_coloreado)
    else:
        print(texto_coloreado, end="")

def limpiar_pantalla():
    # Limpiar pantalla en Windows
    if os.name == "nt":
        os.system("cls")
    # Limpiar pantalla en Unix/Linux/MacOS
    else:
        os.system("clear")

class Player:
    def __init__(self, name=None, damage=None, health=None):
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self):
        return self.damage


class Enemy:
    def __init__(self, name=None, damage=None, health=None, description=None):
        self.name = name
        self.damage = damage
        self.health = health
        self.description = description

    def attack(self):
        return random.randint(int(self.damage * 0.5), int(self.damage * 1.5))


class Game:
    def __init__(self):
        self.player = None
        self.current_enemy = None
        self.enemies = []
        self.isGameSaved = False
        self.difficulty = None

    def newGame(self):
        self.loadEnemies()
        self.player = Player(name=None, damage=1000, health=100000)
        self.isGameSaved = False
        self.difficulty = None
        self.deleteSaveGame()

        if self.enemies:
            self.current_enemy = random.choice(self.enemies)
            self.enemies.remove(self.current_enemy)

    def readSaveGame(self):
        with open('savegame.json', 'r') as file:
            save_data = json.load(file)
        return save_data
    def loadEnemiesFromXML(self):
        enemies = []
        tree = ET.parse("enemies.xml")
        root = tree.getroot()
        for enemy in root.iter("enemy"):
            name = enemy.find("name").text
            damage = int(enemy.find("damage").text)
            health = int(enemy.find("health").text)
            enemies.append(Enemy(name, damage, health))
        return enemies
    def loadGame(self, player_name):
        save_data = self.readSaveGame()
        self.player = Player(
            name=player_name,
            health=save_data["playerStats"]["health"],
            damage=save_data["playerStats"]["damage"]
        )
        self.current_enemy = Enemy(
            name=save_data["currentEnemy"],
            health=save_data["enemyStats"]["health"],
            damage=save_data["enemyStats"]["damage"]
        )
        self.enemies = self.loadEnemiesFromXML()  # Cargar los datos de los enemigos desde enemies.xml

    def loadEnemies(self):
        try:
            tree = ET.parse("enemies.xml")
            root = tree.getroot()

            for enemy in root.findall("enemy"):
                name = enemy.find("name").text
                damage = int(enemy.find("damage").text)
                health = int(enemy.find("health").text)
                description = enemy.find("description").text

                self.enemies.append(Enemy(name=name, damage=damage, health=health, description=description))
        except FileNotFoundError:
            print("No se encontró el archivo enemies.xml.")

    def saveGame(self):
        save_data = {
            "currentEnemy": self.current_enemy.name if self.current_enemy else None,
            "difficulty": self.difficulty,
            "enemyStats": {
                "damage": self.current_enemy.damage if self.current_enemy else None,
                "health": self.current_enemy.health if self.current_enemy else None,
            },
            "playerStats": {
                "name": self.player.name if self.player else None,
                "damage": self.player.damage if self.player else None,
                "health": self.player.health if self.player else None,
            },
            "remainingEnemies": [enemy.name for enemy in self.enemies],
        }

        with open("savegame.json", "w") as file:
            json.dump(save_data, file)
    def deleteSaveGame(self):
        try:
            os.remove("savegame.json")
        except FileNotFoundError:
            pass

    def deleteEnemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def attackEnemy(self, damage):
        if self.current_enemy:
            self.current_enemy.health -= damage

            if self.current_enemy.health <= 0:
                self.deleteEnemy(self.current_enemy)

                if self.enemies:
                    self.current_enemy = random.choice(self.enemies)
                    self.enemies.remove(self.current_enemy)
                else:
                    self.current_enemy = None
                    print("\033[33m██   ██  █████  ███████      ██████   █████  ███    ██  █████  ██████   ██████  ██ ")
                    print("\033[32m██   ██ ██   ██ ██          ██       ██   ██ ████   ██ ██   ██ ██   ██ ██    ██ ██ ")
                    print("\033[36m███████ ███████ ███████     ██   ███ ███████ ██ ██  ██ ███████ ██   ██ ██    ██ ██ ")
                    print("\033[34m██   ██ ██   ██      ██     ██    ██ ██   ██ ██  ██ ██ ██   ██ ██   ██ ██    ██    ")
                    print("\033[35m██   ██ ██   ██ ███████      ██████  ██   ██ ██   ████ ██   ██ ██████   ██████  ██ ")
                    self.deleteSaveGame()
                    sys.exit(0)

    def playerTurn(self):
        print("\n¡Es tu turno, jugador {}!".format(self.player.name))
        print("1. Atacar")
        print("2. Guardar partida y salir")

        choice = input("Elige una opción: ")
        limpiar_pantalla()
        if choice == '1':
            damage = self.player.attack()
            self.attackEnemy(damage)
            print("Atacaste al enemigo {} con {} de daño.".format(self.current_enemy.name, damage))
        elif choice == '2':
            self.saveGame()
            print("Partida guardada. ¡Hasta luego!")
            sys.exit(0)
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


    def enemyTurn(self):
        if self.current_enemy:
            print("Turno del enemigo {}.".format(self.current_enemy.name))
            damage = self.current_enemy.attack()
            self.player.health -= damage

            print("El enemigo {} te atacó con {} de daño.".format(self.current_enemy.name, damage))

    def gameLoop(self):
        limpiar_pantalla()
        while self.player.health > 0 and (self.current_enemy or self.enemies):
            self.playerTurn()
            self.enemyTurn()

            if self.player:
                print("\033[35mJugador: {} \033[0m| \033[32mVida: {} \033[0m| \033[31mDaño: {}\033[0m".format(self.player.name, self.player.health, self.player.damage))
            if self.current_enemy:
                print("\033[31mEnemigo: {} \033[0m| \033[35mVida: {} \033[0m| \033[31mDaño: {}\033[0m".format(self.current_enemy.name, self.current_enemy.health, self.current_enemy.damage))
            self.saveGame()
        if self.player.health <= 0:
            print("Has perdido. ¡Game Over!")
        elif not self.enemies and not self.current_enemy:
            print("¡Has derrotado a todos los enemigos! ¡Victoria!")
        else:
            print("El juego ha terminado.")

        self.deleteSaveGame()


    @staticmethod
    def startGame():
        game = Game()
        
        print("¡Bienvenido al juego!")

        print("1. Nueva partida")
        if os.path.exists("./savegame.json"):
            save_data = game.readSaveGame()
            last_game_username=save_data["playerStats"]["name"]
            savegame_exists = True
            print("2. Cargar partida [{}]".format(last_game_username))
        else:
            savegame_exists = False
        
        choice = input("Elige una opción: ")

        if choice == '1':
            game.newGame()
            player_name = input("Ingresa el nombre del jugador: ")
            game.player.name = player_name
        elif choice == '2' and savegame_exists:
            game.loadGame(last_game_username)
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

        if game.player:
            game.gameLoop()

if __name__ == "__main__":
    Game.startGame()