N = int(input())

# 트리 만들기
tree = [[] for _ in range(N+1)]

def convert_idx(a):
    return int(ord(a) - ord('A'))

for i in range(N):
    root,left,right = input().split()
    tree[convert_idx(root)] = [left,right]

pre_result=''
def pre_order(root):
    global pre_result
    pre_result += root
    node = tree[convert_idx(root)]
    if(node[0] != '.'):
        pre_order(node[0])
    if(node[1] != '.'):
        pre_order(node[1])

in_result = ''
def in_order(root):
    global in_result
    node = tree[convert_idx(root)]
    if node[0] != '.':
        in_order(node[0])
    in_result += root
    if node[1] != '.':
        in_order(node[1])

post_result = ''
def post_order(root):
    global post_result
    node = tree[convert_idx(root)]
    if node[0] != '.':
        post_order(node[0])
    if node[1] != '.':
        post_order(node[1])
    post_result += root

    

pre_order('A')
in_order('A')
post_order('A')
print(pre_result)
print(in_result)
print(post_result)