import xmltodict

print("Crea un enemigo")
print("|-------------|")

name = input("Nombre: ")
strength = int(input("Fuerza: "))
health = int(input("Salud: "))


enemy= {
	"enemy": {
 		"name": name,
		"damage": strength,
		"health": health,
 	}   
}
enemy_xml=xmltodict.unparse(enemy, pretty=True)
print(enemy_xml)
f = open("enemy_xml", "w")
f.write(enemy_xml)

f.close()		
