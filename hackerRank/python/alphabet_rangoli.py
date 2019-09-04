''' 
    My Solution to 'Alphabet Rangoli' under Python in HackerRank 
    First of all, I thought this had to be done with matrices.. so I took a huge chunk out of my time to get it done the matrix way.. I didn't think about strings.. 
    that's what happens when you do challenges randomly..

    Anyway, here's my code: It's kinda large, messy and not so elegant..
	
    1. Idea is to first make a matrix filled with '-'
    2. Then make required alphabet list.
    3. Fill in the middle column upto half.
    4. Then fill both sides of the top-half and then fill the bottom half by copying the top half.
'''

def display_matrix(mat, r, c):
    for i in range(c):
        for j in range(r):
            print(mat[i][j], end = '')
        print()
    return


def print_rangoli(size):
    columns = size*2 - 1
    rows = columns*2 - 1

# Creating list of needed alphabets
    asciis = list(range(ord('a'), ord('z')+1))
    alphabets = list(map(chr, asciis))[0:size]
    alphabets.reverse()

# Creating matrix and filling it with '-'
    filler = list('-'*rows)
    matrix = []
    for _ in range(columns):
        matrix.append(filler[:]) 

# Finding how middle row of the final result should be
    midRow = []
    midRow.extend(alphabets[:]+list(reversed(alphabets))[1:])

# Filling middle column as referenced by step 3
    midIndex = int((rows-1)/2)
    for i in range(int((columns-1)/2)+1):
        matrix[i][midIndex] = midRow[i]

# filling right of middle column
    midIndex = int((rows-1)/2)
    for i in range(1, size):
        midIndex = int((rows-1)/2)
        charAtMidOfRow = matrix[i][midIndex]
        for j in range(1,i+1):
            midIndex+=2
            matrix[i][midIndex] = midRow[midRow.index(charAtMidOfRow)-j]

# filling left of middle column
    midIndex = int((rows-1)/2)
    for i in range(1, size):
        midIndex = int((rows-1)/2)
        charAtMidOfRow = matrix[i][midIndex]
        for j in range(1,i+1):
            midIndex-=2
            matrix[i][midIndex] = midRow[midRow.index(charAtMidOfRow)-j]

# filling bottom half
    mid = int((columns-1)/2)
    for counter, item in enumerate(matrix[mid+1:]):
        matrix[matrix.index(item)] = matrix[mid-(counter+1)]

    display_matrix(matrix, rows, columns)

if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
