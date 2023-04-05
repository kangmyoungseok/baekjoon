import sys

N,M = map(int,input().split())

S = []
for i in range(N):
    S.append(sys.stdin.readline().rstrip())

count = 0
for i in range(M):
    if sys.stdin.readline().rstrip() in S:
        count +=1

print(count)