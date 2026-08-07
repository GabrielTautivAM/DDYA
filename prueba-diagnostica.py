def solicitar_numero():
    print()
    print("por favor digite el numero")
    x = int(input())
    return x 

def verificar_signos(num):
    if num ==0:
        print("el numero es 0")
    elif num > 0:
        print("el numero es positivo")
    else:
        print("el numero es negativo")

def verificar_par(num):
    x = 0
    if num % 2 == 0:
        print("el numero es par")
        x=2
    else:
        print("el numero es impar")
        x=1
    return x 

def verificar_fibonacci(num):
    a = 0
    b = 1
    c = 0
    while b < num:
        c = b
        b = b + a 
        a = c
    if b == num:
        print("el numero es fibonacci")
    else:
        print("el numero no es fibonacci")


def verificar_primo(num):
    contador = 0 
    for rep in range(num):
        if num % (rep+1) == 0:
            contador +=1 
    if contador ==2:
        print("el numero es primo")
    else:
        print("el numero no es primo")

def main():
    num = solicitar_numero()
    verificar_signos(num)
    x= verificar_par(num)
    verificar_fibonacci(num)
    verificar_primo(num)
    print()
    print("ahora haremos lo mismo pero con su carne estudiantil")
    num = solicitar_numero()
    verificar_signos(num)
    x= verificar_par(num)
    verificar_fibonacci(num)
    verificar_primo(num)
    print()

main()


###punto 8, 9 y 10 no se como realizarlos, tendira que investigar 