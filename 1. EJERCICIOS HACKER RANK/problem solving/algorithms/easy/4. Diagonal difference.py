# crear una matriz, llenarla y sumar sus diagonales, y luego el valor absoluto de resta del resusltado de la sumas

def diagonalDifference(arr):
    sum = [0, 0]

    for i in range(len(arr)):
        sum[0] += arr[i][i]
        sum[1] += arr[i][len(arr)-i-1]

    res = abs(sum[0] - sum[1])
    return res

if __name__ == "__main__":
    n = int(input('Ingrese el tamaño de la matriz cuadrada: ')) 

    arr = []

    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(int(input(f'ingresde el valor para la posicion {i}, {j}: ')))

    print(diagonalDifference(arr))