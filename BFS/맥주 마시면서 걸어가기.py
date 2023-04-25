import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    visited = []
    N = int(input())
    start_x,start_y = map(int,input().split())
    for i in range(N):
        x,y = map(int,input().split())
        visited.append({'x':x,'y':y,})
