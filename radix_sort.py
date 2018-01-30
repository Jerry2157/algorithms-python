#Radix_sort
#Gerardo Ezequiel Magdaleno Hernandez
#@cherry2157

def radix_sort(alist):
    len_list = len(alist)
    modulus = 10
    div = 1
    while True: #repite infinitamente para numero k de queue
        new_list = [[], [], [], [], [], [], [], [], [], []] #diez slots de 0-9
        for value in alist: #primero divide en unidades, despues en centenas y
                            #asi prograsivamente
            least_digit = value % modulus #residuo y dependiendo del residuo es a un slot
            least_digit /= div #el valor del digito menos significativo
            new_list[least_digit].append(value)
        modulus = modulus * 10 #para la siguiente cantidad de digito mas significativo
        div = div * 10          #para la siguiente cantidad de digito mas significativo
        if len(new_list[0]) == len_list: #como en algun momento todos los numeros son residuos
                                        #del digito significativo, estos se guardaran en la casilla 0
                                        # aqui se verifica si todos los numeros estan en esta casilla
                                        #y si si estan se termina la iteracion y regresa esta casilla
            return new_list[0]
        alist = [] #se vacia alist
        for x in new_list: #y se agregan los numero ordenados dependiendo del digito significativo
            for y in x:
                alist.append(y)
alist = [54,26,93,17,77,31,44,55,20,52]
print("lista desordenada")
print alist
print("lista ordenada")
print radix_sort(alist)
