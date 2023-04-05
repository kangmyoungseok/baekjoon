import sys

input = sys.stdin.readline

sudoku = []

# 스도쿠 채우기
for i in range(9):
    sudoku.append(list(map(int,input().split())))

# 공백 찾기
blank = []
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == 0:
            blank.append([row,col])

def checkRow(x,y,i):
    for j in range(9):
        if sudoku[x][j] == i:
            return False
    return True

def checkCol(x,y,i):
    for j in range(9):
        if sudoku[j][y] == i:
            return False
    return True

def checkSquare(x,y,i):
    base_x = int(x//3)
    base_y = int(y//3)
    for row in range(3):
        for col in range(3):
            if sudoku[base_x*3 + row][base_y*3 + col] == i:
                return False
    return True

# 검증 함수
def check(x,y,val):
    if checkRow(x,y,val) and checkCol(x,y,val) and checkSquare(x,y,val):
        return True
    return False

def dfs(i):
    if len(blank) == i:
        for idx in range(9):
            print(' '.join(map(str,sudoku[idx])))
        sys.exit()
    
    x,y = blank[i]
    for val in range(1,10):
        if check(x,y,val):
            sudoku[x][y] = val
            dfs(i+1)
            sudoku[x][y] = 0
        
dfs(0)
