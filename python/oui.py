def taille(nombre):
	taille = 0
	while nombre != 0:
		nombre = nombre * 0.1
		nombre = (int)(nombre)
		taille = taille + 1
	return taille

def inverse(nombre):
	res = 0
	while nombre != 0:
		res = res * 10
		res = res + nombre%10
		nombre = nombre * 0.1
		nombre = (int)(nombre)
	return res

def reduire(nombre, nb):
	while taille(nombre) > nb:
		nombre = nombre * 0.1
		nombre = (int)(nombre)
	return nombre

import sys


mot = "bonjour"

for mot in sys.argv[1].split():
	print mot