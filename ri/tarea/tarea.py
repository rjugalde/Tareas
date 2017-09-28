import csv
import matplotlib.pyplot as plot
##with open("ArchivosEntrada/Ecuaciones.txt") as f:
##    lines = f.read().splitlines()

def listFromFile(path):
    with open(path) as f:
        lines = []
        for line in f:
             # to deal with blank 
            if line:            # lines (ie skip them)
                num = int(line)
                
                lines.append(num)
    return lines





def Main():
    path = "ArchivosEntrada/Ecuaciones.txt"
    nums = listFromFile(path)

    primerFuncion = nums[:,3]
    
    
Main()




