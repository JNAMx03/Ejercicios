#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(size):
    # your code goes here

    #-------------------- MI BASURA
    # abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # aux = []
    # aux2 = []
    # rev = []
    
    # st = ""
    # st2 = ""
    

    # a= 1

    # t = size+(size-1)
    # tt = t+(t-1)

    # print(tt)

    # for i in range(size):
    #     aux.append(abc[i])        

    # #rev = aux.copy()
    # aux.sort(reverse=True)

    # for i in range(1, size):
    #     aux2.append(abc[i])

    # st = "".join(aux)
    # st2 = "".join(aux2)

    # for i in range(int(len(st))):
    #     sts = st[0:i+1]
    #     #print(st[0:i+1])
    #     #print((len(st)-i)-len(st))
    #     if((len(st)-i)-len(st)!=0):
    #         #print(st[(len(st)-i)-len(st):])
    #         sts = sts + st2[(len(st2)-i)-len(st2):]
    #         rev.append(list(sts))
    #     print("-".join(sts).center(tt, "-"))

    # for i in range(len(rev)):
    #     print(rev[i])
            
        
    #     # st = st + str(aux[i])
    #     # sts = st + sts + str(aux[i-1])
    #     # print(sts.center(tt, "-"))   

    #---------------------------LA DE OTRO XD  
    width  = size*4-3
    string = ''
       
    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):    
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))
        string = ''

    for i in range(size-1,0,-1):
        string = ''
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))    

   

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)