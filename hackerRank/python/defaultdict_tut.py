''' Solution to 'DefaultDict Tutorial' under Python in HackerRank '''

from collections import defaultdict
n, m = tuple(map(int, input().split()))
li1 = []
li2 = defaultdict(lambda: [-1])
li = []
for i in range(n):
    x = input()
    li1.append(x)
    li2[x].append(i+1)
    try:
        li2[x].remove(-1)
    except:
        continue

for i in range(m):
    x = input()
    li.append(li2[x])

for x in li:
    print(*x, sep = ' ')
