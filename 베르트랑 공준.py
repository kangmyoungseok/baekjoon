import math

def is_prime(p):
    for i in range(2,int(math.sqrt(p))+1):
        if p % i == 0:
            return False
    return True

prime = []

for i in range(2,123456*2+1):
    if is_prime(i) :
        prime.append(i)

while True:
    N = int(input())
    if N == 0 :
        break
    
    count = 0
    for i in prime:
        if i > N and i <= 2*N:
            count +=1
    print(count)
    