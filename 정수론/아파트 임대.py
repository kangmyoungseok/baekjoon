import sys
input = sys.stdin.readline

# 2,3,5,7,11에 대해서 테스트
# 페르마 소정리

def miller_rabin(n,a):
    # n - 1 = m * 2^k 를 만족하는 m,k 구하기
    m,k = n-1,0
    while m % 2 == 0 :
        m //= 2
        k +=1
    
    T = pow(a,m,n)
    # a^n-1 mod n = 1을 만족하므로 소수이다.
    if T == 1 or T == n-1:
        return True # primary
    
    for i in range(1,k):
        T = pow(T,2,n)
        if T == 1: return False #composite
        if T == n-1: return True # composite
    
    return False #primary

def is_prime(n):
    return miller_rabin(n,2) and\
        miller_rabin(n,3) and\
        miller_rabin(n,5) and\
        miller_rabin(n,7) and\
        miller_rabin(n,11)
    
N = int(input())

count = 0
for i in range(N):
    num = int(input())
    if is_prime(2*num +1):
        count+=1

print(count)