s_capacity = int(input())   # capacity of the stadium
n_fans = int(input())       # number of fans
fans_A = 0                  # percentage of fans in sector A from all fans in the stadium
fans_B = 0                  # .... B
fans_V = 0                  # .... V
fans_G = 0                  # .... G
fans_counter = 0

for each_fan in range(n_fans):
    sector = input()        # "A", "B", "V" or "G"
    if sector == "A":
        fans_A += 1
    elif sector == "B":
        fans_B += 1
    elif sector == "V":
        fans_V += 1
    elif sector == "G":      # else
        fans_G += 1
    fans_counter = fans_A + fans_B + fans_V + fans_G

percentage_A = fans_A / fans_counter * 100
percentage_B = fans_B / fans_counter * 100
percentage_V = fans_V / fans_counter * 100
percentage_G = fans_G / fans_counter * 100
percentage_fans = n_fans / s_capacity * 100

print(f"{percentage_A:.2f}%")
print(f"{percentage_B:.2f}%")
print(f"{percentage_V:.2f}%")
print(f"{percentage_G:.2f}%")
print(f"{percentage_fans:.2f}%")
