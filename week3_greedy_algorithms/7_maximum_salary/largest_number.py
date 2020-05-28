#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ''
    while len(a) > 0:
        max = '0'
        max_idx = '-1'
        for idx, i in enumerate(a):
            if int(i + max) >= int(max + i):
                max = i
                max_idx = idx
        res += a[max_idx]
        del a[max_idx]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
