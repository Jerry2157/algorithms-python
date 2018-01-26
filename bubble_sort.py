#bubble sort
#Gerardo Ezequiel Magdaleno Hernandez
#@cherry2157
alist = [54,26,93,17,77,31,44,55,20]
i = 0
j = 0
temp = alist[i]
alist[i] = alist[j]
alist[j] = temp
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): #inicia en el ultimo elemento de la lista, se detiene en 0 y cada vez resta 1
        print(passnum)
        for i in range(passnum):
            print(alist[i] , alist[i+1])#muestra que numeros va a comparar
            if alist[i]>alist[i+1]: #si detecta que el primero es mayor que el segundo dato evaluado procede
                temp = alist[i] #se almacena el primer dato en temp
                alist[i] = alist[i+1]#se guarda el segundo dato en el primero espacio [0]
                alist[i+1] = temp #se guarda el primer dato en el segundo espacio [1]
print("lista desordenada")
print(alist)
bubbleSort(alist)
print("lista ordenada")
print(alist)
