import sys

def recursion(s, l, r,depth):
    if l >= r: return (1,depth+1)
    elif s[l] != s[r]: return (0,depth+1)
    else: return recursion(s, l+1, r-1,depth+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)

N = int(input())

for i in range(N):
    result = isPalindrome(sys.stdin.readline().strip())
    print(f"{result[0]} {result[1]}" )

