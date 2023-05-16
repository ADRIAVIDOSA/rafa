import json
import random
import xml.etree.ElementTree as ET
import xml
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
        self.savemethod = None

    def newGame(self):
        self.loadEnemies()
        self.player = Player(name=None, damage=1000, health=30000)
        self.isGameSaved = False
        self.savemethod = "XML" if input("Elige formato de guardado:\n1. XML\n2. JSON\n[1 | 2]: ") == "1" else "JSON"
        self.deleteSaveGame(self.savemethod)
        if self.enemies:
            self.current_enemy = random.choice(self.enemies)
            self.enemies.remove(self.current_enemy)

    def readSaveGame(self, method="JSON"):
        if method == "JSON":
            with open('savegame.json', 'r') as file:
                save_data = json.load(file)
        else:
            tree = ET.parse('savegame.xml')
            root = tree.getroot()

            save_data = {
                "currentEnemy": root.findtext("current_enemy"),
                "enemyStats": {
                    "damage": int(root.findtext("enemy_stats/damage")),
                    "health": int(root.findtext("enemy_stats/health")),
                },
                "playerStats": {
                    "name": root.findtext("player_stats/name"),
                    "damage": int(root.findtext("player_stats/damage")),
                    "health": int(root.findtext("player_stats/health")),
                },
                "remainingEnemies": [enemy.text for enemy in root.findall("remaining_enemies/enemy")],
            }
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



    def loadGame(self, player_name, method="JSON"):
        
        self.savemethod = method

        if method == "JSON":
            save_data = self.readSaveGame("JSON")
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
        else:
            tree = ET.parse('savegame.xml')
            root = tree.getroot()

            save_data = {
                "currentEnemy": root.findtext("current_enemy"),
                "enemyStats": {
                    "damage": int(root.findtext("enemy_stats/damage")),
                    "health": int(root.findtext("enemy_stats/health")),
                },
                "playerStats": {
                    "name": root.findtext("player_stats/name"),
                    "damage": int(root.findtext("player_stats/damage")),
                    "health": int(root.findtext("player_stats/health")),
                },
                "remainingEnemies": [enemy.text for enemy in root.findall("remaining_enemies/enemy")],
            }

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

    def saveGame(self, method="JSON"): # Can be JSON or XML
        save_data = {
            "currentEnemy": self.current_enemy.name if self.current_enemy else None,
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
        if method == "JSON":
            with open("savegame.json", "w") as file:
                json.dump(save_data, file)
        else:
            root = ET.Element("save_data")

            current_enemy = ET.SubElement(root, "current_enemy")
            current_enemy.text = save_data["currentEnemy"]

            enemy_stats = ET.SubElement(root, "enemy_stats")
            enemy_damage = ET.SubElement(enemy_stats, "damage")
            enemy_damage.text = str(save_data["enemyStats"]["damage"])
            enemy_health = ET.SubElement(enemy_stats, "health")
            enemy_health.text = str(save_data["enemyStats"]["health"])

            player_stats = ET.SubElement(root, "player_stats")
            player_name = ET.SubElement(player_stats, "name")
            player_name.text = save_data["playerStats"]["name"]
            player_damage = ET.SubElement(player_stats, "damage")
            player_damage.text = str(save_data["playerStats"]["damage"])
            player_health = ET.SubElement(player_stats, "health")
            player_health.text = str(save_data["playerStats"]["health"])

            remaining_enemies = ET.SubElement(root, "remaining_enemies")
            for enemy_name in save_data["remainingEnemies"]:
                enemy = ET.SubElement(remaining_enemies, "enemy")
                enemy.text = enemy_name

            tree = ET.ElementTree(root)
            tree.write("savegame.xml", encoding="utf-8", xml_declaration=True)
    
    
    def deleteSaveGame(self, method="JSON"):
        if method == "JSON":
            try:
                os.remove("savegame.json")
            except FileNotFoundError:
                pass
        else:
            try:
                os.remove("savegame.xml")
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
                    self.deleteSaveGame(self.savemethod)
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
            self.saveGame(self.savemethod)
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
            self.saveGame(self.savemethod)
        if self.player.health <= 0:
            print("Has perdido. ¡Game Over!")
        elif not self.enemies and not self.current_enemy:
            print("¡Has derrotado a todos los enemigos! ¡Victoria!")
        else:
            print("El juego ha terminado.")

        self.deleteSaveGame(self.savemethod)


    @staticmethod
    def startGame():
        game = Game()
        
        print("¡Bienvenido al juego!")
        print("1. Nueva partida")
        if os.path.exists("./savegame.json"):
            save_data = game.readSaveGame("JSON")
            last_game_username=save_data["playerStats"]["name"]
            savegame_exists = True
            print("2. Cargar partida (JSON) [{}]".format(last_game_username))
        if os.path.exists("./savegame.xml"):
            xml_save_data = game.readSaveGame("XML")
            xml_save_data_exists = True
            last_xml_game_username=xml_save_data["playerStats"]["name"]
            print("3. Cargar partida (XML) [{}]".format(last_xml_game_username))
        else:
            savegame_exists = False
        
        choice = input("Elige una opción: ")

        if choice == '1':
            game.newGame()
            player_name = input("Ingresa el nombre del jugador: ")
            game.player.name = player_name
        
        elif choice == '2' and savegame_exists:
            save_method = "JSON"
            game.loadGame(last_game_username)

        elif choice == '3' and xml_save_data_exists:
            save_method = "XML"
            game.loadGame(last_xml_game_username, "XML")
        
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

        if game.player:
            game.gameLoop()

if __name__ == "__main__":
    Game.startGame()