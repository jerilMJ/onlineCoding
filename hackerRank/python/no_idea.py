''' Solution to 'No Idea!' under Python in HackerRank '''

from itertools import filterfalse

n, m = tuple(input().split())
arr = input().split()
clone = arr[:]
A = set(input().split())
B = set(input().split())
happiness = 0

clone = filterfalse(lambda x: x not in A, arr)
happiness += len(list(clone))
clone = arr[:]
clone = filterfalse(lambda x: x not in B, arr)
happiness -= len(list(clone))

print(happiness)
