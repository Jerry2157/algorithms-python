#Schoning K-SAT solver
#Gerardo Ezequiel Magdaleno Hernandez
#@cherry2157

#CNF PROVIDED BY DR. VENEGAS ANDRACA

from random import randint
import random
import sys

# direciones ejemplo de CNF's
# direccionSchoning = '04. Instance_3SAT_example.txt'
# direccionSchoning = 'CNFEXAMPLETHREE.txt'
# direccionSchoning = 'CNFEXAMPLE50.txt'
# direccionSchoning = 'CNFEXAMPLE70.txt'
# direccionSchoning = 'CNFEXAMPLE80.txt'
direccionSchoning = 'CNFEXAMPLE90.txt'
numVariables = 0  # numero de variables, en este caso 20
numClauses = 0  # numero de clausulas
totalRepeat = 0

ArrayToVerify = []  # array que contiene las clausulas y las variables, es un array de arrays
ArrayVariables = []  # array que contiene los valores booleanos que comparar
sys.setrecursionlimit(100000)  # permite un mayor heap en la recursividad, NOTA: en mas de 50,000 crashea, depende del interprete cuanto soporta

# obtiene numero de Variables y Clausulas
def readCNF():
    ArrayVARCLAU = []
    global numVariables
    global numClauses
    with open(direccionSchoning) as fp:
        for line in fp:
            ArrayVARCLAU.append(line)

    ArrayB = ArrayVARCLAU[1].split(" ")
    numVariables = int(ArrayB[2])
    numClauses = int(ArrayB[3])
    for i in range(2, (numClauses + 2)):
        ArrayTemp = ArrayVARCLAU[i].split(" ")
        ArrayTempTwo = []
        ArrayTempTwo.append(int(ArrayTemp[0]))
        ArrayTempTwo.append(int(ArrayTemp[1]))
        ArrayTempTwo.append(int(ArrayTemp[2]))
        ArrayToVerify.append(ArrayTempTwo)

# regresa numeros aleatoros dependiendo de lo que se necesite
def randomNumberTwo(min, max):
    NumRand = randint(min, max)
    return NumRand

# mismo metodo que solo regresa 1 y 0
def randomNumber():
    NumRand = randint(0, 1)
    return NumRand

# llenta de 0 u 1 el ArrayVariables[]
def fillVariables():
    for i in range(0, numVariables):
        ArrayVariables.append(randomNumber())

# llama a Schoning solamente agregando el contador
def SchoningHelper(ArrayCNF, ArrayVar):
    global totalRepeat
    totalRepeat = 3 * numVariables
    return Schoning(ArrayCNF, ArrayVar,
                    0)  # ArrayCNF es el array que incluye las clausulas y variables a comparar, ArrayVar incluye el
    # string de booleanos a comparar

# metodo principal
def Schoning(ArrayCNF, ArrayVar, Repeater):
    global numClauses
    global totalRepeat
    #print len(ArrayCNF)
    print ''
    print "String a comparar: " + str(ArrayVar)
    a = 0
    clausuleCorrect = 0 # pregunta: la clausula esta correcta, es una bandera
    CountClausuleCorrect = 0 # cuantas clausulas estan satisfechas
    CountClausuleFail = 0 # cuantas clausulas no estan satisfechas
    operCounter = 0 # contador de operaciones
    iCounter = 0 # selector de clausula a verificar
    ClausulasModify = [] # guarda las clausulas a modificar
    modifyIT = 0 # boleano que de manera aleatoria se activa para proseguir a corregir n clausula
    selected = 0 # estado de que si una clausula se ha modificado
    clauseToConvert = 0 # que clausula se cambio
    varToConvert = 0 #
    for i in ArrayCNF: # lee cada clausula
        for j in i: # lee cada variable
            operCounter += 1 # agrega una operacion al contador (por si se requiere
            a = 0 # sirve para obtener el valor absoluto de la variable
            if clausuleCorrect == 1: # si ya encontro una variable satisfecha en su misma clausula, ya no verifica las siguientes de la misma clausula
                placebo = 0  # placebo 'if', is useless
            else: # proceso de verificar las variables
                if j < 0:  # NOT'S
                    a = j * (-1) # si la clausula dice que se debe verificar una variable con un NOT
                    if ArrayVar[(a - 1)] == 0: # si el valor de la variable es la misma a que la de la clausa, levanta la bandera indicando que la clausula es correcta
                        clausuleCorrect = 1 # bandera 'la clausula se satisface'
                elif j > 0:  # YES
                    a = j # si la clausula dice que se debe verificar una varibale con un YES
                    if ArrayVar[(a - 1)] == 1: # si el valor de la variable es la misma a que la de la clausa, levanta la bandera indicando que la clausula es correcta
                        clausuleCorrect = 1 # bandera 'la clausula se satisface'
        if clausuleCorrect == 1: # si la clausula esta satisfecha
            CountClausuleCorrect += 1 # suma una clausula correcta
        elif clausuleCorrect == 0: # clausula no esta satisfecha
            ClausulasModify.append(iCounter) # crea un indice con todas las clausulas no satisfechas
            ranDec = randomNumberTwo(0, 2) # seleciona un numero entero de 0 a 1
            ArrayTemp = ArrayCNF[iCounter] # crea un arreglo con todas las clausulas no satisfechas
            # ---inicia sleecion aleatoria de clausula a cambiar---
            if selected == 0: # si no se ha cambiado una clausula no satisfecha, decide aleatoriamente si se cambiara o no
                modifyIT = randomNumberTwo(0, 1) # 1 = se cambia, 0 = no se cambia
            if (modifyIT==1 | iCounter==numClauses) & selected==0: # si se va a modificar o no es la ultima clase  y no se ha cambiado, prosigue a cambiar la variable de la clausula
                selected = 1 # bandera de que se ha invertido una variable
                clauseToConvert = ClausulasModify[len(ClausulasModify)-1] # numero de clausula a modificar
                varToConvert = abs(ArrayTemp[ranDec]) # variable a modificar de la clausula a modificar
                if ArrayVar[abs(ArrayTemp[ranDec]) - 1] == 0: # si la variable es negativa
                    ArrayVar[abs(ArrayTemp[ranDec]) - 1] = 1
                else:
                    ArrayVar[abs(ArrayTemp[ranDec]) - 1] = 0 # si la variable es positiva
                CountClausuleFail += 1 # contador de clausulas no satisfechas
        clausuleCorrect = 0
        iCounter += 1

    print "clausulas satisfechas: " + str(CountClausuleCorrect)
    print "clausulas no satisfechas: " + str(CountClausuleFail)
    Repeater += 1 #verififcar de 3n veces
    if CountClausuleCorrect == numClauses: #se encontro solucion
        return "Se encontro solucion," + "se comprobo: " + str(Repeater) + " veces." + "\n" + "con el string: " + str(ArrayVar)
    else:
        print 'solo se modificara la clausula: ' + str(clauseToConvert)
        print "solo se modificara la variable: " + str(varToConvert)
        print "nuevo String a comparar: " + str(ArrayVar)
        if Repeater >= totalRepeat:
            return "no se encontro solucion," + "se comprobo: " + str(totalRepeat)
        else:
            return Schoning(ArrayCNF, ArrayVar, Repeater)
    return ArrayVar

readCNF()
fillVariables()
print "String Inicial: " + str(ArrayVariables) + " | numero de variables: " + str(len(ArrayVariables)) + " | numero de clausas: " + str(numClauses)
print SchoningHelper(ArrayToVerify, ArrayVariables)
