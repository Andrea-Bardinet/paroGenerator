#!/bin/python
# -*- coding: UTF-8 -*-

import csv
import os
import sys

os.system("clear")

mot = sys.argv[1]
phone = ""
pMin = (int)(sys.argv[2])
pMax = (int)(sys.argv[3])


dico = open("python/dico")
read_tsv = csv.reader(dico, delimiter="\t")



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

res = ""




for precision in xrange(pMax,pMin,-1):
	dico.seek(0, 0)
	for row in read_tsv:	
		if phone[-precision:] == row[1][-precision:]:
			print row[0]

	
print res
dico.close()