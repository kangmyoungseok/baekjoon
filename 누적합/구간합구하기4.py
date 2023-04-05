import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = list(map(int,input().split()))

accum = [0] * (len(arr)+1)

for i in range(len(arr)):
    accum[i+1] = accum[i] + arr[i]


def solve():
    i,j = map(int,input().split())

    print(accum[j] - accum[i-1])

for i in range(M):
    solve()
