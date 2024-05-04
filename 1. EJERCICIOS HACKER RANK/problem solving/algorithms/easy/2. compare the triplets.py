# comparar los valores de dos listas(arrays) y saber cual es mayor en las mismas posiciones y dar putnos e imprimirlos


def triplets(a, b):

    if len(a) == len(b):
        p = [0, 0]
        for i in range(len(a)):
            if a[i] > b[i]:
                p[0] += 1
            elif a[i] < b[i]:
                p[1] +=1
        
        return p


if __name__ == "__main__":
    a1 = input('ingrese los valores de alice: ')
    b1 = input('ingrese los valores de bobs: ')

    a = a1.split(" ")
    b = b1.split(" ")

    for i in range(len(a)):
        a[i] = int(a[i])

    for i in range(len(b)):
        b[i] = int(b[i])

    print(triplets(a, b))