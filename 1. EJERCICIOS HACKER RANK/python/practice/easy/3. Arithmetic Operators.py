# solo es hacer una suma, resta y multiplicacion de dos numeros


def Arith_Operators(a, b):
    s = a + b
    r = a - b
    m = a * b

    return(f'{s}\n{r}\n{m}')

if __name__ == '__main__':
    a = int(input('Ingrese el primer numero: '))
    b = int(input('Ingrese el segundo numero: '))

    print(Arith_Operators(a, b))