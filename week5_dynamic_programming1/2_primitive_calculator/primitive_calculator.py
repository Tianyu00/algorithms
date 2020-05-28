# Uses python3
import sys
import numpy as np

def optimal_sequence(n):
    s=[]
    s.append(0)
    s.append(1)
    s.append(1)
    s.append(1)
    s.append(2)
    v = []
    v.append(0)
    v.append(0)
    v.append(1)
    v.append(1)
    v.append(2)
    i = 5
    while i <= n:
        v1 = v[i//2] if not(bool(i%2)) else np.Inf
        v2 = v[i//3] if not(bool(i%3)) else np.Inf
        v3 = v[-1]
        v_min = min(v1, v2, v3) 
        v.append(v_min+1)
        if v_min == v1:
            s.append(i//2)
        elif v_min == v2:
            s.append(i//3)
        elif v_min == v3:
            s.append(i-1)
        i += 1
    ss = [n]
    while not(ss[-1] == 1):
        ss.append(s[ss[-1]])
    #print('v',v)
    #print('s',s)
    return sorted(ss)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)


    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
