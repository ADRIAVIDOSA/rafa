import xmltodict

title = "Editor de enemigos"
print(title)
print("-"*len(title))
enemies = []

def obten_datos ():
	name = input("Nombre: ")
	strength = int(input("Fuerza: "))
	health = int(input("Salud: "))
	description = input("Descripcion: ")
	return {
		"name": name,
 		"damage": strength,
		"health": health,
		"description": description
	}
		
def escribe_datos (export):
	enemy_xml = xmltodict.unparse(export, pretty=True)
	print(enemy_xml)
	f = open("enemy_xml", "w")
	f.write(enemy_xml)

	f.close()		

salir = False

while not salir:
	option = input("¿Quieres añadir un enemigo? [y/N]")
	if option.lower() != "y":
		salir = True
		continue

	enemy = obten_datos()

	enemies.append(enemy)

enemies_export = {
	"enemies": {
		"enemy": enemies
	}
}

escribe_datos(enemies_export)

