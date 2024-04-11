number_groups = int(input())
total_number_hikers = 0
counter_peak_1 = 0  # for peak Moussala
counter_peak_2 = 0  # for peak Montblanc
counter_peak_3 = 0  # for peak Kilimanjaro
counter_peak_4 = 0  # for peak K2
counter_peak_5 = 0  # for peak Everest

for hikers in range(number_groups):
    number_hikers_per_group = int(input())
    total_number_hikers += number_hikers_per_group
    if number_hikers_per_group < 6:
        counter_peak_1 += number_hikers_per_group
    elif number_hikers_per_group < 13:
        counter_peak_2 += number_hikers_per_group
    elif number_hikers_per_group < 26:
        counter_peak_3 += number_hikers_per_group
    elif number_hikers_per_group < 41:
        counter_peak_4 += number_hikers_per_group
    else:
        counter_peak_5 += number_hikers_per_group

percentage_hikers_peak_1 = (counter_peak_1 / total_number_hikers) * 100
percentage_hikers_peak_2 = (counter_peak_2 / total_number_hikers) * 100
percentage_hikers_peak_3 = (counter_peak_3 / total_number_hikers) * 100
percentage_hikers_peak_4 = (counter_peak_4 / total_number_hikers) * 100
percentage_hikers_peak_5 = (counter_peak_5 / total_number_hikers) * 100

print(f"{percentage_hikers_peak_1:.2f}%")
print(f"{percentage_hikers_peak_2:.2f}%")
print(f"{percentage_hikers_peak_3:.2f}%")
print(f"{percentage_hikers_peak_4:.2f}%")
print(f"{percentage_hikers_peak_5:.2f}%")
