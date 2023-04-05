import sys

N = int(input())

arr = [0 for x in range(10001)]
for i in range(N):
    arr[int(sys.stdin.readline())] += 1

num=0
for i in range(10001):    
    for j in range(arr[i]):
        print(i)

    