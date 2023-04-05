import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    A,B = map(int,input().split())
    arr.append([A,B])

arr.sort(key= lambda x:x[0])

B_arr = []
for a in arr:
    B_arr.append(a[1])

# B에서 가장 긴 증가하는 부분수열 찾기
dp = [0] * 501
for i in B_arr:
    dp[i] = max(dp[:i]) + 1

print(N - max(dp))





