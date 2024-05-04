def timeConversion(s):
    if s[8] == 'P' and s[0:2] != '12':
        x = str(int(s[0]) + 1)
        y = str(int(s[1]) + 2)
        z = x + y
        for i in range(2, len(s)-2 ):
            z = z + s[i]
    elif s[8] == 'A' and s[0] == '1' and s[1] == '2':
        x = "0"
        y = "0"
        z = x + y
        for i in range(2, len(s)-2 ):
            z = z + s[i]
    else:
        z = ""
        for i in range(len(s)-2 ):
            z = z + s[i]

    return(z)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()