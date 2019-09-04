''' Solution for 'Exceptions' under Python in HackerRank '''

how_many = int(input())
results = []
for i in range(how_many):
    a, b = tuple(input().split())
    try:
        results.append(int(int(a)/int(b)))
    except ZeroDivisionError:
        results.append('Error Code: integer division or modulo by zero')
    except ValueError as e:
        results.append('Error Code: ' + str(e))
    
for res in results:
    print(res)