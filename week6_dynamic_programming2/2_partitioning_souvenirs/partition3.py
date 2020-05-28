# reference: https://stackoverflow.com/questions/4803668/3-partition-problem
# reference: https://github.com/anoubhav/Coursera-Algorithmic-Toolbox/blob/master/assignment%20solutions/6.2%20partition%20souvenirs.py

# Uses python3
import sys
import itertools
import numpy as np

def partition3(A):
    count = 0
    W = sum(A)
    if W % 3 != 0:
        return 0
    if max(A) > (W/3):
        return 0
    n = len(A)
    value = np.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
           value[i][j] = value[i][j-1]
           if A[j-1] <= i:
               temp = value[i-A[j-1]][j-1] + A[j-1]
               if temp > value[i][j]:
                   value[i][j] = temp
    if_partition3 = (W//3 in value[W//3]) and (W//3*2 in value[W//3*2])
    return int(if_partition3)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

