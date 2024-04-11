number_months = int(input())
fees_elect = 0      # fees for electricity per month
fees_water = 0      # fees for water per month
fees_inter = 0      # fees for internet per month
fees_other = 0      # all other fees per month
sum_fees_elect = 0
sum_fees_water = 0
sum_fees_inter = 0
sum_fees_other = 0

for months in range(number_months):
    fees_elect = float(input())
    fees_water = 20.00
    fees_inter = 15.00
    fees_other = fees_elect + fees_inter + fees_water + (fees_elect + fees_inter + fees_water) * 0.2
    sum_fees_elect += fees_elect
    sum_fees_water += fees_water
    sum_fees_inter += fees_inter
    sum_fees_other += fees_other

total_fees = sum_fees_other + sum_fees_elect + sum_fees_water + sum_fees_inter
average_fees_per_month = total_fees / number_months

print(f"Electricity: {sum_fees_elect:.2f} lv")
print(f"Water: {sum_fees_water:.2f} lv")
print(f"Internet: {sum_fees_inter:.2f} lv")
print(f"Other: {sum_fees_other:.2f} lv")
print(f"Average: {average_fees_per_month:.2f} lv")

