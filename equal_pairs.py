# Given are 2*n numbers. The first and second form a pair, the third and fourth also, and so on.
# Each pair has a value - the sum of its constituent numbers.
# Write a program that checks if all pairs have the same value or
# prints the maximum difference between two consecutive pairs.
# If all pairs have the same value, print "Yes, value={Value}" + the value.
# Otherwise, print "No, maxdiff={Difference}" + the maximum difference.

num_pairs = int(input("Enter the number of pairs: "))

previous_pair_sum = None
max_difference = 0
all_same = True
same_value = None

for _ in range(num_pairs):
    pair_sum = sum(int(input()) for _ in range(2))

    if previous_pair_sum is not None:
        difference = abs(pair_sum - previous_pair_sum)
        if difference > max_difference:
            max_difference = difference
        if difference != 0:
            all_same = False
    else:
        same_value = pair_sum

    previous_pair_sum = pair_sum

if all_same:
    print(f"Yes, value={same_value}")
else:
    print(f"No, maxdiff={max_difference}")
