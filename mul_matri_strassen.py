#Multiplicacion de matrices por Strassen
#Gerardo Ezequiel Magdaleno Hernandez
#@cherry2157

#Matrices proporcionadas por el  DR. VENEGAS ANDRACA

#thanks to:
#https://software.intel.com/sites/default/files/m/c/d/5/3/d/24469-Strassen_akki.pdf
#https://web.archive.org/web/20100711123350/http://surj.stanford.edu/2004/pdfs/kakaradov.pdf
#https://www.youtube.com/watch?v=6cBSAkzzQzU
#https://es.wikipedia.org/wiki/Algoritmo_de_Strassen


#its well knowed that strassen is futhermore quickly but is expensive in terms of memory
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
direccionMatrizC = '09. MatrizResultadoStrassen.txt'
ArrayC = []

#suma total
MulTotal = 0
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
#print ArrayA
#print ArrayB
print("--- %s seconds. Steph: 1- Read files. ---" % (time.time() - start_time))
def convertMatrizAtoInt():
    row = 0
    col = 0
    for line in ArrayA:
        for lineTwo in line:
            ArrayA[row][col] = int(lineTwo)
            col += 1
        col = 0
        row +=1
    row = 0
def convertMatrizBtoInt():
    row = 0
    col = 0
    for line in ArrayB:
        for lineTwo in line:
            ArrayB[row][col] = int(lineTwo)
            col += 1
        col = 0
        row +=1
    row = 0
convertMatrizAtoInt()
convertMatrizBtoInt()
#print ArrayA
#print ArrayB

def createEmptyMatrix(x, y): # reconstruir matriz
    matrix = [[0 for row in range(x)] for col in range(y)]
    return matrix


def split(matrix): # dividir la matriz en cuatro
    a = matrix
    b = matrix
    c = matrix
    d = matrix
    while(len(a) > len(matrix)/2):
        a = a[:len(a)/2]
        b = b[:len(b)/2]
        c = c[len(c)/2:]
        d = d[len(d)/2:]
    while(len(a[0]) > len(matrix[0])/2):
        for i in range(len(a[0])/2):
            a[i] = a[i][:len(a[i])/2]
            b[i] = b[i][len(b[i])/2:]
            c[i] = c[i][:len(c[i])/2]
            d[i] = d[i][len(d[i])/2:]
    return a,b,c,d

def addMatrix(a, b): # add 2 matrices
    d = []
    for i in range(len(a)):
        c = []
        for j in range(len(a[0])):
            c.append(a[i][j] + b[i][j])
        d.append(c)
    return d

def subMatrix(a, b): # subtract 2 matrices
    assert len(a) == len(b), "Numero de filas no coincide!"
    assert len(a[0]) == len(b[0]), "Numero de columnas no coincide!"
    d = []
    for i in range(len(a)):
        c = []
        for j in range(len(a[0])):
            c.append(a[i][j] - b[i][j])
        d.append(c)
    return d

def strassen(a, b, n):
    global MulTotal
    if n == 1:#caso base: cuando solamente hay una matriz y ya no se puede dividir en dos por obviedad.
        d = [[0]]
        MulTotal += 1
        d[0][0] = a[0][0] * b[0][0]
        return d
    else: #evento recursivo, se divide en 4 sectores ambas matrices
        a11, a12, a21, a22 = split(a)
        b11, b12, b21, b22 = split(b)

        p1 = strassen(addMatrix(a11,a22), addMatrix(b11,b22), n/2)

    p2 = strassen(addMatrix(a21,a22), b11, n/2)
    p3 = strassen(a11, subMatrix(b12,b22), n/2)
    p4 = strassen(a22, subMatrix(b21,b11), n/2)
    p5 = strassen(addMatrix(a11,a12), b22, n/2)
    p6 = strassen(subMatrix(a21,a11), addMatrix(b11,b12), n/2)
    p7 = strassen(subMatrix(a12,a22), addMatrix(b21,b22), n/2)

    c11 = addMatrix(subMatrix(addMatrix(p1, p4), p5), p7)
    c12 = addMatrix(p3, p5)
    c21 = addMatrix(p2, p4)
    c22 = addMatrix(subMatrix(addMatrix(p1, p3), p2), p6)
    c = createEmptyMatrix(len(c11) * 2, len(c11) * 2)

    for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j]                   = c11[i][j]
                c[i][j+len(c11)]          = c12[i][j]
                c[i+len(c11)][j]          = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

    return c


ArrayC = strassen(ArrayA,ArrayB,len(ArrayA[0]))
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
print('total operaciones escalares: ' + str(MulTotal) + '.')
print 'finish'