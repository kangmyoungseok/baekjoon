# N < 900만 인 경우 a=31,73만 해도 충분
# N < 47억인 경우 2,7,61 충분
# 그냥 깔끔하게 2,3,5,7,11 로 암기


# 소수 구하기 문제
# 밀러 라빈 테스트를 2,3,5,7,11에 대해서 소수라고 판단하면 소수이다.
    

def millerRabin(n,a):
    # 1. n-1 = m * 2^k 를 만족하는 m,k를 구한다.
    m,k = n-1,0
    while m % 2 == 0:
        m //= 2
        k += 1
    
    T = pow(a,m,n)
    if T == 1 or T == n-1:
        return True # prime
    
    for i in range(1,k):
        T = pow(T,2,n)
        if T == 1 : return False    # composite
        if T == n-1 : return True   # prime
    
    return False    # composite

def is_prime(p):
    if p < 15:
        if p == 1:
            return False
        if p in [2,3,5,7,11,13]:
            return True
            
    if p % 2 == 0:
        return False
    
    return millerRabin(p,2) \
        and millerRabin(p,3)


M,N = map(int,input().split())

for i in range(M,N+1):
    if is_prime(i): print(i)
    