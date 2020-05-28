# Uses python3
import sys
from random import randint
import math

def get_majority_element(a, left, right):
    a.sort()
    for i in range(math.ceil(right/2)):
        if a[i] == a[i+ math.floor(right/2)]:
            return 1
    return -1


def get_majority_element1(a, left, right):
    if n <= 1:
        return -1
    if n == 2:
        if a[0] == a[1]:
            return 1
        else: return -1
    candidate = []
    if right % 2 == 0:
        for i in range(int(right / 2)):
            if a[i*2] == a[i*2+1]:
                candidate.append(a[i*2])
    else:
        for i in range(int(right // 2 - 1)):
            if a[i*2] == a[i*2+1]:
                candidate.append(a[i*2])
        if (a[-1] == a[-2]) or (a[-1] == a[-3]):
            candidate.append(a[-1])
        elif (a[-2] == a[-3]):
            candidate.append(a[-2])
    for candidate_i in candidate:
        count = sum([1 if a_i == candidate_i else 0 for a_i in a])
        if count > right/2:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # while True:
      #  nn = randint(1,10)
       # a = [randint(0,10) for i in range(nn)]
        #n = len(a)
        #print(a)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
