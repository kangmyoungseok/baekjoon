# 2,5 의 개수를 다 구하면 되는디..

N = int(input())

def get_two(n):
    result = 0
    while n % 2 == 0:
        result += 1
        n //=2
    return result

def get_five(n):
    result = 0
    while n % 5 == 0:
        result += 1
        n //=5
    return result

count_2 = 0
count_5 = 0
for i in range(1,N+1):
    count_2 += get_two(i)
    count_5 += get_five(i)

# 
print(min(count_2,count_5))
