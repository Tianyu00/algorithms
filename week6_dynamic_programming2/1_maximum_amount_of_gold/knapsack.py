# Uses python3
import sys

def optimal_weight(W, w):
    D = [[0]*(W+1) for i in range(len(w)+1)]
    for i in range(1,len(w)+1):
        for j in range(1, W+1):
            if j < w[i-1]: 
                D[i][j] = D[i-1][j]
            else:
                D[i][j] = max(D[i-1][j], D[i-1][j-w[i-1]]+w[i-1])
    return D[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
