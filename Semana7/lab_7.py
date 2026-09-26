def pedir_nombre(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato == "":
            print("Error: debe poner un nombre")
        else:
            tiene_numero = False
            for caracter in dato:
                if caracter.isdigit():
                    tiene_numero = True
                    break
            if tiene_numero:
                print("Error: el nombre no puede tener numeros")
            else:
                return dato

def pedir_codigo(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato == "":
            print("Error: el codigo no puede quedar vacio")
        elif not dato.isdigit():
            print("Error: el codigo solo puede tener numeros")
        elif int(dato) <= 0:
            print("Error: el codigo debe ser un numero entero positivo")
        else:
            return int(dato)

def pedir_precio(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        else:
            print("Error: el precio debe ser un numero entero positivo")

def ver_cola(cola):
    if not cola:
        return "Vacia"
    return " -> ".join(cola)

def ver_pila(pila):
    if not pila:
        print("La pila esta vacia")
        return
    print("\nPila de clientes atendidos:")
    print("| " + str(pila[-1]) + " | <- Tope")
    for i in range(len(pila) - 2, -1, -1):
        print("| " + str(pila[i]) + " |")
    print("---------")

def mostrar_ultimo_atendido(pila):
    if not pila:
        print("Todavia no se ha atendido a ningun cliente")
    else:
        print("El ultimo cliente atendido fue: " + str(pila[-1]))

def guardar_producto(cod, nom, prec, prim, ult):
    nuevo = [cod, nom, prec, None, None]
    if prim is None:
        prim = nuevo
        ult = nuevo
    else:
        ult[4] = nuevo
        nuevo[3] = ult
        ult = nuevo
    return prim, ult

def texto_producto(producto):
    return str(producto[0]) + " - " + str(producto[1]) + " - $" + str(producto[2])

def ver_productos_adelante(prim):
    if prim is None:
        return "NULL"
    res = "NULL <- "
    aux = prim
    while aux is not None:
        res = res + texto_producto(aux)
        if aux[4] is not None:
            res = res + " <-> "
        aux = aux[4]
    res = res + " -> NULL"
    return res

def ver_productos_atras(ult):
    if ult is None:
        return "NULL"
    res = "NULL <- "
    aux = ult
    while aux is not None:
        res = res + texto_producto(aux)
        if aux[3] is not None:
            res = res + " <-> "
        aux = aux[3]
    res = res + " -> NULL"
    return res

def buscar_prod(cod, prim):
    aux = prim
    while aux is not None:
        if aux[0] == cod:
            return aux
        aux = aux[4]
    return None

def borrar_producto(cod, prim, ult):
    elem = buscar_prod(cod, prim)
    if elem is not None:
        nom_borrado = elem[1]
        ant = elem[3]
        sig = elem[4]
        if ant is not None:
            ant[4] = sig
        else:
            prim = sig
        if sig is not None:
            sig[3] = ant
        else:
            ult = ant
        return nom_borrado, prim, ult
    return None, prim, ult

def sistema():
    cola = []
    pila = []
    cabeza = None
    cola_lista = None

    n = 0
    valido = False
    while not valido:
        num = input("Cuantos clientes desea registrar? ").strip()
        if num.isdigit():
            n = int(num)
            if n > 0:
                valido = True
            else:
                print("Error: por favor ingrese un valor mayor a 0")
        else:
            print("Error: el numero debe ser un entero positivo")
            
    for i in range(1, n + 1):
        nom = pedir_nombre("Ingrese el nombre del cliente " + str(i) + ": ")
        cola.append(nom) 
        
    print("\nLa cola inicialmente es:")
    print(ver_cola(cola))
    
    opcion = ""
    while opcion != "0":
        print("\n\t-BIENVENIDO-")
        print("1. Agregar un nuevo cliente a la cola")
        print("2. Atender al siguiente cliente")
        print("3. Mostrar los clientes que siguen esperando")
        print("4. Mostrar el ultimo cliente atendido")
        print("5. Deshacer la ultima atencion")
        print("6. Agregar un producto al final de la lista")
        print("7. Mostrar productos de primero a ultimo")
        print("8. Mostrar productos de ultimo a primero")
        print("9. Buscar un producto usando su codigo")
        print("10. Eliminar un producto usando su codigo")
        print("0. Salir")
        
        opcion = input("Seleccione una opcion con el numero: ").strip()

        if opcion == "1":
            nom = pedir_nombre("Ingrese el nombre del nuevo cliente: ")
            cola.append(nom)
            print("Cliente agregado correctamente")
            print("La cola queda asi:")
            print(ver_cola(cola))

        elif opcion == "2":
            if cola:
                cli = cola.pop(0) 
                pila.append(cli)  
                print("Atendiendo a: " + str(cli))
                print("Clientes esperando: " + ver_cola(cola))
            else:
                print("No hay clientes en espera")

        elif opcion == "3":
            if not cola:
                print("No hay clientes esperando")
            else:
                print("Clientes en espera: " + ver_cola(cola))

        elif opcion == "4":
            mostrar_ultimo_atendido(pila)

        elif opcion == "5":
            if not pila:
                print("No hay atenciones para deshacer")
            else:
                cli_recup = pila.pop() 
                cola.insert(0, cli_recup) 
                
                print("\nDeshacer ultima atencion")
                print(cli_recup + " fue retirado de la pila de clientes atendidos")
                print("La pila queda asi:")
                ver_pila(pila)
                print(cli_recup + " regreso al inicio de la cola")
                print("La cola queda asi: " + ver_cola(cola))

        elif opcion == "6":
            cod = pedir_codigo("Ingrese codigo del producto: ")
            if buscar_prod(cod, cabeza) is not None:
                print("Error: ya existe un producto con ese codigo")
            else:
                nom = pedir_nombre("Ingrese nombre del producto: ")
                prec = pedir_precio("Ingrese precio del producto: ")
                cabeza, cola_lista = guardar_producto(cod, nom, prec, cabeza, cola_lista)
                print("Producto agregado correctamente")
                print("Catalogo actual:")
                print(ver_productos_adelante(cabeza))

        elif opcion == "7":
            print("Catalogo de productos (primero al ultimo):")
            if cabeza is None:
                print("El catalogo esta vacio")
            else:
                print(ver_productos_adelante(cabeza))

        elif opcion == "8":
            print("Catalogo de productos (ultimo al primero):")
            if cola_lista is None:
                print("El catalogo esta vacio")
            else:
                print(ver_productos_atras(cola_lista))

        elif opcion == "9":
            cod = pedir_codigo("Ingrese el codigo del producto a buscar: ")
            prod = buscar_prod(cod, cabeza)
            if prod is not None:
                print("Producto encontrado: " + texto_producto(prod))
            else:
                print("Error: no se encontro un producto con ese codigo")

        elif opcion == "10":
            cod = pedir_codigo("Ingrese el codigo del producto a eliminar: ")
            borrado, cabeza, cola_lista = borrar_producto(cod, cabeza, cola_lista)
            if borrado is not None:
                print("Producto eliminado correctamente: " + str(borrado))
                print("Catalogo despues de eliminar:")
                print(ver_productos_adelante(cabeza))
            else:
                print("Error: no existe un producto con ese codigo")

        elif opcion == "0":
            print("Saliendo del programa... Gracias por su tiempo")

        else:
            print("Error: debe seleccionar un numero de las opciones")

sistema()