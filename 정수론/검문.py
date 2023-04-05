N = int(input())

def gcd(a,b):
    if b>a:
        a,b = b,a
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

arr = []
for i in range(N):
    arr.append(int(input()))
# 각각의 숫자들의 차이를 배열에 저장
arr.sort()

diff = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        diff.append(arr[j]-arr[i])

# diff들의 최대 공약수를 구한다.
gcd_val = diff[0]
for i in range(1,len(diff)):
    gcd_val = gcd(diff[i],gcd_val)

# gcd_val의 약수들을 구한다
result = set()
for i in range(2,int(gcd_val**0.5)+1):
    if gcd_val % i == 0:
        result.add(i)
        result.add(int(gcd_val//i))
result.add(gcd_val)
result = sorted(list(result))
result = map(str,result)

print(' '.join(result))
