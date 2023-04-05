import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

dp=[0] * 1001
result = [0] * 1001


for a in arr[::-1]:
    N -=1
    dp[a] = max(dp[:a]) + 1
    result[N] = dp[a]

dp = [0] * 1001

for a in arr:
    dp[a] = max(dp[:a]) +1
    result[N]+= (dp[a]-1)
    N +=1

print(max(result))
