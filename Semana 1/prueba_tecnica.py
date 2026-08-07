def solicitar_numero():
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
    verificar_primo(num)

main()
