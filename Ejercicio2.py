def LeerNumero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Ingrese un número válido, intente de nuevo.")
        except Exception as e:
            print(f"Ha ocurrido un error en el proceso de lectura del número: {e}")

def IniciarMatriz(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def CrearMatriz(nombre_matriz):
    try:
        filas = LeerNumero(f"Ingrese el número de filas de la matriz {nombre_matriz}: ")
        columnas = LeerNumero(f"Ingrese el número de columnas de la matriz {nombre_matriz}: ")
        matriz = IniciarMatriz(filas, columnas)
        print(f"Ingrese los elementos de la matriz {nombre_matriz}:")
        for i in range(filas):
            for j in range(columnas):
                matriz[i][j] = LeerNumero(f"Elemento {nombre_matriz}({i},{j}): ")
        return matriz
    except Exception as e:
        print(f"Ha ocurrido un error al crear la matriz {nombre_matriz}: {e}")

def imprimir_matriz(matriz, nombre_matriz):
    print(f"\nMatriz {nombre_matriz}:")
    for fila in matriz:
        print(fila)

def Mayor(matriz):
        mayor = matriz[0][0]
        for fila in matriz:
            for elemento in fila:
                if elemento > mayor:
                    mayor = elemento
        print(f"El numero mayor de la matriz es: {mayor}")
        return mayor

def Menor(matriz):
        
        menor = matriz[0][0]
        for fila in matriz:
            for elemento in fila:
                if elemento < menor:
                        menor = elemento
        print(f"El numero menor de la matriz es: {menor}")
        return menor

def menu():
    matriz = None
    
    while True:
        print("\nMenú de opciones:")
        print("1. Crear matriz")
        print("2. Imprimir matriz A")
        print("3. Numero Mayor")
        print("4. Numero Menor")
        print("5. Salir")

        opcion = LeerNumero("Seleccione una opción: ")

        if opcion == 1:
            matriz = CrearMatriz("A")
        elif opcion == 2:
            imprimir_matriz(matriz, "A")
        elif opcion == 3:
            if matriz:
                Mayor(matriz)
            else:
                print("La matriz A no ha sido creada.")
        elif opcion == 4:
            if matriz:
                Menor(matriz)
            else:
                print("La matriz A no ha sido creada.")
        elif opcion == 5:
            print("Salir del programa")
            break
        else:
                print("Opcion invalida.")


menu()



