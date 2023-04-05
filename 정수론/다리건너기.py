def binomial(n,k):
    boonja = 1
    for i in range(k):
        boonja = boonja * (n-i)
    boonmo = 1
    for i in range(1,k+1):
        boonmo = boonmo * i
    return int(boonja // boonmo)

def solve():
    k,n = map(int,input().split())
    result = binomial(n,k)
    print(result)

T = int(input())

for i in range(T):
    solve()