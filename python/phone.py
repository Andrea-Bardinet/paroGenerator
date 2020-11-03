#!/bin/python
# -*- coding: UTF-8 -*-

import csv
import os
import sys

os.system("clear")

mot = sys.argv[1]
phone = ""
pMax = (int)(sys.argv[2])
pMin = (int)(sys.argv[3])


dico = open("dico")
read_tsv = csv.reader(dico, delimiter="\t")



print "Recherche: "+mot



for mot in sys.argv[1].split():
	dico.seek(0, 0)
	trouve = False
	for row in read_tsv:
		if row[0] == mot:
			trouve = True
			phone = phone+row[1]
	if not trouve:
		print "["+mot+"] non trouvé  :'("
		exit(1)

if pMax > len(phone):
	pMax = len(phone)

if pMin > pMax:
	pMin = pMax -1


print "Précision: De "+str(pMax)+" à "+str(pMin)+"."
print "------------------------------"
for precision in xrange(pMax,pMin,-1):
	print "Précision: "+(str)(precision)
	print "------------------------------"
	dico.seek(0, 0)
	for row in read_tsv:	
		if phone[-precision:] == row[1][-precision:]:
			print row[0]
	print "------------------------------"
	

dico.close()