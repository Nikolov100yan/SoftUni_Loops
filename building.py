number_floors = int(input())
flats_per_floor = int(input())
flat_name = ""

for floors in range(number_floors, 0, -1):
    for rooms in range(flats_per_floor):
        if floors == number_floors:
            flat_name = f"L{floors}{rooms}"
        elif floors % 2 == 1:
            flat_name = f"A{floors}{rooms}"
        elif floors % 2 == 0:
            flat_name = f"O{floors}{rooms}"
        print(flat_name, end=" ")
    print()
