# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the solve function below.
def solve(s):

    #MI SOLUCION
    # arr = s.split(" ")
    # res = []
    # for x in range (len(arr)):
    #     res.append(arr[x].capitalize())
    
    # return " ".join(res)

    #SOLUCION DE OTRO
    return ' '.join([word[0:1].upper()+word[1:] for word in s.split(' ')])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()