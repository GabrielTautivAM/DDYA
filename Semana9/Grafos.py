import collections
import networkx as nx
import matplotlib.pyplot as plt

def mostrar_grafo_grafico(grafo):
    print("=== REPRESENTACIÓN GRÁFICA DE LA RED ===")
    print("Generando ventana con la visualización de la red...")
    print("IMPORTANTE: Para continuar con el programa, debes CERRAR la ventana del gráfico.\n")
    
    G = nx.Graph(grafo)
    
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2500, 
            font_size=12, font_weight='bold', edge_color='gray', width=2)
    plt.title("Red de Distribución de Mensajería", fontsize=16)
    
    plt.show()

def imprimir_lista_adyacencia(grafo):
    print("=== LISTA DE ADYACENCIA ===")
    print("grafo = {")
    for centro, conexiones in grafo.items():
        conexiones_str = '", "'.join(conexiones)
        print(f'    "{centro}": ["{conexiones_str}"],')
    print("}\n")

def obtener_centro_valido(grafo, mensaje):
    while True:
        centro = input(mensaje).strip().upper()
        if centro in grafo:
            return centro
        print(f"Error: El centro '{centro}' no existe. Por favor, ingrese un centro válido.")

def bfs(grafo, inicio):
    visitados = set()
    cola = collections.deque([(inicio, 0)]) 
    visitados.add(inicio)
    
    recorrido = []
    distancias = {}

    while cola:
        centro_actual, distancia = cola.popleft()
        recorrido.append(centro_actual)
        
        if distancia not in distancias:
            distancias[distancia] = []
        distancias[distancia].append(centro_actual)
        
        for conexion in grafo[centro_actual]:
            if conexion not in visitados:
                visitados.add(conexion)
                cola.append((conexion, distancia + 1))

    print(f"Recorrido BFS desde {inicio}: {' -> '.join(recorrido)}")
    for dist, centros in distancias.items():
        print(f"Distancia {dist}: {', '.join(centros)}")
    print()

def dfs(grafo, inicio):
    visitados = set()
    recorrido = []

    def dfs_recursivo(centro_actual):
        visitados.add(centro_actual)
        recorrido.append(centro_actual)
        for conexion in grafo[centro_actual]:
            if conexion not in visitados:
                dfs_recursivo(conexion)

    dfs_recursivo(inicio)
    print(f"Recorrido DFS desde {inicio}: {' -> '.join(recorrido)}\n")

def buscar_ruta_bfs(grafo, inicio, destino):
    visitados = set()
    cola = collections.deque([[inicio]]) 
    visitados.add(inicio)

    if inicio == destino:
        print(f"Centro encontrado. Ruta: {inicio} Cantidad de conexiones: 0\n")
        return

    while cola:
        ruta = cola.popleft()
        centro_actual = ruta[-1]

        for conexion in grafo[centro_actual]:
            if conexion == destino:
                ruta.append(conexion)
                print(f"Centro encontrado. Ruta: {' -> '.join(ruta)} Cantidad de conexiones: {len(ruta) - 1}\n")
                return
            
            if conexion not in visitados:
                visitados.add(conexion)
                nueva_ruta = list(ruta)
                nueva_ruta.append(conexion)
                cola.append(nueva_ruta)

    print("No existe una ruta hasta el centro solicitado.\n")

def agregar_centro(grafo):
    while True:
        nuevo_centro = input("Ingrese el nuevo centro: ").strip().upper()
        if nuevo_centro in grafo:
            print(f"El centro '{nuevo_centro}' ya existe en la red. Intente con un nombre diferente.")
        elif not nuevo_centro:
            print("El nombre del centro no puede estar vacío.")
        else:
            break

    grafo[nuevo_centro] = []
    
    print(f"A continuación, indique con qué centros existentes desea conectar '{nuevo_centro}'.")
    print("Presione ENTER sin escribir nada para terminar de agregar conexiones.")
    
    while True:
        conexion = input(f"Conectar {nuevo_centro} con: ").strip().upper()
        if not conexion:
            break
            
        if conexion not in grafo:
            print(f"Error: El centro '{conexion}' no existe. Intente con un centro válido.")
        elif conexion in grafo[nuevo_centro]:
            print(f"Ya existe una conexión registrada con el centro '{conexion}'.")
        else:
            grafo[nuevo_centro].append(conexion)
            grafo[conexion].append(nuevo_centro)
            print(f"Conexión {nuevo_centro} - {conexion} agregada correctamente.")
    
    print("\nCentro y conexiones agregadas exitosamente.\n")
    
    imprimir_lista_adyacencia(grafo)
    inicio = obtener_centro_valido(grafo, "Seleccione nuevamente el vértice (centro) desde el cual comenzarán los recorridos: ")
    print()
    bfs(grafo, inicio)
    dfs(grafo, inicio)

def main():
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "G"],
        "F": ["C", "G"],
        "G": ["E", "F"]
    }

    print("INICIALIZACIÓN DEL SISTEMA DE RED DE DISTRIBUCIÓN...\n")
    
    mostrar_grafo_grafico(grafo)
    
    imprimir_lista_adyacencia(grafo)
    
    print("=== RECORRIDOS INICIALES DESDE 'A' ===")
    bfs(grafo, "A")
    dfs(grafo, "A")

    while True:
        print("====== MENÚ DEL ADMINISTRADOR ======")
        print("1. Seleccionar centro inicial y ejecutar recorridos")
        print("2. Buscar un centro en la red")
        print("3. Agregar nuevos centros (mostrará lista y ejecutará recorridos)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        print()

        if opcion == "1":
            inicio = obtener_centro_valido(grafo, "Ingrese el centro inicial: ")
            bfs(grafo, inicio)
            dfs(grafo, inicio)

        elif opcion == "2":
            inicio = obtener_centro_valido(grafo, "Centro inicial: ")
            destino = obtener_centro_valido(grafo, "Centro que desea buscar: ")
            buscar_ruta_bfs(grafo, inicio, destino)

        elif opcion == "3":
            agregar_centro(grafo)

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo seleccionando un número del 1 al 4.\n")

main()