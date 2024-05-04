# ingresar el numero de elemtnos de una lista(array), llenarla con numeros grandes y sumar esos numeros, por lo que genera un long  

def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum += i

    return sum

if __name__ == "__main__":
    ar_count = int(input('ingrese la cantidad de numeros: '))

    ar1 = input('Ingrese los numeros: ')

    ar = ar1.split(' ')

    for i in range(len(ar)):
        ar[i] = int(ar[i])

    print(aVeryBigSum(ar))