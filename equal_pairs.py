n = int(input())
sum_pair_1 = 0
sum_pair_2 = 0
difference = abs(sum_pair_1 - sum_pair_2)

for pair_1 in range(1, 2 * n + 1):
    sum_pair_1 = sum_pair_1 + int(input())
for pair_2 in range(1, 2 * n + 1):
    sum_pair_2 = sum_pair_2 + int(input())
if sum_pair_1 == sum_pair_2:
    print(f"Yes, value={sum_pair_1}")
else:
    print(f"No, maxdiff={difference}")
