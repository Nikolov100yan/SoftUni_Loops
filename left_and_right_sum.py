n = int(input())
sum_right = 0
sum_left = 0


for left in range(1, n + 1):
    sum_left = sum_left + int(input())
for right in range(1, n + 1):
    sum_right = sum_right + int(input())

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:  # sum_left != sum_right:
    difference = abs(sum_left - sum_right)
    print(f"No, diff = {difference}")
