caras = input()
caras_split = caras.split()
if int(caras_split[0]) <= int(caras_split[1]):
    menor = int(caras_split[0])
    mayor = int(caras_split[1])
else:
    menor = int(caras_split[1])
    mayor = int(caras_split[0])

for x in range(mayor+1):
    a = 1 + x
    if ((menor+1) == a):
        print(a)
        menor = menor + 1