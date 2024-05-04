# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true


def print_formatted(number):
    #------------------------MIO
    l1 = len(bin(number)[2:]) #no se qeu hace, solo devuelve un 2 xd
    for i in range(1, number+1):
        #txt = "{0}  {0:o}  {0:X}  {0:b}".format(i)
        octt = "{:o}".format(i)
        hexx = "{:X}".format(i)
        binn = "{:b}".format(i)
        print(str(i).rjust(l1,' '),end=" ")
        print(octt.rjust(l1,' '),end=" ")
        print(hexx.rjust(l1,' '),end=" ")
        print(binn.rjust(l1,' '),end=" ")
        print("")
        #print("|{:>8}|".format(txt))

    #-------------------------DE ALGUIEN MAS

    l1 = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i)[2:].rjust(l1,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1,' '),end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)