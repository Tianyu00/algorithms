# Uses python3
import sys

def fibonacci_sum_naive(n):
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
    return (sum(fn)*(n//length) + sum(fn[:(n%length+1)])) % 10



def a_fibonacci_sum_naive(n):
    if n <= 1:
        return n
    if n == 2:
        return 2

    previous = 0
    current  = 1
    sum = 0

    for i in range(2, n+1):
        previous, current, sum = current % 10, (previous + current) % 10, (sum + current) % 10
    return (sum + current) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
