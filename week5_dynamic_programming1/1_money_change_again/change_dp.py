# Uses python3
import sys

def get_change(m):
    v = []
    v.append(0)
    v.append(1)
    v.append(2)
    v.append(1)
    v.append(1)
    while (len(v)-1 < m):
        v.append(min(v[-1], v[-3], v[-4])+1)
    return v[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
