import sys
input = sys.stdin.readline

R,G,B=0,1,2

N = int(input())


house = []
for i in range(N):
    house.append(list(map(int,input().split())))

bestR = [house[0][R]]
bestG = [house[0][G]]
bestB = [house[0][B]]

for i in range(1,N):
    bestR.append(min(bestG[i-1],bestB[i-1]) + house[i][R])
    bestG.append(min(bestR[i-1],bestB[i-1]) + house[i][G])
    bestB.append(min(bestR[i-1],bestG[i-1]) + house[i][B])

print(min(bestR[-1],bestG[-1],bestB[-1]))