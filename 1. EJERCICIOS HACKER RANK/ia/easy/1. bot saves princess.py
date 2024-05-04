#!/usr/bin/python
import math

def displayPathtoPrincess(n,grid):
#print all the moves here
    center = math.ceil(n/2)-1
    for i in range(len(grid)):
        if('p' in str(grid[i])):
            pC = i
            pR = str(grid[i]).index('p')
    dC = pC - center
    dR = pR - center

    #print(''.join(['DOWN\n'*abs(dC)if(dC>0)else"UP\n"*abs(dC), 'RIGTH\n'*abs(dR)if(dR>0)else"LEFT\n"*abs(dR)]))
    if(dC > 0):
        for _ in range(abs(dC)):
            print("DOWN")
    else:
        for _ in range(abs(dC)):
            print("UP")
    if(dR > 0):
        for _ in range(abs(dR)):
            print("RIGTH")
    else:
        for _ in range(abs(dR)):
            print("LEFT")

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)