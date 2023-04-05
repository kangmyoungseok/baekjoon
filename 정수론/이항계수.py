def binomial(n,k):
    # n! / (n-k)!
    boonja = 1
    for i in range(k):
        boonja = boonja * (n - i)
    boonmo = 1
    for i in range(1,k+1):
        boonmo = boonmo * i
    return int(boonja // boonmo)

n,k = map(int,input().split())
print(binomial(n,k) % 10007 )

