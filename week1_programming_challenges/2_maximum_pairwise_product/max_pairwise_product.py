# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max1 = 0
    max1_idx = 0
    max2 = 0
    max2_idx = 0
    for idx, number in enumerate(numbers):
        if number > max1:
            max1 = number
            max1_idx = idx
    for idx, number in enumerate(numbers):
        if (number > max2) & (idx != max1_idx):
            max2 = number
            max2_idx = max2_idx
    return max1 * max2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
