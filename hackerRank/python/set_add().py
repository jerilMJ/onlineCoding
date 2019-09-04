''' Solution to "Set.add()" under Python in HackerRank '''

n = int(input())
stamps = set()
for i in range(n):
    stamps.add(input())
print(len(stamps))

