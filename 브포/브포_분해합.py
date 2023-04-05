N = int(input())

min = 1
if N > 100:
    min = N - 100

result = 0
for i in range(min,N+1):
    tmp = str(i)
    sum = i
    for j in tmp:
        sum += int(j)
    if sum == N:
        result = i
        break

print(result)


