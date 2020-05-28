# Uses python3
import sys

def gcd(a, b):
    a,b = max(a,b), min(a,b)
    a,b = b, a % b
    while b != 0:
        a,b = b, a%b
    return a


def lcm_naive(a, b):
    gcd1 = gcd(a,b)

    return round(gcd1*(a/gcd1)*(b/gcd1))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

