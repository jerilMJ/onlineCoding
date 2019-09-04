''' Solution to 'Collections.deque()' under Python in HackerRank'''

from collections import deque

dq = deque()
n = int(input())
for _ in range(n):
    opr, *num = tuple(input().split())
    try:
        getattr(dq, opr)(num[0])
    except:
        getattr(dq, opr)()

print(*list(dq), sep = ' ')


