K = int(input())

s = []
row = []
col = []
for i in range(6):
    dir,dist = map(int,input().split())
    s.append([dir,dist])
    if dir == 1 or dir == 2:
        row.append(dist)
    else:
        col.append(dist)

result = []
for i in range(6):
    if s[i][0] == s[(i+2)%6][0]:
        result.append(s[(i+1)%6][1])

small_square = result[0] * result[1]
big_square = max(row) * max(col)

print(K * (big_square-small_square))
    