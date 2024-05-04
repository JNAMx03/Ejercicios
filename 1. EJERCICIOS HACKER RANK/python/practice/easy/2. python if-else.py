# saber si un numero es par o impar con otras condiciones de rango e imprimir si es raro o no


def if_else(n):
    if n % 2 != 0:
        m = 'Weird'
    else:
        if n >= 2 and n <= 5:
            m = 'Not Weird'
        elif n >= 6 and n <= 20:
            m = 'Weird'
        else:
            m = 'Not Weird'
    
    return m

if __name__ == "__main__":
    n = int(input('ingrese un numero: '))

    print(if_else(n))