lista = []
valss = []

def inserts():
    lista.insert(int(valss[0]), int(valss[1]))

def prints():
    print(lista)
    
def removes():
    lista.remove(int(valss[0]))
    
def appends():
    lista.append(int(valss[0]))

def sorts():
    lista.sort()
    
def pops():
    lista.pop()
    
def reverses():
    lista.reverse()    


def error():
    print("No command")

def commands(command):
    switch = {
        "insert": inserts,
        "print": prints,
        "remove": removes,
        "append": appends,
        "sort": sorts,
        "pop": pops,
        "reverse": reverses,
    }
    switch.get(command, error)()
    

if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        Command, *vals = input().split()
        valss = vals
        commands(Command)