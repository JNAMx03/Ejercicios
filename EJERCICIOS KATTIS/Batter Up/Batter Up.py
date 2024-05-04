suma = 0
n = int(input())
m = input()
m_split = m.split()
for x in m_split:
    suma = suma + int(x)
    if x == '-1':
        n = n - 1
        suma = suma + 1
print(suma/n)