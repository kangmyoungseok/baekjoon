import sys


N = int(input())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

cum = 0
result = 0
[1,2,3,3,4]
for i in arr:
    cum += i
    result += cum
print(result)