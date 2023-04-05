import sys
def millerRaibn(n,a):
    # n-1 = m * 2^k 를 만족하는 m,k 구하기
    m,k = n-1,0
    while m % 2 == 0:
        m //= 2
        k += 1

    T = pow(a,m,n)
    if T == 1 or T == n-1 : return True

    for i in range(1,k):
        T = pow(T,2,n)
        if T == 1 : return False
        if T == n-1 : return True
    
    return False

def is_prime(p):
    return millerRaibn(p,2) and millerRaibn(p,3)

prime = [2,3,5,7]
for i in range(11,123456*2+1,2):
    if is_prime(i): prime.append(i)

N = int(sys.stdin.readline())
while N != 0:
    count = 0
    for i in range(N+1,2*N+1):
        if i in prime : count +=1
    print(count)
    N = int(sys.stdin.readline())





