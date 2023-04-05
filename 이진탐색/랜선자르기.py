import sys
input = sys.stdin.readline

N,K = map(int,input().split())

lan = []
for i in range(N):
    lan.append(int(input()))

start = 1
end = max(lan)
while start<=end:
    count = 0
    mid = (start + end) // 2

    for i in lan:
        count += i // mid
    
    if count >= K:
        start = mid +1
    else:
        end = mid -1

print(end)

arr = [75,90,70,80,65,80,96,86]
sum = 0
for i in arr:
    sum += i
sum / len(arr)

arr1 = [80,85]
arr2 = [85,85]
import math
math.sqrt((pow(arr1[0] - arr2[0],2) + pow(arr1[1] - arr2[1],2)))

