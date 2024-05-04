# https://www.hackerrank.com/challenges/collections-counter/problem

def collectionsCounter(A, N):
    direct = {} #diccionario vacio
    for i in A:
        if i not in direct: #un ciclo para llenar el diccionario, si no esta la llave, se agrega al diccionario y si ya esta, se va sumando al valor de esa llave
            direct[i] = 1 
        else:
            direct[i] = direct[i]+1

    sum = 0
    for _ in range(0, N): #un ciclo para los zapatos vendidos
        n1, n2 = map(int, input().split()) #dos valores, el zapato y el precio
        if n1 in direct: #ahora una validacion para saber si esta (n1) y luego para saber si hay mas de 0, y si lo hay se resta el valor de esa llave y se van sumando los precios(n2)
            if direct[n1] > 0: 
                direct[n1] = direct[n1]-1
                sum += n2
    print(sum)
    

if __name__ == '__main__':
    X = int(input()) #ingresamos la cantidad de zapatos, no se utiliza para nada xd
    A = list(map(int, input().split())) #ingresamos y separamos cada zapato en una lista
    N = int(input()) #ingresamos la cantidad de zapatos vendidos
    collectionsCounter(A, N)


#otra solucion mas practica, pero no utiliza diccionarios solo listas y elimina los valores que ya se pidieron

# shoes=int(input())
# sizes=input().split()
# cust=int(input())
# money=0
# for i in range(0,cust):
#     visted=input().split()
#     if visted[0] in sizes:
#         sizes.remove(visted[0])
#         money+=int(visted[1])
# print(money)