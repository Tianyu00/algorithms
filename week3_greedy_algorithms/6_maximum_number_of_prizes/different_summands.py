# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    number = 1
    if n == 1: return [1]
    while n > 2*number:
        n -= number
        summands.append(number)
        number += 1
    summands.append(n)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
