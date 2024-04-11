number_bottles_detergent = int(input())
volume_one_bottle_detergent = 750
volume_used_for_1_plate = 5
volume_used_for_1_pot = 15
counter_washing_procedures = 0
counter_plates = 0
counter_pots = 0
number_dishes = 0
used_detergent = 0
total_quantity_detergent = number_bottles_detergent * volume_one_bottle_detergent
total_number_dishes = counter_plates + counter_pots

while total_quantity_detergent >= 0:
    order = input()
    if order == "End":
        print("Detergent was enough!")
        print(f"{counter_plates} dishes and {counter_pots} pots were washed.")
        print(f"Leftover detergent {total_quantity_detergent} ml.")
        break
    else:
        number_dishes = int(order)
        counter_washing_procedures += 1
        if counter_washing_procedures % 3 == 0:
            used_detergent = number_dishes * volume_used_for_1_pot
            counter_pots += number_dishes
        else:
            used_detergent = number_dishes * volume_used_for_1_plate
            counter_plates += number_dishes
        total_quantity_detergent -= used_detergent
else:
    print(f"Not enough detergent, {abs(total_quantity_detergent)} ml. more necessary!")
