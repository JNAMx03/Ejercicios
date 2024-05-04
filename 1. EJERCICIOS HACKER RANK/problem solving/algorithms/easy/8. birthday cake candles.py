def birthdayCakeCandles(candles):
    x = max(candles)
    print(candles.count(x))
    # return(candles.count(x))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    # fptr.write(str(result) + '\n')

    # fptr.close()