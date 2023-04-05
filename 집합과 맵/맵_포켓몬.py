import sys
import string

N,M = map(int,sys.stdin.readline().split())

poc_list = []
poc_dic = {}
poc_list.append(0)
count = 0
for i in range(N):
    count +=1
    poc = sys.stdin.readline().rstrip()
    poc_dic[poc] = count
    poc_list.append(poc)

for j in range(M):
    search = sys.stdin.readline().rstrip()
    if search[0] in string.digits:
        result = poc_list[int(search)]
    else:
        result = poc_dic[search]
    print(result)
