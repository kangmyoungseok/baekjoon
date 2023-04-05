import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

sum = [arr[0]]

for i in range(1,n):
    sum.append(max(arr[i],sum[i-1]+arr[i]))

print(max(sum))