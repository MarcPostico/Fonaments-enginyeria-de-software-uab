###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tecnic = input("nom del tècnic: ")
nom_xarxa = input("nom de l xarxa: ")
print("El tècnic", nom_tecnic, "està instal·lant la xarxa ", nom_xarxa)
# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud = float(input("Longitud de L'enllaç (km) : "))
velocitat = float(input("Velocitat de trasmissio (Gbps) :"))
segons = 8/velocitat
print("Temps necessari per transsmetre 1 GB de dades: ", segons, "segons")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores = float(input("Nombre d'hores de feina: "))
preu_hora = float(input("Preu per hora: "))
preu_material = float(input("Preu del material: "))
cost_total = hores * preu_hora + preu_material
print("El cost total de la instal·lació és: ", cost_total)
