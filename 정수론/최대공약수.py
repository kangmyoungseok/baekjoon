def gcd(x,y):
    divisor = [1,x]
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            divisor.append(i)
            divisor.append(x//i)
    divisor.sort()
    

    for i in divisor[::-1]:
        if y % i == 0:
            return i



def lcm(gcd,x,y):
    return int(x // gcd) * y

x,y = map(int,input().split())

a = gcd(x,y)
b = lcm(a,x,y)
print(a)
print(b)