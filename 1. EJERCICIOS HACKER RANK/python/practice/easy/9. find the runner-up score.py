def main():
    n = int(input("n: "))
    arr = map(int, input().split())
        
    arrsort = sorted(arr)

    a = arrsort.count(arrsort[n-1])

    if a > 1:
        ru = arrsort[n-1-a]
    else:
        ru = arrsort[n-1-1]
    
    print(ru)

if __name__ == '__main__':
    main()