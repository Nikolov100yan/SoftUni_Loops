heritage_amount = float(input())
final_year = int(input())
age = 18

for years in range(1800, final_year + 1):
    if years % 2 == 0:
        heritage_amount -= 12000
    else:
        heritage_amount -= 12000 + 50 * age
    age += 1

if heritage_amount >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage_amount:.2f} dollars left.")
else:
    print(f"He will need {abs(heritage_amount):.2f} dollars to survive.")
