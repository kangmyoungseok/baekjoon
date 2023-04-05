def count_two(n):
    count = 0
    while n >= 2:
        count += n // 2 
        n //=2
    return count

def count_five(n):
    count = 0
    while n >=5 :
        count += n // 5
        n //=5
    return count

n,m = map(int,input().split())
total_two = count_two(n) - count_two(n-m) - count_two(m)
total_five = count_five(n) - count_five(n-m) - count_five(m)
print(min(total_two,total_five))
