# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    if tank <  max(max([ s1-s2 for s1, s2 in zip(stops[1:],stops[:-1])]),stops[0], distance - stops[-1]):
        return -1
    n_refill = 0
    current = 0
    last_refill = 0
    stops.append(distance)
    while current < distance:
        next_stop = stops.pop(0)
        if next_stop - last_refill > tank:
            last_refill = current
            n_refill += 1
        current = next_stop
    return n_refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
