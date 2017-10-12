"""
Ordenamientos, Taller de Programación
Paola Alvarado y Ricardo Ugalde Gómez
Burbuja
Selección
Inserción
Shell
Radix
Heap-Heapsort
Shake
"""
import ast
  # Metodos
def ordenamientoBurbuja(lista,tam):
  for i in range(1,tam):
    for j in range(0,tam-i):
      if(lista[j] > lista[j+1]):
        k = lista[j+1]
        lista[j+1] = lista[j]
        lista[j] = k;
  return lista

def ordenShell(lista,tam):
  inc=1
  for inc in range(1,tam,inc*3+1):
    while inc>0:
      for i in range(inc,tam):
        j=i
        temp=lista[i]
        while j>=inc and lista[j-inc]>temp:
          lista[j]=lista[j-inc]
          j=j-inc
        lista[j]=temp
      inc=inc/2
  return lista

def insercionDirecta(lista,tam):
  for i in range(1,tam):
    v=lista[i]
    j=i-1
    while j >= 0 and lista[j] > v:
      lista[j+1] = lista[j]
      j=j-1
    lista[j+1]=v
  return lista

def selectionsort(lista,tam):
  for i in range(0,tam-1):
    min=i
    for j in range(i+1,tam):
      if lista[min] > lista[j]:
        min=j
    aux=lista[min]
    lista[min]=lista[i]
    lista[i]=aux
  return lista

#############################SHELL###################################

def mainloop():
  while True:
    print("Cuál ordenamiento desea utilizar?")
    print("1)Burbuja")
    print("2)Selección")
    print("3)Inserción")
    print("4)Shell")
    print("5)Radix")
    print("6)Heap-Heapsort")
    print("7)Shake")
    print("S) Salir del sistema")

    respuesta=input(": ")
    print("")
    
    if respuesta == "1":
        print("Usted seleccionó el método: Burbuja")
        print("Digite los numeros de la lista:")
        print("O digite \"s\" para salir.")
        lista = input()
        lista = lista.split(",")
        
        if "s" in lista or "S" in lista:
          pass

        else:
          lista = list(map(int,lista))
          tam= len(lista)
          result = ordenamientoBurbuja(lista,tam)
          print("La lista ordenada sería:")
          print(result)
          print("")

    if respuesta == "2":
        print("Usted seleccionó el método: SelectionSort")
        print("Digite los numeros de la lista:")
        print("O digite \"s\" para salir.")
        lista = input()
        lista = lista.split(",")
        
        if "s" in lista or "S" in lista:
          pass

        else:
          lista = list(map(int,lista))
          tam= len(lista)
          result = selectionsort(lista,tam)
          print("La lista ordenada sería:")
          print(result)
          print("")

    if respuesta == "3":
        print("Usted seleccionó el método: InsercionDirecta")
        print("Digite los numeros de la lista:")
        print("O digite \"s\" para salir.")
        lista = input()
        lista = lista.split(",")
        
        if "s" in lista or "S" in lista:
          pass

        else:
          lista = list(map(int,lista))
          tam= len(lista)
          result = insercionDirecta(lista,tam)
          print("La lista ordenada sería:")
          print(result)
          print("")

    if respuesta == "4":
        print("Usted seleccionó el método: OrdenShell")
        print("Digite los numeros de la lista:")
        print("O digite \"s\" para salir.")
        lista = input()
        lista = lista.split(",")
        
        if "s" in lista or "S" in lista:
          pass

        else:
          lista = list(map(int,lista))
          tam= len(lista)
          result = ordenShell(lista,tam)
          print("La lista ordenada sería:")
          print(result)
          print("")
      
          
          
    if respuesta == "s" or respuesta == "S":
      break






mainloop()

