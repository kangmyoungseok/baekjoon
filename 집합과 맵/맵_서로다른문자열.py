S = input()

dic = {}
for i in range(len(S)):
    for j in range(i+1,len(S)+1):
        dic[S[i:j]] = 1
    
print(len(dic))
