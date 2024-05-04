# toca ingresar el tamaño de una lista(array), llenarla y luego sumar susa valores

def suma(numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum

if __name__ == "__main__":
    cantidad = int(input('Ingrese el numeros de valores: '))
    numeros = []

    for i in range(cantidad):
        num = int(input(f'ingrese el valor {i+1}: '))
        numeros.append(num)

    print(suma(numeros))