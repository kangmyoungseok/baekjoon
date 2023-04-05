import sys

N,M = map(int,sys.stdin.readline().split())

A = {}
arr = list(map(int,sys.stdin.readline().split()))
for i in arr:
    A[i] = 1


arr = list(map(int,sys.stdin.readline().split()))
onlyA = 0
onlyB = 0
common = 0
for i in arr:
    try:
        A[i]
        common +=1
    except:
        onlyB += 1
        pass
onlyA = len(A) - common
result = onlyA + onlyB
print(result)