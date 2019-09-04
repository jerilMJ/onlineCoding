''' Solution for 'Symmetric Difference' under Python in HackerRank '''

a = int(input())
set_1 = set(input().split(' '))
b = int(input())
set_2 = set(input().split(' '))     # No need for a and b since they're not used.
                                    # They're just to bypass the question parameters.
set_3 = []
for x in set_1:
    if x not in set_2:              # If x is in both sets, it is removed from second                                        # set. Else, it is taken in the third set.
        set_3.append(x)
    else:
        set_2.remove(x)             
set_3.extend(set_2)                 # Now Remaining elements are appended since they're 
set_3 = list(map(int, set_3))       # unique.
set_3.sort()
for x in set_3:
    print(x)
