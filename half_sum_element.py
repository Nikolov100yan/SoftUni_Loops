from sys import maxsize

n = int(input())
max_number = - maxsize
sum_numbers = 0

for i in range(n):
    number = int(input())
    sum_numbers += number
    if number > max_number:
        max_number = number

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (sum_numbers - max_number))
    print("No")
    print(f"Diff = {difference}")
