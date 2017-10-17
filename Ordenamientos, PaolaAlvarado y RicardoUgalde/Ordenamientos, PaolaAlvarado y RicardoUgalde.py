"""
Ordenamientos, Taller de Programación
Paola Alvarado y Ricardo Ugalde Gómez
#Burbuja
#Selección
#Inserción
#Shell
#Radix
#Heap-Heapsort
Shake
"""
import ast
  # Metodos
#burbuja
def ordenamientoBurbuja(lista,tam):
  for i in range(1,tam):
    for j in range(0,tam-i):
      if(lista[j] > lista[j+1]):
        k = lista[j+1]
        lista[j+1] = lista[j]
        lista[j] = k;
  return lista
#shell
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
      inc=inc//2
  return lista
  print (lista)
  
#insercion
def insercionDirecta(lista,tam):
  for i in range(1,tam):
    v=lista[i]
    j=i-1
    while j >= 0 and lista[j] > v:
      lista[j+1] = lista[j]
      j=j-1
    lista[j+1]=v
  return lista
#selection
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
#radix
def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
    # split aList between lists
    for  i in aList:
      tmp = i // placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
    # move to next digit
    placement *= RADIX
  return aList

#Heap sort
def swap(a, i, j):
  a[i], a[j] = a[j], a[i]  
def is_heap(a):
  n = 0
  m = 0
  while True:
    for i in [0, 1]:
      m += 1
      if m >= len(a):
        return True
      if a[m] > a[n]:
        return False
    n += 1   
def sift_down(a, n, max):
  while True:
    biggest = n
    c1 = 2*n + 1
    c2 = c1 + 1
    for c in [c1, c2]:
      if c < max and a[c] > a[biggest]:
        biggest = c
    if biggest == n:
      return
    swap(a, n, biggest)
    n = biggest
def heapify(a):
  i = len(a) // 2 - 1
  max = len(a)
  while i >= 0:
    sift_down(a, i, max)
    i -= 1
def heapsort(a):
  heapify(a)
  j = len(a) - 1
  while j > 0:
    swap(a, 0, j)
    sift_down(a, 0, j)
    j -= 1
  return a
#Shake
def shakerSort (arr,n):
  left=0
  right=n-1
  k=n
  while True:
    for j in range (right,left,-1):  #de derecha a izquierda
      if (arr[j]<arr[j-1]):
        temp=arr[j]
        arr[j]=arr[j-1]
        arr[j-1]=temp
        k=j
    left=k

    for j in range (left,right):  #de izquierda a derecha
      if (arr[j]>arr[j+1]):
        temp= arr[j]
        arr[j]=arr[j+1]
        arr[j+1]=temp
        k=j
    right=k
    if (left>=right):
      break
  return arr

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
          
    if respuesta == "5":
        print("Usted seleccionó el método: Radix")
        print("Digite los numeros de la lista:")
        print("O digite \"s\" para salir.")
        lista = input()
        lista = lista.split(",")
        
        if "s" in lista or "S" in lista:
          pass

        else:
          lista = list(map(int,lista))
          #tam= len(lista)
          result = radixsort(lista)
          print("La lista ordenada sería:")
          print(result)
          print("")
        6
    if respuesta == "6":
        print("Usted seleccionó el método: HeapSort")
        print("Digite los numeros de la lista:")
        print("O digite \"s\" para salir.")
        lista = input()
        lista = lista.split(",")
        
        if "s" in lista or "S" in lista:
          pass

        else:
          lista = list(map(int,lista))
          #tam= len(lista)
          result = heapsort(lista)
          print("La lista ordenada sería:")
          print(result)
          print("")
          
    if respuesta == "7":
        print("Usted seleccionó el método: Shaker")
        print("Digite los numeros de la lista:")
        print("O digite \"s\" para salir.")
        lista = input()
        lista = lista.split(",")
        
        if "s" in lista or "S" in lista:
          pass

        else:
          lista = list(map(int,lista))
          tam= len(lista)
          result = shakerSort(lista,tam)
          print("La lista ordenada sería:")
          print(result)
          print("")
      
          
          
    if respuesta == "s" or respuesta == "S":
      break






mainloop()

