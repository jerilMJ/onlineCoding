''' Solution to 'Collections.OrderedDict()' under Python in HackerRank '''

from collections import OrderedDict

items = OrderedDict()
n = int(input())

for _ in range(n):
    item = input().split()
    price = item[-1]
    name = ' '.join(item[:-1])
    if name in items.keys():
        items[name] += int(price) 
    else:
        items[name] = 0
        items[name] += int(price) 

for i in range(len(items.keys())):
    print(list(items.items())[i][0], list(items.items())[i][1])

