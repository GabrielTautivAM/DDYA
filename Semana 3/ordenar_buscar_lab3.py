def merge_sort(lista, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(lista, p, q)
        merge_sort(lista, q + 1, r)
        merge(lista, p, q, r)

def merge(lista, p, q, r):
    izq = lista[p : q + 1]
    der = lista[q + 1 : r + 1]
    
    i = 0
    j = 0
    k = p

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            lista[k] = izq[i]
            i = i + 1
        else:
            lista[k] = der[j]
            j = j + 1
        k = k + 1

    while i < len(izq):
        lista[k] = izq[i]
        i = i + 1
        k = k + 1

    while j < len(der):
        lista[k] = der[j]
        j = j + 1
        k = k + 1


def busqueda_binaria(arreglo, dato):
    izq = 0
    der = len(arreglo) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if arreglo[medio] == dato:
            return True
        elif arreglo[medio] < dato:
            izq = medio + 1
        else:
            der = medio - 1
    return False

def main():
    productos = []
    
    print("REGISTRO DE PRODUCTOS")
    cant = input("Ingrese la cantidad de productos a registrar: ")
    
    while not cant.isdigit() or int(cant) < 1:
        print("Error: Ingrese un numero valido mayor a 0.")
        cant = input("Ingrese la cantidad de productos a registrar: ")
        
    cant = int(cant)

    for i in range(cant):
        repetido = True
        
        while repetido:
            cod = input("Codigo del producto #" + str(i + 1) + ": ")
            
            if not cod.isdigit():
                print("Error: Solo se permiten digitos.")
            else:
                num = int(cod)

                if num in productos:
                    print("El codigo", num, "ya fue ingresado, intente de nuevo.")
                else:
                    productos.append(num)
                    repetido = False

    print("\nCodigos ingresados:", productos)

    merge_sort(productos, 0, len(productos) - 1)
    print("Codigos ordenados:", productos)

    print("\n--- BUSQUEDA ---")
    band = True

    while band:
        buscado = input("Codigo que desea buscar")

        while not buscado.isdigit():
            print("Error,Ingrese solo numeros")
            buscado = input("Codigo que desea buscar: ")

        buscado = int(buscado)

        
        if busqueda_binaria(productos, buscado):
            print("El producto", buscado, "SI existe en el registro.")
        else:
            print("El producto", buscado, "NO fue encontrado.")

        print("desea buscar otro codigo?, escribir unicamente SI o NO")
        x = input()
        while x != "SI" and x!= "NO":
            print("repuesta invalida, intente nuevamente")
            x = input()

        if x == "NO":
            band = False

    print("Gracias por usar el programa")

main()