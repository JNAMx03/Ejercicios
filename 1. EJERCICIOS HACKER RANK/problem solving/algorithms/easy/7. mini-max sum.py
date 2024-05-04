def miniMaxSum(arr):
    may = 0
    men = 0

    org = sorted(arr)

    for i in range(len(org)):
        if i > 0:
            may += org[i]
            
        if i < len(org)-1:
            men += org[i]

    print(men, may)


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)