# reference: https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0

# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left == 0:
        return 0
    if right - left == 1:
        return int(a[left] > a[right])
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
    #write your code here
    a[left:(ave+1)] = sorted(a[left:(ave+1)])
    a[(ave+1):(right+1)] = sorted(a[(ave+1):(right+1)])
    i = left
    j = ave + 1
    while (i <= ave) & (j <= right):
        if a[i]<=a[j]:
            i += 1
        else:
            j += 1
            number_of_inversions += ave-i+1
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = list(input.split())
    b = len(a) * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
