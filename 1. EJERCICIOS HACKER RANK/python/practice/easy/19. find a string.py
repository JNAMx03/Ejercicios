def count_substring(string, sub_string):
   
    # ultima = 0
    # fin = 0
    # while(True):
    #     f = string.find(sub_string, ultima)
        
    #     ultima = f+1

    #     cc = 0
        
    #     for i in range(len(sub_string)):
    #         if(string[f] == sub_string[i] ):
    #             cc += 1
    #             f += 1
    #     if(cc == len(sub_string)):
    #         fin += 1  

    #     if((ultima-1) + len(sub_string) >= len(string) or ultima <= 0):
    #         break 
    fin = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            fin += 1
        
    return fin

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)