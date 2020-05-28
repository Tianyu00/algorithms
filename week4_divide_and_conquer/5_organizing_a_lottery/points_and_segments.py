# reference: https://towardsdatascience.com/course-1-algorithmic-toolbox-part-3-divide-and-conquer-dd9022bfa2c0

# Uses python3
import sys
import numpy as np
import math

def binary_search(a, x):
        left, right = 0, len(a) - 1
        if x < a[0] or x > a[-1]:
            return -1
        else:
            while left <= right:
                middle = math.floor((left+right)/2)
                if x == a[middle]:
                    return middle
                elif x > a[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            return -1

def fast_count_segments(starts, ends, points):
    cnt = []
    ss = [(int(x), 1) for x in starts]
    ee = [(int(x), 3) for x in ends]
    pp = [(int(x), 2) for x in points]
    ll = np.array(ss + ee + pp, dtype = [('A', 'int'), ('B', 'int')])
    ord = np.lexsort((ll['B'], ll['A']))
    ll = ll[ord]
    count = 0
    ord2 = np.array(points).argsort().argsort()
    for i in range(len(ll)):
        if ll[i][1] == 2:  # points
            cnt.append(count) 
        elif ll[i][1] == 1:  # starts
            count += 1
        elif ll[i][1] == 3:  # ends
            count -= 1
    cnt = np.array(cnt)[ord2]
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
