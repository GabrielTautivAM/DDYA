import matplotlib.pyplot as plt
import networkx as nx

class NodoBST:
    def __init__(self, codigo):
        self.codigo = codigo
        self.hijo_izquierdo = None
        self.hijo_derecho = None

class NodoAVL:
    def __init__(self, codigo):
        self.codigo = codigo
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        self.altura = 1

def insertar_en_bst(nodo_actual, codigo):
    if nodo_actual is None:
        return NodoBST(codigo)
    if codigo < nodo_actual.codigo:
        nodo_actual.hijo_izquierdo = insertar_en_bst(nodo_actual.hijo_izquierdo, codigo)
    elif codigo > nodo_actual.codigo:
        nodo_actual.hijo_derecho = insertar_en_bst(nodo_actual.hijo_derecho, codigo)
    return nodo_actual

def obtener_altura(nodo):
    if nodo is None:
        return 0
    return nodo.altura

def actualizar_altura(nodo):
    nodo.altura = 1 + max(obtener_altura(nodo.hijo_izquierdo),
                          obtener_altura(nodo.hijo_derecho))

def obtener_balance(nodo):
    if nodo is None:
        return 0
    return obtener_altura(nodo.hijo_izquierdo) - obtener_altura(nodo.hijo_derecho)

def rotacion_derecha(nodo_desbalanceado):
    nueva_raiz = nodo_desbalanceado.hijo_izquierdo
    subarbol_movido = nueva_raiz.hijo_derecho

    nueva_raiz.hijo_derecho = nodo_desbalanceado
    nodo_desbalanceado.hijo_izquierdo = subarbol_movido

    actualizar_altura(nodo_desbalanceado)
    actualizar_altura(nueva_raiz)

    return nueva_raiz   

def rotacion_izquierda(nodo_desbalanceado):
    nueva_raiz = nodo_desbalanceado.hijo_derecho
    subarbol_movido = nueva_raiz.hijo_izquierdo

    nueva_raiz.hijo_izquierdo = nodo_desbalanceado
    nodo_desbalanceado.hijo_derecho = subarbol_movido

    actualizar_altura(nodo_desbalanceado)
    actualizar_altura(nueva_raiz)

    return nueva_raiz

def insertar_en_avl(nodo_actual, codigo):
    if nodo_actual is None:
        return NodoAVL(codigo)
    if codigo < nodo_actual.codigo:
        nodo_actual.hijo_izquierdo = insertar_en_avl(nodo_actual.hijo_izquierdo, codigo)
    elif codigo > nodo_actual.codigo:
        nodo_actual.hijo_derecho = insertar_en_avl(nodo_actual.hijo_derecho, codigo)
    else:
        return nodo_actual  

    actualizar_altura(nodo_actual)
    balance = obtener_balance(nodo_actual)

    if balance > 1 and obtener_balance(nodo_actual.hijo_izquierdo) >= 0:
        return rotacion_derecha(nodo_actual)
    if balance < -1 and obtener_balance(nodo_actual.hijo_derecho) <= 0:
        return rotacion_izquierda(nodo_actual)
    if balance > 1 and obtener_balance(nodo_actual.hijo_izquierdo) < 0:
        nodo_actual.hijo_izquierdo = rotacion_izquierda(nodo_actual.hijo_izquierdo)
        return rotacion_derecha(nodo_actual)
    if balance < -1 and obtener_balance(nodo_actual.hijo_derecho) > 0:
        nodo_actual.hijo_derecho = rotacion_derecha(nodo_actual.hijo_derecho)
        return rotacion_izquierda(nodo_actual)

    return nodo_actual

def recorrido_preorden(nodo, lista_resultado):
    if nodo is not None:
        lista_resultado.append(nodo.codigo)
        recorrido_preorden(nodo.hijo_izquierdo, lista_resultado)
        recorrido_preorden(nodo.hijo_derecho, lista_resultado)

def recorrido_inorden(nodo, lista_resultado):
    if nodo is not None:
        recorrido_inorden(nodo.hijo_izquierdo, lista_resultado)
        lista_resultado.append(nodo.codigo)
        recorrido_inorden(nodo.hijo_derecho, lista_resultado)

def recorrido_postorden(nodo, lista_resultado):
    if nodo is not None:
        recorrido_postorden(nodo.hijo_izquierdo, lista_resultado)
        recorrido_postorden(nodo.hijo_derecho, lista_resultado)
        lista_resultado.append(nodo.codigo)

def calcular_posiciones_y_conexiones(nodo, grafo, posiciones, x=0, y=0, nivel=1, ancho=1.0):
    if nodo is None:
        return

    grafo.add_node(nodo.codigo)
    posiciones[nodo.codigo] = (x, y)

    desplazamiento = ancho / (2 ** nivel)

    if nodo.hijo_izquierdo:
        grafo.add_edge(nodo.codigo, nodo.hijo_izquierdo.codigo)
        calcular_posiciones_y_conexiones(
            nodo.hijo_izquierdo, grafo, posiciones,
            x - desplazamiento, y - 1, nivel + 1, ancho
        )
    if nodo.hijo_derecho:
        grafo.add_edge(nodo.codigo, nodo.hijo_derecho.codigo)
        calcular_posiciones_y_conexiones(
            nodo.hijo_derecho, grafo, posiciones,
            x + desplazamiento, y - 1, nivel + 1, ancho
        )

def mostrar_arboles(raiz_bst, raiz_avl):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    if raiz_bst is not None:
        grafo_bst = nx.DiGraph()
        posiciones_bst = {}
        calcular_posiciones_y_conexiones(raiz_bst, grafo_bst, posiciones_bst)
        ax1.set_title("Árbol Binario de Búsqueda (BST)", fontsize=14, fontweight="bold")
        nx.draw(grafo_bst, pos=posiciones_bst, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrows=False, ax=ax1)
    
    if raiz_avl is not None:
        grafo_avl = nx.DiGraph()
        posiciones_avl = {}
        calcular_posiciones_y_conexiones(raiz_avl, grafo_avl, posiciones_avl)
        ax2.set_title("Árbol AVL Balanceado", fontsize=14, fontweight="bold")
        nx.draw(grafo_avl, pos=posiciones_avl, with_labels=True, node_size=2000, node_color="lightgreen", font_size=12, font_weight="bold", arrows=False, ax=ax2)

    plt.show()

def pedir_entero_positivo(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("Entrada inválida. Ingrese un número entero (sin letras ni decimales).")
            continue
        if numero <= 0:
            print("Por favor, ingrese un número mayor que 0.")
            continue
        return numero

def pedir_codigo(mensaje, codigos_ya_ingresados):
    while True:
        codigo = pedir_entero_positivo(mensaje)
        if codigo in codigos_ya_ingresados:
            print(f"El código {codigo} ya fue ingresado. Escriba uno diferente.")
            continue
        return codigo

def pedir_codigos_productos():
    cantidad = pedir_entero_positivo("Ingrese la cantidad de productos: ")
    codigos = []

    for i in range(cantidad):
        codigo = pedir_codigo(f"Ingrese el código {i + 1}: ", codigos)
        codigos.append(codigo)

    return codigos

def preguntar_si_o_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("Respuesta inválida. Escriba 's' para sí o 'n' para no.")

def ejecutar_programa():
    print("=" * 50)
    print(" ORGANIZACIÓN DE CÓDIGOS MEDIANTE ÁRBOLES (BST vs AVL)")
    print("=" * 50)

    codigos = pedir_codigos_productos()
    print(f"\nLista de códigos inicial: codigos = {codigos}\n")

    raiz_bst = None
    for codigo in codigos:
        raiz_bst = insertar_en_bst(raiz_bst, codigo)

    raiz_avl = None
    for codigo in codigos:
        raiz_avl = insertar_en_avl(raiz_avl, codigo)

    bst_preorden, bst_inorden, bst_postorden = [], [], []
    recorrido_preorden(raiz_bst, bst_preorden)
    recorrido_inorden(raiz_bst, bst_inorden)
    recorrido_postorden(raiz_bst, bst_postorden)

    avl_preorden, avl_inorden, avl_postorden = [], [], []
    recorrido_preorden(raiz_avl, avl_preorden)
    recorrido_inorden(raiz_avl, avl_inorden)
    recorrido_postorden(raiz_avl, avl_postorden)

    print("-" * 50)
    print("RECORRIDOS DEL ÁRBOL BST")
    print("-" * 50)
    print(f"Recorrido Preorden del árbol BST  : {bst_preorden}")
    print(f"Recorrido Inorden del árbol BST   : {bst_inorden}")
    print(f"Recorrido Postorden del árbol BST : {bst_postorden}\n")

    print("-" * 50)
    print("RECORRIDOS DEL ÁRBOL AVL")
    print("-" * 50)
    print(f"Recorrido Preorden del árbol AVL  : {avl_preorden}")
    print(f"Recorrido Inorden del árbol AVL   : {avl_inorden}")
    print(f"Recorrido Postorden del árbol AVL : {avl_postorden}\n")

    mostrar_arboles(raiz_bst, raiz_avl)

def main():
    while True:
        ejecutar_programa()
        print("-" * 50)
        if not preguntar_si_o_no("¿Desea probar con otro conjunto de datos? (s/n): "):
            print("¡Programa finalizado!")
            break
        print("\n")

main()