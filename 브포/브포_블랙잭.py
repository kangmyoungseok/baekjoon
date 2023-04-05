import sys
N,M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

max = 0
arr.sort()
for i in range(len(arr)):
    if arr[i] >= M:
        break
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            sum = arr[i] + arr[j] + arr[k]
            if sum > max and sum <= M:
                max = sum

print(max)