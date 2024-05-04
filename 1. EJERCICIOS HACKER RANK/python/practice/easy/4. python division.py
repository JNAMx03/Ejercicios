
def division(a, b):
    e = a // b
    d = a/ b

    return(f'{e}\n{d}')

if __name__ == "__main__":
    a = int(input('Ingrese el primer numero: '))
    b = int(input('Ingrese el segundo dumero: '))

    print(division(a, b))