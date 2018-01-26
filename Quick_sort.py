#Quick_sort
#Gerardo Ezequiel Magdaleno Hernandez
#@cherry2157

alist = [54,26,93,17,77,31,44,55,20]

def quickSortLauncher(alist, izq, der):
    pivote = alist[izq] #tomamos el primer elemento como pivote
    i = izq             #i realiza la busqueda de izquierda a derecha
    j = der             #j realiza la busqueda de derecha a izquierda
    aux = 0
    while(i<j):         #mientras no de crucen las busquedas
        while(alist[i]<= pivote and i<j): #busca elemento mayor que pivote
            i = i + 1
        while(alist[j]> pivote):          #busca elemento menor que pivote
            j = j - 1
        if(i<j):                          #si no se han cruzado
            aux =alist[i]                 #los intercambia
            alist[i] = alist[j]
            alist[j] = aux
    alist[izq] = alist[j]       #se coloca el pivote en su lugar de forma que tendremos
    alist[j] = pivote           #los menores a su izquierda y los mayores a su derecha
    if(izq<(j-1)):
        quickSortLauncher(alist,izq,(j-1)) #ordenamos subarray izquierdo
    if((j+1)<der):
        quickSortLauncher(alist,(j+1),der) #ordenamos subarray derecho

def quickSort(alist):#se podria llamar a la funcion directamente pero por convencion se llama asi
    quickSortLauncher(alist,0,len(alist)-1)

print("lista desordenada")
print alist

quickSort(alist) #se llama un metodo auxiliar

print("lista ordenada")
print alist
