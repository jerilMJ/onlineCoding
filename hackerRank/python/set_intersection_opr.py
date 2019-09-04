''' Solution to 'Set.intersection() Operation' under Python in HackerRank '''

e = int(input())
english = set(input().split())
f = int(input())
french = set(input().split())

print(len(english.intersection(french)))
