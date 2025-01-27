def LeerNumero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Ingrese un número válido, intente de nuevo.")
        except Exception as e:
            print(f"Ha ocurrido un error en el proceso de lectura del número: {e}")


def arreglo():
    
    try:
        numero = LeerNumero("Ingrese la cantidad de elementos del arreglo: ")
        if numero <= 0 or int(numero) != numero:
            print("El número debe ser mayor a 0.")
            return
        numero = int(numero)
    except ValueError:
            print("Debe ingresar un número entero válido.")
            return
                
        
        
    arreglo = []
    append = 0   
    suma = 0
    
    print(f"Ingrese {numero} elementos (uno por línea):")

        
        
    for i in range(numero):
        while True:
            try:
                elemento = LeerNumero(f"Elemento {i + 1}: ")

                if append == 0:
                    arreglo = [elemento]
                else:
                    arreglo1 = [0] * (append + 1)
                    for j in range(append):
                        arreglo1[j] = arreglo[j]

                    arreglo1[append] = elemento
                            
                    arreglo = arreglo1

                append += 1
                suma += elemento
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

                
                    
    print(arreglo)
    print(f"La suma del arreglo es : {suma}")

arreglo()

