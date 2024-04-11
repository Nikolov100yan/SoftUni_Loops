first_number = int(input())
sum_other_numbers = 0

while True:
    other_numbers = int(input())
    sum_other_numbers += other_numbers
    if sum_other_numbers >= first_number:
        break
print(f"{sum_other_numbers}")
