#!/usr/bin/python3
#
# Script waarmee reiskosten opgesomd kunnen worden.
# Jun 2021 Matthew Buchanan Astley (matthewbuchanan@astley.nl) 

import os,sys
import glob

try:
   dir = sys.argv[1]
   dir1 = os.path.realpath(dir)
except IndexError:
   print('./pr_ov.py "mapje"')
   print('./pr_ov.py "mapje" -a  voor totale reiskosten per maand')
   print('"mapje" is de folder met alle gedownloade ov declaratie bestanden.')
   print('Declaratie bestanden moeten MmmYYYY als prefix hebben')

try:
   t3 = sys.argv[2]
   if t3 == '-a':
       t = 'a'
   else:
       t = ''
except IndexError:
   t = ''
   next
   

a = glob.glob(dir1 + '/*')

maanden = { 1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5 : 'Mei', 6 : 'Jun', 7 : 'Jul', 8 : 'Aug', 9 : 'Sep', 10 : 'Okt', 11 : 'Nov', 12 : 'Dec' }  

a1 = [] 

def ov_bestand(self):   
    a2 = open(self,'r')
    a3 = []     
    for i in a2:
        ii = i.split(';')
        if ii[0] != "Datum" and ii[6].strip('"') == 'Check-uit':
            a3.append(ii[5].strip('"').replace(',','.'))

    a4 = float()
    for i in a3:
        a4 += float(i)
 
    if t != 'a':
        if round(a4) > 80: 
            return(';'.join(['80',os.path.basename(self)]))  
        else:
            return(';'.join([str(round(a4)),os.path.basename(self)]))  
    else:
        return(';'.join([str(round(a4)),os.path.basename(self)]))  
    


a5 = []
a6 = {}

for i in a:
    ii = os.path.basename(i)
    iii = ii[3:7]
    a6[str(iii)] = 1 

a7 = []

print("Maand totaal;bestandsnaam")

for i in sorted(a6.keys()):
    for j in range(1,13):
        for c in a:
            ii = os.path.basename(c)
            iii = ii[0:3]
            iiii = ii[3:7]
            if iiii == i and maanden[j] == iii:
                t2 = dir1 + "/" + ii
                a7.append(ov_bestand(t2))

a8 = int() 
for i in a7:
    ii = i.split(';')
    print(i)
    a8 += int(ii[0])

print(';'.join(["Totaal",str(a8)]))

print("Aantal maanden",len(a7),"* 80;",len(a7) * 80 )
    
