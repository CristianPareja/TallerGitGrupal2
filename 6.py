def crear_arreglo():
    try:
        n = int(input("Número de elementos del arreglo: "))
        arreglo = [0] * n
        for i in range(n):
                arreglo[i] = int(input(f"Elemento {i + 1}: "))
        return arreglo     
    except ValueError:
        print("El valor ingresado debe ser un entero")

def obtener_pares(arreglo):
    try:
        pares = []
        for numero in arreglo:
            if numero % 2 == 0: 
                pares.append(numero)  
        return pares
    except Exception as e:
             print("No se puede obtener el arreglo de pares")
    

def obtener_impares(arreglo):
    try:
        impares = []
        for numero in arreglo:
            if numero % 2 != 0:  
                impares.append(numero)  
        return impares
    except Exception as e:
             print("No se puede obtener el arreglo de impares")
    

arreglo=None

arreglo=crear_arreglo()
pares = obtener_pares(arreglo)
impares = obtener_impares(arreglo)

print("arreglo original:")
print(arreglo)
print("Números pares:", pares)
print("Números impares:", impares)
