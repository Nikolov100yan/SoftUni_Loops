number = int(input())
numbers_counter = 0
sum_numbers = 0
average_value = 0

while numbers_counter < number:
    new_number = int(input())
    numbers_counter += 1
    sum_numbers += new_number
    average_value = sum_numbers / numbers_counter
else:
    print(f"{average_value:.2f}")
