number_cargos = int(input())
total_cargo_weight = 0
total_price = 0
counter_microbus = 0
counter_truck = 0
counter_train = 0

for cargo in range(number_cargos):
    cargo_weight = int(input())
    total_cargo_weight += cargo_weight
    if cargo_weight <= 3:
        total_price += cargo_weight * 200
        counter_microbus += cargo_weight
    elif cargo_weight <= 11:
        total_price += cargo_weight * 175
        counter_truck += cargo_weight
    else:
        total_price += cargo_weight * 120
        counter_train += cargo_weight

average_price_per_ton = total_price / total_cargo_weight
percentage_tons_microbus = counter_microbus / total_cargo_weight * 100
percentage_tons_truck = counter_truck / total_cargo_weight * 100
percentage_tons_train = counter_train / total_cargo_weight * 100

print(f"{average_price_per_ton:.2f}")
print(f"{percentage_tons_microbus:.2f}%")
print(f"{percentage_tons_truck:.2f}%")
print(f"{percentage_tons_train:.2f}%")