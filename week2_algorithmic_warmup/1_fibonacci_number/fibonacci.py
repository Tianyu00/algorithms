# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n
    else :
        fn = []
        fn.append(0)
        fn.append(1)
        for i in range(2,n+1):
            fn.append(fn[-1] + fn[-2])
        return fn.pop()

n = int(input())
print(calc_fib(n))
