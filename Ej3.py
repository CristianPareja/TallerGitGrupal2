# ### Ejercicio 3: Promedio de un arreglo
# Descripción: Crea una función que reciba un arreglo de números enteros y retorne el promedio de los elementos.  
# Debe tener la función para crear la matriz e imprimirlo.  
# No se pueden usar funciones propias de listas

def arreglo():
    try:
        numeros = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
        arreglo =[0]*numeros
        print(arreglo)
        for i in range (len(arreglo)):
            arreglo[i] = int(input("Ingrese el valor que desee: "))
        return arreglo
    except ValueError:
         print("EL caracter que ha ingresado no es un número entero")

def promedio(arregloA):
    try: 
        promedio = 0
        for i in (arregloA):
                promedio += i
        promedio = promedio / (len(arregloA))
        return promedio
    except Exception as e :
         print(f"Error en proceso previo a crear el promedio, error especifciiado: {e}")

arregloA = None
prom = None

arregloA = arreglo()

if arregloA == None:
    print(" ")
else:
    print(f"El arreglo que creaste es: \n {arregloA} ")
prom = promedio(arregloA)
if prom == None:
     print(" ")
else:
    print(f"El promdeio de tu arreglo es: \n {prom}")