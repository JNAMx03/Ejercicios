from ast import For
import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    #MI SOLUCIONS
    # pos1, pos2, time1, time2 = x1, x2, 0, 0
    # if(pos1 < 1000): limit= 10000
    # if(pos1 >= 1000 and pos1 <= 10000): limit= 100000000
    # if(x1 > x2): 
    #     return "NO"
    # else:
    #     while (pos1 <= limit):
    #         pos1 += v1
    #         time1 += 1
            
    #         pos2 += v2
    #         time2 += 1

    #         if(pos1 == pos2 and time1 == time2):
    #             print(pos1)
    #             print(time1)
    #             return "YES"
    #     return "NO"

    #SOLUCION DE OTROS
    if(v1 < v2): return "NO"
    while(x1 < x2):
        x1 += v1
        x2 += v2
        if(x1 == x2): return "YES"
    return "NO"



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
