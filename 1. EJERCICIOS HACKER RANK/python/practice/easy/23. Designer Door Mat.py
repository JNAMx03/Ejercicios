def ooo(x, y):
    line = "-"*x
    point = ".|."*(y+(y-1))
    return(line+point+line)  

if __name__ == '__main__':
    n, m = input().split()
    nn = int(n)
    mm = int(m)
    guion = int((mm/2)-1)
    ar = []
    
    for i in range(int(nn/2)):
        ar.append(ooo(guion, (i+1)))
        guion = guion - 3
        
    j = 0
    while j <len(ar):
        print(ar[j])
        j = j + 1
            
    print("-"*(int((mm-7)/2))+"WELCOME"+"-"*(int((mm-7)/2)))
                    
    j = (len(ar)-1)
    while j>=0:
        print(ar[j])
        j = j -1


#----------------------------------

N, M = map(int, input().split())
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))