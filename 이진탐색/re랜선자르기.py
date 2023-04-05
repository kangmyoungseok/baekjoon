import sys

input = sys.stdin.readline

K,N = map(int,input().split())
arr = []
for i in range(K):
    arr.append(int(input()))

start,end = 1,max(arr)

def count_lan(a):
    result =0
    for i in arr:
        result += i // a
    return result

def bin_search(start,end):
    mid = (start + end) // 2
    count_lan_mid = count_lan(mid)
    count_lan_mid1 = count_lan(mid+1)
    if count_lan_mid >= N and count_lan_mid1 <N:
        return mid
    if count_lan_mid < N:
        return bin_search(start,mid-1)
    else:
        return bin_search(mid+1,end)

print(bin_search(start,end)) 