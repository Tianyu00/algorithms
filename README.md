# Implementing Common Algorithms

The problems here come from coursera course 'Algorithm toolbox'.

They include problems about [Greedy Algorithms](#week-3-greedy-algorithms), [Divide and Conquer](#week-4-divide-and-conquer), Dynamic Programming [1](#week-5-dynamic-programming1), [2](#week-5-dynamic-programming2), and some other problems [week1](#week-1-programming-challenges), [week2](#week-2-algorithmic-warmup). The solutions are all original.

### week 1 programming challenges

- [sum_of_two_digits](week1_programming_challenges/1_sum_of_two_digits/APlusB.py)
- [maximum_pairwise_product](week1_programming_challenges/2_maximum_pairwise_product/max_pairwise_product.py)

### week 2 algorithmic warmup
[detailed problem description](week2_algorithmic_warmup/week2_algorithmic_warmup.pdf)

#### 1 [Fibonacci Number](week2_algorithmic_warmup/1_fibonacci_number/fibonacci.py)

Given an integer <img src="https://latex.codecogs.com/gif.latex?n">, find the 𝑛th Fibonacci number <img src="https://latex.codecogs.com/gif.latex?F_n">.

#### 2 [Last Digit of a Large Fibonacci Number](week2_algorithmic_warmup/2_last_digit_of_fibonacci_number/fibonacci_last_digit.py)

Given an integer <img src="https://latex.codecogs.com/gif.latex?n">, find the last digit of the <img src="https://latex.codecogs.com/gif.latex?n">th Fibonacci number.

#### 3 [Greatest Common Divisor](week2_algorithmic_warmup/3_greatest_common_divisor/gcd.py)

Given two integers <img src="https://latex.codecogs.com/gif.latex?a"> and <img src="https://latex.codecogs.com/gif.latex?b">, find their greatest common divisor.

#### 4 [Least Common Multiple](week2_algorithmic_warmup/4_least_common_multiple/lcm.py)

Given two integers <img src="https://latex.codecogs.com/gif.latex?a"> and <img src="https://latex.codecogs.com/gif.latex?b">, find their least common multiple.

#### 5 [Fibonacci Number Again](week2_algorithmic_warmup/5_fibonacci_number_again/fibonacci_huge.py)

Given two integers <img src="https://latex.codecogs.com/gif.latex?n"> and <img src="https://latex.codecogs.com/gif.latex?m">, output <img src="https://latex.codecogs.com/gif.latex?F_n"> mod <img src="https://latex.codecogs.com/gif.latex?m"> (that is, the remainder of <img src="https://latex.codecogs.com/gif.latex?F_n"> when divided by <img src="https://latex.codecogs.com/gif.latex?m">).

#### 6 [Last Digit of the Sum of Fibonacci Numbers](week2_algorithmic_warmup/6_last_digit_of_the_sum_of_fibonacci_numbers/fibonacci_sum_last_digit.py)

Given an integer <img src="https://latex.codecogs.com/gif.latex?n">, find the last digit of the sum 
<img src="https://latex.codecogs.com/gif.latex?F_1&plus;F_2&plus;%5Ccdots&plus;F_n">.

#### 7 [Last Digit of the Sum of Fibonacci Numbers Again](week2_algorithmic_warmup/7_last_digit_of_the_sum_of_fibonacci_numbers_again/fibonacci_partial_sum.py)

Given two non-negative integers <img src="https://latex.codecogs.com/gif.latex?m"> and <img src="https://latex.codecogs.com/gif.latex?n">, where <img src="https://latex.codecogs.com/gif.latex?m"> ≤ <img src="https://latex.codecogs.com/gif.latex?n">, find the last digit of the sum <img src="https://latex.codecogs.com/gif.latex?F_n">.

#### 8 [Last Digit of the Sum of Squares of Fibonacci Numbers](week2_algorithmic_warmup/8_last_digit_of_the_sum_of_squares_of_fibonacci_numbers/fibonacci_sum_squares.py)

Compute the last digit of <img src="https://latex.codecogs.com/gif.latex?F_1%5E2&plus;F_2%5E2&plus;%5Ccdots&plus;F_n%5E2">.

### week 3 greedy algorithms
[detailed problem description](week3_greedy_algorithms/week3_greedy_algorithms.pdf)

#### 1 [Money Change](week3_greedy_algorithms/1_money_change/change.py)

The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

#### 2 [Maximum Value of the Loot](week3_greedy_algorithms/2_maximum_value_of_the_loot/fractional_knapsack.py)

The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

Input: The first line of the input contains the number <img src="https://latex.codecogs.com/gif.latex?n"> of items and the capacity <img src="https://latex.codecogs.com/gif.latex?W"> of a knapsack. The next <img src="https://latex.codecogs.com/gif.latex?n"> lines define the values and weights of the items. The <img src="https://latex.codecogs.com/gif.latex?i">-th line contains integers <img src="https://latex.codecogs.com/gif.latex?v_i"> and <img src="https://latex.codecogs.com/gif.latex?w_i">—the value and the weight of <img src="https://latex.codecogs.com/gif.latex?i">-th item, respectively.

Output: Output the maximal value of fractions of items that fit into the knapsack

#### 3 [Car Fueling](week3_greedy_algorithms/3_car_fueling/car_fueling.py)

You are going to travel to another city that is located <img src="https://latex.codecogs.com/gif.latex?d"> miles away from your home city. Your car can travel at most <img src="https://latex.codecogs.com/gif.latex?m"> miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1, stop2, . . . , stopn from your home city. What is the minimum number of refills needed?

#### 4 [Maximum Advertisement Revenue](week3_greedy_algorithms/4_maximum_advertisement_revenue/dot_product.py)

Given two sequences <img src="https://latex.codecogs.com/gif.latex?a_1%2Ca_2%2C...%2Ca_n">, (<img src="https://latex.codecogs.com/gif.latex?a_i"> is the profit per click of the <img src="https://latex.codecogs.com/gif.latex?i">-th ad) and <img src="https://latex.codecogs.com/gif.latex?b_1%2Cb_2%2C...%2Cb_n"> (<img src="https://latex.codecogs.com/gif.latex?b_i"> is the average number of clicks per day of the <img src="https://latex.codecogs.com/gif.latex?i">-th slot), we need to partition them into 𝑛 pairs (<img src="https://latex.codecogs.com/gif.latex?a_i%2Cb_i">) such that the sum of their products is maximized.

#### 5 [Collecting Signatures](week3_greedy_algorithms/5_collecting_signatures/covering_segments.py)

Given a set of <img src="https://latex.codecogs.com/gif.latex?n"> segments <img src='https://latex.codecogs.com/gif.latex?%7B%5Ba_0%2Cb_0%5D%2C%5Ba_1%2Cb_1%5D%2C...%5Ba_%7Bn-1%7D%2Cb_%7Bn-1%7D%5D%7D'> with integer coordinates on a line, find the minimum number <img src="https://latex.codecogs.com/gif.latex?m"> of points such that each segment contains at least one point. That is, find a set of integers <img src="https://latex.codecogs.com/gif.latex?X"> of the minimum size such that for any segment <img src='https://latex.codecogs.com/gif.latex?%5Ba_i%2Cb_i%5D'> there is a point <img src='https://latex.codecogs.com/gif.latex?x%5Cin%20X'> such that <img src='https://latex.codecogs.com/gif.latex?a_i%5Cle%20x%5Cle%20b_i'>.

#### 6 [Maximum Number of Prizes](week3_greedy_algorithms/6_maximum_number_of_prizes/different_summands.py)

The goal of this problem is to represent a given positive integer <img src="https://latex.codecogs.com/gif.latex?n"> as a sum of as many pairwise distinct positive integers as possible. That is, to find the maximum <img src="https://latex.codecogs.com/gif.latex?k"> such that <img src="https://latex.codecogs.com/gif.latex?n"> can be written as <img src='https://latex.codecogs.com/gif.latex?a_1&plus;a_2&plus;%5Ccdots&plus;a_k'> where <img src='https://latex.codecogs.com/gif.latex?a_1%2C...%2Ca_k'> are positive integers and <img src='https://latex.codecogs.com/gif.latex?a_i%20%5Cne%20a_j'> for all <img src='https://latex.codecogs.com/gif.latex?1%20%5Cle%20i%3Cj%5Cle%20k'>.

#### 7 [Maximum Salary](week3_greedy_algorithms/7_maximum_salary/largest_number.py)

Compose the largest number out of a set of integers.

Say, input: 21, 2, output: 221.

### week 4 divide and conquer
[detailed problem description](week3_greedy_algorithms/week4_divide_and_conquer.pdf)

#### 1 [Binary Search](week4_divide_and_conquer/1_binary_search/binary_search.py)

The goal in this code problem is to implement the binary search algorithm.

#### 2 [Majority Element](week4_divide_and_conquer/2_majority_element/majority_element.py)

The goal in this code problem is to check whether an input sequence of length <img arc='https://latex.codecogs.com/gif.latex?n'> contains a majority element (an element that appears appears strictly more than <img arc='https://latex.codecogs.com/gif.latex?n/2'> times).

#### 3 [Improving Quick Sort](week4_divide_and_conquer/3_improving_quicksort/sorting.py)

To force the given implementation of the quick sort algorithm to efficiently process sequences with few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new partition procedure should partition the array into three parts: <img src='https://latex.codecogs.com/gif.latex?%3C%20x'> part, <img src='https://latex.codecogs.com/gif.latex?%3Dx'> part, and <img src='https://latex.codecogs.com/gif.latex?%3Ex'> part.

#### 4 [Number of Inversions](week4_divide_and_conquer/4_number_of_inversions/inversions.py)

The goal in this problem is to count the number of inversions of a given sequence. An inversion of a sequence <img src='https://latex.codecogs.com/gif.latex?a_0%2Ca_1%2C%5Ccdots%2Ca_%7Bn-1%7D'> is a pair of indices <img src='https://latex.codecogs.com/gif.latex?0%5Cle%20i%3Cj%3C%3Dn'> such that <img src='https://latex.codecogs.com/gif.latex?a_i%3Ea_j'>. The number of inversions of a sequence in some sense measures how close the sequence is to being sorted. 

#### 5 [Organizing a Lottery](week4_divide_and_conquer/5_organizing_a_lottery/points_and_segments.py)

You are given a set of points on a line and a set of segments on a line. The goal is to compute, for each point, the number of segments that contain this point.

#### 6 [Closest Points](week4_divide_and_conquer/6_closest_points/closest.py)

Given <img src='https://latex.codecogs.com/gif.latex?n'> points on a plane, find the smallest distance between a pair of two (different) points. 

### week 5 dynamic programming1
[detailed problem description](week3_greedy_algorithms/week5_dynamic_programming1.pdf)

#### 1 [Money Change Again](week5_dynamic_programming1/1_money_change_again/change_dp.py)

Your goal now is to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4. (discrete nnapsack problem with repetition)

#### 2 [Primitive Calculator](week5_dynamic_programming1/2_primitive_calculator/primitive_calculator.py)

You are given a primitive calculator that can perform the following three operations with the current number <img src='https://latex.codecogs.com/gif.latex?x'>: multiply <img src='https://latex.codecogs.com/gif.latex?x'> by 2, multiply <img src='https://latex.codecogs.com/gif.latex?x'> by 3, or add 1 to <img src='https://latex.codecogs.com/gif.latex?x'>. Your goal is given a positive integer <img src='https://latex.codecogs.com/gif.latex?n'>, find the minimum number of operations needed to obtain the number <img src='https://latex.codecogs.com/gif.latex?n'> starting from the number 1.

#### 3 [Edit Distance](week5_dynamic_programming1/3_edit_distance/edit_distance.py)

The goal of this problem is to implement the algorithm for computing the edit distance between two strings.

The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.

#### 4 [Longest Common Subsequence of Two Sequences](week5_dynamic_programming1/4_longest_common_subsequence_of_two_sequences/lcs2.py)

Compute the length of a longest common subsequence of two sequences.

Example: input: [2 7 5], [2 5], output: 2

#### 5 [Longest Common Subsequence of Three Sequences](week5_dynamic_programming1/5_longest_common_subsequence_of_three_sequences/lcs3.py)

Compute the length of a longest common subsequence of three sequences.
