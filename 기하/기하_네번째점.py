coor_x = []
coor_y = []

for i in range(3):
    x,y = map(int,input().split())
    coor_x.append(x)
    coor_y.append(y)

result_x,result_y = 0,0
if coor_x[0] == coor_x[1]: result_x = coor_x[2]
elif coor_x[0] == coor_x[2]: result_x = coor_x[1]
else: result_x = coor_x[0]

if coor_y[0] == coor_y[1]: result_y = coor_y[2]
elif coor_y[0] == coor_y[2]: result_y = coor_y[1]
else: result_y = coor_y[0]

print(f"{result_x} {result_y}")