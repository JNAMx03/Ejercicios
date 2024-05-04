b = 0
x = input()
n = input()
for i in range(int(n)):
    p = input()
    a = (int(x) - int(p))
    b = (int(b) + int(a))
print(b+int(x))