def staircase(n):
    for i in range(1, n+1):
        if i != n:
            print(" "*(n-i-1), "#"*i)
        else:
            print("#"*i)

if __name__ == "__main__":
    n = int(input("n: "))

    staircase(n)