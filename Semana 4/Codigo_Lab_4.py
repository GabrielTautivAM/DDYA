def memoized_coin_change(monedas, n):
    r = [None] * (n + 1)
    solucion = [0] * (n + 1)
    mini_monedas = aux(monedas, n, r, solucion)
    
    if mini_monedas == float('inf'):
        return -1, []

    monedas_usadas = []
    monto_actual = n
    
    while monto_actual > 0:
        moneda = solucion[monto_actual]
        monedas_usadas.append(moneda)
        monto_actual -= moneda
        
    return mini_monedas, monedas_usadas

def aux(monedas, n, r, solucion):
    if n < 0:
        return float('inf')
    if n == 0:
        return 0
        
    if r[n] is not None:
        return r[n]
    
    q = float('inf')
    mejor_moneda = 0
    
    for moneda in monedas:
        if n - moneda >= 0:
            res = aux(monedas, n - moneda, r, solucion)
            if res != float('inf') and res + 1 < q:
                q = res + 1
                mejor_moneda = moneda
                
    r[n] = q
    solucion[n] = mejor_moneda
    return q

def obtener_cambio_valido():
    while True:
        print("\nIngrese la cantidad de cambio que desea:")
        entrada = input().strip()
        
        if not entrada.isdigit():
            print("Error al ingresar el cambio, solo se permiten numeros enteros positivos. digite nuevamente por favor")
            continue
            
        x = int(entrada)

        if x % 50 != 0:
            x = round(x / 50) * 50
            print(f"La cantidad fue aproximada a: {x}")
            
        print(f"Esta seguro de que desea calcular el cambio para {x}? [SI] o [NO]:")
        y = input().strip().upper()
        
        while y != "SI" and y != "NO":
            print("invalido, por favor escriba [SI] o [NO]:")
            y = input().strip().upper()
            
        if y == "SI":
            return x
        else:
            print("Por favor ingrese el cambio.")

def main():
    monedas = [1000, 500, 200, 100, 50]
    print("Bienvenido, calcularemos el cambio en monedas para sus clientes.")
    
    continuar_programa = True
    while continuar_programa:
        x = obtener_cambio_valido()
        print("\nDETALLES DEL CAMBIO")
        if x == 0:
            print("El cambio es 0. No hay nada que dar")
        else:
            cant, lista_monedas = memoized_coin_change(monedas, x)
            if cant != -1:
                print("Cantidad minima de monedas usadas:", cant)
                formato_suma = " + ".join(map(str, lista_monedas))
                print(f"Monedas usadas para el cambio: {formato_suma} = {x}")
            else:
                print("No fue posible dar cambio exacto con las monedas disponibles.")
            
        print("\n¿Desea realizar otra consulta? [SI] para continuar o cualquier otra tecla para salir:")
        continuar = input().strip().upper()
        
        if continuar != "SI":
            continuar_programa = False
            print("Muchas gracias por su tiempo, que tenga un feliz día.")

def test(input, expected_output):
    monedas = [1000, 500, 200, 100, 50]
    got_output, _ = memoized_coin_change(monedas, input)
    assert got_output == expected_output, f"se obtuvo {got_output}, pero se esperaba {expected_output}"
    print(f"Paso caso de prueba {input} -> {expected_output}")

def bench(n: int, step: int = 50) -> list[tuple[int, float]]:
    print("Generando datos ...", end='')
    import time
    results: list[tuple[int, float]] = []
    monedas = [1000, 500, 200, 100, 50]
    
    for size in range(50, n + 1, step):
        ti = time.perf_counter()
        memoized_coin_change(monedas, size)
        tf = time.perf_counter()
        
        delta = (tf - ti) * 1000
        print(".", end="")
        results.append((size, delta))
    print()
    return results

def dibujar(x, y, dimensiones=(7, 5)):
    assert len(x) == len(y)
    import matplotlib.pyplot as plt
    plt.figure(figsize=dimensiones)
    plt.plot(x, y, marker='o', markersize=3)
    plt.title("Rendimiento del algoritmo Memoized Coin Change")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.grid(True)
    plt.show()

tiempos = bench(2000, step=50)
x = [size for size, timing in tiempos]
y = [timing for size, timing in tiempos]
dibujar(x, y)
