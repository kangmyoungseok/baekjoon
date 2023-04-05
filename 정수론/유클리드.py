import sys

def euclid_gcd(m,n):
    if n > m:
        n,m = m,n
    if m%n == 0:
        return n
    else:
        return euclid_gcd(n,m%n)

def lcm(m,n):
    return int(m // euclid_gcd(m,n) ) * n

N = int(input())
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    print(lcm(a,b))