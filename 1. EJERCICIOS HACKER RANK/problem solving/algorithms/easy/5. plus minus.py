def main():
    n = int(input("n: "))
    arr = list(map(int, input().rstrip().split()))

    men =0 
    may = 0
    cer = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            men += 1
        if arr[i] > 0:
            may += 1
        if arr[i] == 0:
            cer += 1
        
    print(may/n)
    print(men/n)
    print(cer/n)

if __name__ == "__main__":
    main()