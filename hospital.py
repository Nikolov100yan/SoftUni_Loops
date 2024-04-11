period = int(input())               # number days
treated_patients = 0
untreated_patients = 0
doctors = 7                         # at the initial moment

for days in range(1, period + 1):
    if days % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    new_patients = int(input())     # per day
    if new_patients <= doctors:
        treated_patients += new_patients
    else:
        treated_patients += doctors
        untreated_patients += new_patients - doctors


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
