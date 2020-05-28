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


def fibonacci_partial_sum_naive(m, n):
    if m == 0:
        return fibonacci_sum_naive(n)
    return (fibonacci_sum_naive(n) - fibonacci_sum_naive(m-1)) % 10 


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
