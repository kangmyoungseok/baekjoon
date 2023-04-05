import sys

N = int(input())

arr = list(map(int,sys.stdin.readline().split()))

arr2 = list(set(arr))
arr2 = sorted(arr2)

map_arr = {}
for i in range(len(arr2)):
    map_arr[arr2[i]] = i

for i in range(N):
    print(map_arr[arr[i]],end=' ')
