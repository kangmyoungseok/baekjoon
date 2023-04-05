
M = 1234567891

def hashing(s):
    result = 0
    for i in range(len(s)):
        num = ord(s[i]) - ord('a') + 1
        result += num * pow(31,i,M)

    return result % M

_ = input()
s = input()

print(hashing(s))
