def crear_arreglo():
    
    try:
        n = int(input("Número de elementos del arreglo: "))
        arreglo = [0] * n
        for i in range(n):
                arreglo[i] = int(input(f"Elemento {i + 1}: "))
        return arreglo     
    except ValueError:
        print("El valor ingresado debe ser un entero")
        

def invertir_arreglo(arreglo):
    try:
        n = len(arreglo)
        arreglo_inv = [0] * n  
        for i in range(n):
            arreglo_inv[i] = arreglo[n - 1 - i]
        return arreglo_inv
    except Exception as e:
             print("No se puede invertir el arreglo")

def imprimir_arreglo(arreglo):
    try:
        for elemento in arreglo:
            print(elemento, end=" ")
        print()
    except Exception as e:
            print("No se puede ingresar el arreglo")
arreglo=None

arreglo = crear_arreglo()
print("Arreglo ingresado:")
imprimir_arreglo(arreglo)
print("Arreglo invertido:")
arreglo_invertido = invertir_arreglo(arreglo)
imprimir_arreglo(arreglo_invertido)

