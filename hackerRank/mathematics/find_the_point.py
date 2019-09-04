''' Solution to 'Find the point' under Mathematics in HackerRank '''

import os


def findPoint(px, py, qx, qy):
    rx = qx - px + qx if px < qx else qx - (px - qx)
    ry = qy - py + qy if py < qy else qy -(py - qy)
    return [rx, ry]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
