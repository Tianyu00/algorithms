# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    if n == 2:
        return 1
    fn = []
    fn.append(0)
    fn.append(1)
    fn.append(1)
    while not((fn[-2] == fn[0]) & (fn[-1] == fn[1])):
        fn.append( (fn[-1]+fn[-2]) % m)
    length = len(fn) - 2
    return fn[n % length]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
