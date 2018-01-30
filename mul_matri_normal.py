#multiplicacion de matrices normal
#Gerardo Ezequiel Magdaleno Hernandez
#@cherry2157

#Matrices proporcionadas por el Dr. Salvador Andraca

import time
start_time = time.time()
print ("Specs:")
print ("intel Core i7 2.2Ghz, turboBoost 3.4Ghz")
print ("SSD")
print ("Ram: 16GB")

#Matriz A
direccionMatrizA = '03. Matriz_A_128_2_7.txt'
ArrayTempA = []
ArrayA = []

#Matriz B
direccionMatrizB = '04. Matriz_B_128_2_7.txt'
ArrayTempB = []
ArrayB = []

#matriz resultante
direccionMatrizC = '09. MatrizResultado.txt'
ArrayC = []

#time function


#leer matrices
def readMatrizA():
    with open(direccionMatrizA) as fp:
        for line in fp:
            temp = line.split("\n")
            tempTwo = temp[0].split(",")
            ArrayA.append(tempTwo)
def readMatrizB():
    with open(direccionMatrizB) as fp:
        for line in fp:
            temp = line.split("\n")
            tempTwo = temp[0].split(",")
            ArrayB.append(tempTwo)
readMatrizA()
readMatrizB()
print("--- %s seconds. Steph: 1- Read files. ---" % (time.time() - start_time))
#print ArrayA
#print ArrayB

def multiplicar():
    selectorFila = 0
    selectorColumna = 0
    ArrayTemp = [] #aqui se guarda la multiplicacion de la matrizA,B por linea de MatrizA por columna de Matriz B

    count = len(ArrayB) #total de columnas en matrizB

    numTotal = 0
    numEscalar = 0
    #LOGICA: 1-ENTRA A REVISAR CADA FILA DE LA MATRIZ A,
    # DESPUES POR CADA DATO DE LA FILA DE LA MATRIZ A REVISA EL NUMERO DE COLUMNA DE LA MATRIZ B
    # REPITE POR NUMERO DE COLUMNAS DE LA MATRIZ B
    for Aline in ArrayA:     #entro a cada linea de la matrizA
        while (selectorColumna < count): #repite por cada columna de la matriz B
            for AlineTwo in Aline:  # entro a cada dato de la linea de la matrizA
                #print AlineTwo + ' ' + ArrayB[selectorFila][selectorColumna]
                #totalSum += 1
                numTotal = numTotal + int(AlineTwo) * int(ArrayB[selectorFila][selectorColumna])
                numEscalar += 1
                #print numTotal
                selectorFila += 1
            selectorFila = 0
            ArrayTemp.append(numTotal)
            numTotal = 0
            selectorColumna += 1
        ArrayC.append(ArrayTemp)
        ArrayTemp = []
        selectorFila = 0
        selectorColumna = 0
    print('total operaciones escalares: ' + str(numEscalar) + '.')
multiplicar()
print("--- %s seconds. Steph: 2- Multiply Matrix. ---" % (time.time() - start_time))

def results():
    for line in ArrayC:
        print line
#results()
#print("--- %s seconds. Steph: 3- write in console. ---" % (time.time() - start_time))

def writeInDisk():
    thefile = open(direccionMatrizC, 'w')
    for item in ArrayC:
        thefile.write("%s\n" % ','.join(map(str, item)))
writeInDisk()
print("--- %s seconds. Steph: 4- write in disk. ---" % (time.time() - start_time))
print 'finish'


