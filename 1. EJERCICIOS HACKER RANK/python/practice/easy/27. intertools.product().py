def product(A, B):
    for i in A:
        for j in B:
            print(f"({i}, {j})", end=' ')

    # for i in range(len(A)):
    #     for j in range(len(B)):
    #         print(f"({A[i]}, {B[j]})")

if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    product(A, B)