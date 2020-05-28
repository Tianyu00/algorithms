# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    v_over_w = np.array([v / w for v, w in zip(values, weights)])
    idx = v_over_w.argsort()[::-1]
    for i in idx:
        add_weight = min(capacity, weights[i])
        value += add_weight * v_over_w[i]
        capacity -= add_weight
    return round(value,4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
