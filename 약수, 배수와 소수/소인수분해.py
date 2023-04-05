import math

N = int(input())

i = 3
prime_factor = {}

# 1. 2로 나누어지면 2로 나누기
count = 0
while N % 2 == 0:
    count += 1
    N = N // 2
if count > 0:
    prime_factor[2] = count

square = int(math.sqrt(N))
i = 3

while i <= square:
    if N % i == 0:
        count = 0
        while N % i == 0:
            count += 1
            N = N // i
        prime_factor[i] = count
    i += 2

if N != 1:
    prime_factor[N] = 1

for key,value in prime_factor.items():
    for i in range(value):
        print(key)
