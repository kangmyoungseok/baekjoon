def fibo_memoization(n):
    global fibo_dp
    memo = [1 for x in range(50)]
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i -2]
        fibo_dp +=1

    return memo[n]



fibo_dp = 0

N = int(input())
result = fibo_memoization(N)

print(f"{result} {fibo_dp}")