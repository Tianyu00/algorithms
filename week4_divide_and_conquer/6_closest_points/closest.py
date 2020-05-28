#Uses python3
import sys
import math
import numpy as np
import random

def dist(x,y):
    a = np.array([x[0], y[0]])
    b = np.array([x[1], y[1]])
    return math.sqrt(sum((a-b)**2))

def minimum_distance(x, y):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    if n == 0:
        return np.Inf
    if n == 1:
        return np.Inf
    if n == 2:
        return dist(x,y)
    if n in range(3, 6):
        m = np.Inf
        for i in range(n):
            for j in range(i+1,n):
                m = min(m, dist([x[i],x[j]], [y[i],y[j]]))
        return m
    xs = np.array(sorted(x))
    xs_to_x = x.argsort().argsort()
    ys = np.array(sorted(y))
    ys_to_y = y.argsort().argsort()
    x1 = np.array([1]*(n//2) + [0]*(n-n//2))
    x2 = np.array([0]*(n//2-2) + [1]*(n+2-n//2))
    y1 = np.array([1]*(n//2) + [0]*(n-n//2))
    y2 = np.array([0]*(n//2-2) + [1]*(n+2-n//2))
    m1 = x1[xs_to_x] * y1[ys_to_y]
    m2 = x1[xs_to_x] * y2[ys_to_y]
    m3 = x2[xs_to_x] * y1[ys_to_y]
    m4 = x2[xs_to_x] * y2[ys_to_y]
    m1 = [bool(i) for i in m1]
    m2 = [bool(i) for i in m2]
    m3 = [bool(i) for i in m3]
    m4 = [bool(i) for i in m4]
    # print(m1,m2,m3,m4)
    m1 = minimum_distance(x[m1],y[m1]) 
    m2 = minimum_distance(x[m2],y[m2])
    m3 = minimum_distance(x[m3],y[m3])
    m4 = minimum_distance(x[m4],y[m4])
    return round(min(m1, m2, m3, m4),4)

def naive(x,y):
    n = len(x)
    m = np.Inf
    for i in range(n):
        for j in range(i+1, n):
            m = min(m, dist([x[i],x[j]], [y[i],y[j]]))
    return m

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    #while True:
       # n = random.randint(2,1000)
      #  x = [random.randint(-10000,10000) for i in range(n)]
     #   y = [random.randint(-10000,10000) for i in range(n)]
    #    print(x)
   #     print(y)
    print("{0:.9f}".format(minimum_distance(x, y)))
  #      res1 = naive(x,y)
 #       res2 = minimum_distance(x,y)
#        if res1 != res1:
#            print('wrong')
#            print(res1, res2)
