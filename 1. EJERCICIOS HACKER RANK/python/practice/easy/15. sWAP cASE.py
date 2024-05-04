def swap_case(s):
    a=""
    for i in range(len(s)):
        if(s[i].isalpha()):
            if(s[i].islower()):
                a = a + s[i].upper()
            else:
                a = a + s[i].lower()
        else:
            a = a + s[i]
    return a

if __name__ == '__main__':
    normalCase = input()
    print(swap_case(normalCase))
    