import sys
N = int(input())
D = list(map(int,sys.stdin.readline().split()))
P = list(map(int,sys.stdin.readline().split()))


current_price = P[0]
total = 0
for i in range(len(D)):
    if P[i] < current_price:
        current_price = P[i]
    total += current_price * D[i]

print(total)
    