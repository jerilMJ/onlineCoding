''' Solution to 'Check Strict Superset' under Python in HackerRank '''
mainSet = set(input().split())
n = int(input())
checkSets = []
for _ in range(n):
    checkSets.append(set(input().split()))
flag = 0

for x in checkSets:
    if len(x - mainSet) == 0 and len(mainSet - x) != 0:
        continue
    else:
        flag = 1
        break

print(True) if flag == 0 else print(False)


