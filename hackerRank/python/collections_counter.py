''' Solution to 'collections.Counter()' under Python in HackerRank'''
# No need for using Counter. It makes the program slow

shoes_quantity = input()
available_sizes = input().split()
customers_quantity = int(input())

total = 0

for _ in range(customers_quantity):
    size, price = tuple(input().split())
    try:
        available_sizes.remove(size)
        total += int(price)
    except:
        continue

print(total)

