#Heap sort
#Gerardo Ezequiel Magdaleno Hernandez
#@cherry2157


def heapsort(alist):

    size = len(alist)
    for i in range(size/2-1, -1, -1):#crea un heap
        heapUtil(alist, i, size)

    for i in range(size-1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0] #recuperar el dato del primer nivel
        heapUtil(alist, 0, i)#recrear el heap excluyendo el primer termino, que es el dato del primer nivel

def heapUtil(alist, i, n):
    padre = alist[i] #se resguarda el numero del nivel que se va a comparar
    while 2 * i + 1 < n: #hace el recorrido desde el numero de
        hijo = 2 * i + 1 #aumenta en uno hijo y despues lo regresa a ustado original
        if hijo + 1 < n and alist[hijo] < alist[hijo + 1]: #se verifica que de entre los 3 el padre sea el mas grande
            hijo += 1
        if padre >= alist[hijo]: #si el padre es el mas grande se queda en su nivel
            break
        alist[i] = alist[hijo] #asigna al lugar del padre el dato mayor entre los hijos
        i = hijo               #regresa i al estado original
    alist[i] = padre #aqui se almacena

alist = [54,26,93,17,77,31,44,55,20,-52]
print("lista desordenada")
print alist
print("lista ordenada")
heapsort(alist)
print alist
