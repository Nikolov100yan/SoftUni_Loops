number_1 = int(input())
number_2 = int(input())

for numbers in range(number_1, number_2 + 1):
    sum_even = 0
    sum_odd = 0
    numbers_as_string = str(numbers)
    for index, digit in enumerate(numbers_as_string):
        if index % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    if sum_even == sum_odd:
        print(numbers_as_string, end=" ")
