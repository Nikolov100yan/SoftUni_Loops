from sys import maxsize

n = int(input())
number = 0
max_value = - maxsize
min_value = maxsize

for i in range(0, n):
    number = int(input())
    if number > max_value:
        max_value = number
    if number <= min_value:
        min_value = number
print(f"Max number: {max_value}")
print(f"Min number: {min_value}")

