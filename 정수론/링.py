N = int(input())

def euclid_gcd(n,m):
    if m > n :
        n,m = m,n
    if m % n == 0:
        return n
    else:
        return euclid_gcd(m,n%m)

arr = list(map(int,input().split()))
ring = arr[0]

for i in range(1,len(arr)):
    gcd = euclid_gcd(ring,arr[i])
    boonja = int(ring // gcd)
    boonmo = int(arr[i] // gcd )
    print(f"{boonja}/{boonmo}")
