from array import *

def reverseArray(a):
    # Write your code here
    #SOLUCION 1, RAPIDA, CON FUNCION
    # a.reverse()
    # return a

    #SOLUCION 2, LENTA, SIN FUNCION
    # rev = []
    # for i in range(len(a)):
    #     rev.append(a[len(a)-i-1])

    # return rev

    #SOLUCION 3, MAS LENTA, SIN FUNCION
    nums = array('i', a)
    print(type(nums))
    print(nums)
    nums.reverse()
    print(nums)
    return nums.tolist()


if __name__ == '__main__':
    

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(res)
