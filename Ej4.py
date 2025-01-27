# Ejercicio 4: Contar ocurrencias de un número en un arreglo
# Descripción: Crea una función que reciba un arreglo y un número, y retorne cuántas veces aparece ese número en el arreglo.
# Debe tener la función para crear el arreglo e imprimirlo.
# No se pueden usar funciones propias de listas

def crearrreglo():
    try:
        numeros = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
        arreglo =[0]*numeros
        print(arreglo)
        for i in range (len(arreglo)):
            arreglo[i] = int(input("Ingrese los valores con los que desee llenar: "))
        print(arreglo)
        return arreglo
    except ValueError:
         print("El caracter que ha ingresado no es un número entero")

def fucnioncontador(arreglo):
    try:
        if arreglo != None:
            buscar = int(input("Ingresa el numero que deseas contar: "))
            contador = 0
            for i in arreglo:
                if i == buscar:
                    contador +=1
            if contador > 0:
                print(f"El numero que ingresaste aparerce {contador} veces en el arreglo.")
            elif contador == 0:
                print("El numero que ingrsaste no esta en el arreglo. ")
            return contador
    except Exception as e:
        print(f"Existe un error en el valor que deseas buscar, {e}")

arreglo = None
contador = None
arreglo = crearrreglo()
contador = fucnioncontador(arreglo)

# print(arreglo)

# if contador > 0:
#     print(f"El numero que ingresaste aparece {contador} veces dentro del arreglo.")
# else:
#     print("El número que ingresaste no aparece en el arreglo.")