# Uses python3
import numpy as np
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def is_operator(x):
    return (x == '+' or x == '-' or x == '*')

def MinAndMax(i,j, m, M, ops):
    mi = 999
    ma = -999
    for k in range(i, j):
        a = evalt(M[i,k],M[k+1,j],ops[k-1])
        b = evalt(M[i,k], m[k+1,j], ops[k-1])
        c = evalt(m[i,k], M[k+1,j], ops[k-1])
        d = evalt(m[i,k], m[k+1,j], ops[k-1])
        mi = min(mi, a,b,c,d)
        ma = max(ma, a,b,c,d)
    return mi, ma

def get_maximum_value(dataset):
    #write your code here
    num_tmp = ''
    num = []
    ops = []
    for i in range(len(dataset)):
        if is_operator(dataset[i]): 
            ops.append(dataset[i])
            num.append(int(num_tmp))
            num_tmp = ''
        else:
            num_tmp += dataset[i]
    num.append(int(num_tmp))
    if len(ops) == 1:
        return evalt(num[0], num[1], ops[0]) 
    n = len(num)
    m = np.zeros((n+1, n+1)) 
    M = np.zeros((n+1,n+1))
    for i in range(1,n+1): m[i,i] = num[i-1];M[i,i] = num[i-1]
    for s in range(1,n):
        for i in range(1, n-s+1):
            j = i+s
            m[i,j], M[i,j] = MinAndMax(i,j,m,M,ops)
    return int(M[1,n])


if __name__ == "__main__":
    print(get_maximum_value(input()))
