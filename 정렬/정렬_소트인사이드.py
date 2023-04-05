N = input()

arr = [0 for x in range(10)]

for i in N:
    arr[int(i)] +=1

result = ''
for idx in range(9,-1,-1):
    result += str(idx) * arr[idx]

print(result)