#Uses python3

import sys

def lcs3(a, b, c):
    n1 = len(a)
    n2 = len(b)
    n3 = len(c)
    D = [[[1]*(n3+1) for j in range(n2+1)] for i in range(n1+1)]
    for i in range(n1+1):
        D[i][0][0] = 0
    for i in range(n2+1):
        D[0][i][0] = 0
    for i in range(n3+1):
        D[0][0][i] = 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            for k in range(1, n3+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(D[i-1][j][k],
                                     D[i][j-1][k],
                                     D[i][j][k-1])
    return D[n1][n2][n3]




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
