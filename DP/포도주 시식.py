import sys
input = sys.stdin.readline

N = int(input())

arr = [0]
for i in range(N):
    arr.append(int(input()))

dp = [0] * 10001

if N == 1:
    print(arr[1])
    sys.exit()
if N == 2:
    print(arr[1]+arr[2])
    sys.exit()
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for i in range(3,N+1):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i],dp[i-2] + arr[i],dp[i-1])

print(dp[N])