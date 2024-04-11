lili_age = int(input())
price_washing_machine = float(input())
price_one_toy = int(input())
even_birthdays = 0
odd_birthdays = 0
number_toys = 0
money_income = 0  # 10 lv each year
annual_bonus = 0  # 10 lv increase per year
toys_income = 0

for i in range(2, lili_age + 1, 2):
    even_birthdays += 1
    money_income += 10 + annual_bonus
    annual_bonus += 10
for i in range(1, lili_age + 1, 2):
    odd_birthdays += 1
    number_toys = odd_birthdays

brother_intake = even_birthdays   # 1 lv per even birthday
toys_income = number_toys * price_one_toy
total_budget = money_income - brother_intake + toys_income
difference = abs(total_budget - price_washing_machine)

if total_budget >= price_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
