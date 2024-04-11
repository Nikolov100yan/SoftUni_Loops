number_students = int(input())
total_score = 0
counter_students_group1 = 0          # with score between 2.00 and 2.99
counter_students_group2 = 0          # with score between 3.00 and 3.99
counter_students_group3 = 0          # with score between 4.00 and 4.99
counter_students_group4 = 0          # with score over 5.00

for each_student in range(number_students):
    score = float(input())
    total_score += score
    if 2.00 <= score <= 2.99:
        counter_students_group1 += 1
    elif 3.00 <= score <= 3.99:
        counter_students_group2 += 1
    elif 4.00 <= score <= 4.99:
        counter_students_group3 += 1
    else:                            # elif score >= 5.00:
        counter_students_group4 += 1

average_score = total_score / number_students
percentage_group_1 = counter_students_group1 / number_students * 100
percentage_group_2 = counter_students_group2 / number_students * 100
percentage_group_3 = counter_students_group3 / number_students * 100
percentage_group_4 = counter_students_group4 / number_students * 100

print(f"Top students: {percentage_group_4:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_group_3:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_group_2:.2f}%")
print(f"Fail: {percentage_group_1:.2f}%")
print(f"Average: {average_score:.2f}")
