# Uses python3
import numpy as np

def edit_distance(s, t):
    n = len(s)
    m = len(t)
    D = np.zeros(shape = (n+1, m+1))
    D[:,0] = [i for i in range(n+1)]
    D[0,:] = [j for j in range(m+1)]
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = D[i, j-1] + 1
            deletion = D[i-1, j] + 1
            match = D[i-1, j-1]
            mismatch = D[i-1, j-1] + 1
            if s[i-1] == t[j-1]:
                D[i,j] = min(insertion, deletion, match)
            else:
                D[i,j] = min(insertion, deletion, mismatch)
    return int(D[n,m])



if __name__ == "__main__":
    print(edit_distance(input(), input()))
