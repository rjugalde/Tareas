#Ricardo Ugalde, Cramer, Taller

import csv
import matplotlib.pyplot as ploter
##with open("ArchivosEntrada/Ecuaciones.txt") as f:
##    lines = f.read().splitlines()

def listFromFile(path):  #meter archivos en listas
    with open(path) as f:
        lines = []
        for line in f:
             # to deal with blank 
            if line:            # lines (ie skip them)
                num = int(line)
                
                lines.append(num)
    return lines


def det(m):  #función determinante
    g = ((m[0][0])*(m[1][1]))-((m[1][0])*(m[0][1]))
    return g

#main loop

def Main():
    path = "ArchivosEntrada/Ecuaciones.txt"
    nums = listFromFile(path)

    primerFuncion = nums[0:3]
    segundaFuncion = nums [3:]
    #print(primerFuncion)
    #print(segundaFuncion)
    matg =[[primerFuncion[0],primerFuncion[1]],[segundaFuncion[0],segundaFuncion[1]]]
    matx =[[primerFuncion[2],primerFuncion[1]],[segundaFuncion[2],segundaFuncion[1]]]
    maty =[[primerFuncion[0],primerFuncion[2]],[segundaFuncion[0],segundaFuncion[2]]]
##    print (matg)
##    print (det(matg))
##    print (matx)
##    print (det(matx))
##    print (maty)
##    print (det(maty))
    #definir dets en variables
    j= det(matg)
    k= det(matx)
    l= det(maty)
    #pt4
    X = k / j
    Y = l / j
##    print(X)
##    print(Y)
    #x,y de primer funcion
    xs1 = 5
    ys1 = (primerFuncion[2]-primerFuncion[0]*xs1)/primerFuncion[1]
    y1 = primerFuncion[2]/primerFuncion[1]
    x1 = 0
    y2 = 0
    x2 = primerFuncion[2]/primerFuncion[0]
    ploter.plot([x2,x1,X,xs1],[y2,y1,Y,ys1])
    #x,y de segunda funcion
    y1 = segundaFuncion[2]/segundaFuncion[1]
    x1 = 0
    y2 = 0
    x2 = segundaFuncion[2]/segundaFuncion[0]
    #graficada segunda funcion
    ys2 = -1.3
    xs2 = (segundaFuncion[2]-segundaFuncion[1]*ys2)/segundaFuncion[0]
    ploter.plot([x2,x1,X,xs2],[y2,y1,Y,ys2])
    ploter.show()
    
    
Main()




