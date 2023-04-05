# 에라토스테네스의 체
# 소수를 모두 배열에 넣는다.
prime = [True for i in range(10001)]
prime[0] = False
prime[1] = False
for i in range(2,10001):
    if prime[i] == True:
        for j in range(i*2, 10001, i ):
            prime[j] = False

def solve():
    N = int(input())
    for i in range(N//2+1):
        left = N//2 -i
        right = N//2 + i
        if prime[left] and prime[right]:
            print(f"{left} {right}")
            break

T = int(input())
for i in range(T):
    solve()