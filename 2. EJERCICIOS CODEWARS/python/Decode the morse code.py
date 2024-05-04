def decode_morse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morse = {
        ".-" : 'a', "-..." : 'b', "-.-." : 'c', "-.." : 'd', "." : 'e',
        "..-." : 'f', "--." : 'g', "...." : 'h', ".." : 'i', ".---" : 'j',
        "-.-" : 'k', ".-.." : 'l', "--" : 'm', "-." : 'n', "---" : 'o',
        ".--." : 'p', "--.-" : 'q', ".-." : 'r', "..." : 's', "-" : 't',
        "..-" : 'u', "...-" : 'v', ".--" : 'w', "-..-" : 'x', "-.--" : 'y',
        "--.." : 'z', ".----" : '1', "..---" : '2', "...--" : '3', "....-" : '4',
        "....." : '5', "-...." : '6', "--..." : '7', "---.." : '8', "----." : '9',
        "-----" : '0', "" : ' '
    }
    liste = list(morse_code.split(" "))
    s = ""
    for i in liste:
        s = s + morse.get(i)
        
    #print(morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', ''))
    return " ".join(s.split()).upper()

if __main__ (__name__):
    decode_morse(".... . -.--   .--- ..- -.. .")