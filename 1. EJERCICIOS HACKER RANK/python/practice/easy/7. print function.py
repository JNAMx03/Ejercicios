def function(n):
    string = ''
    for i in range(1, n+1):
        string += str(i)

    return string

if __name__ == "__main__":
    n = int(input('ingrese un numero: '))
    print (function(n))