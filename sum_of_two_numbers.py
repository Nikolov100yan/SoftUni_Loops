start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
combinations_counter = 0
magic_combination_found = False
number_1 = 0
number_2 = 0

while number_1 + number_2 != magic_number:
    for number_1 in range(start_interval, end_interval + 1):
        for number_2 in range(start_interval, end_interval + 1):
            combinations_counter += 1
            if number_1 + number_2 == magic_number:
                magic_combination_found = True
                print(f"Combination N:{combinations_counter} ({number_1} + {number_2} = {magic_number})")
                break
        if magic_combination_found:
            break
    if magic_combination_found:
        break
    else:
        print(f"{combinations_counter} combinations - neither equals {magic_number}")
        break
