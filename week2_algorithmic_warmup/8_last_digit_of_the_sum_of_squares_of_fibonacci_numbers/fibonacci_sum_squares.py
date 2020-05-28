# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 2:
        return n
    fn = []
    m = 10
    fn.append(0)
    fn.append(1)
    fn.append(1)
    while not((fn[-2] == fn[0]) & (fn[-1] == fn[1])):
        fn.append( (fn[-1]+fn[-2]) % m)
    del fn[-1]
    del fn[-1]
    length = len(fn)
    return (sum([item**2 for item in fn])*(n//length) + \
            sum([item**2 for item in fn[:(n%length+1)]])) % 10




if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
