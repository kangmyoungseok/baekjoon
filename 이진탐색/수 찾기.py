import sys

input = sys.stdin.readline

N = int(input())
Arr = list(map(int,input().split()))
M = int(input())
target = list(map(int,input().split()))


Arr.sort()

def bin_search(a,start,end):
    if start > end :
        return 0
    mid = (start + end) // 2
    if a == Arr[mid]:
        return 1
    if a < Arr[mid]:
        return bin_search(a,start,mid -1)
    else:
        return bin_search(a,mid+1,end)


for i in target:
    print(bin_search(i,0,N-1))
