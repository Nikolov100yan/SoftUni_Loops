name = input()
class_counter = 0
total_score = 0
fails_counter = 0
average_score = 0

while class_counter < 12:
    annual_score = float(input())
    if annual_score < 4.00:
        fails_counter += 1
        if fails_counter > 1:
            print(f"{name} has been excluded at {class_counter + 1} grade")
            break
        continue
    class_counter += 1
    total_score += annual_score
else:
    average_score = total_score / class_counter
    print(f"{name} graduated. Average grade: {average_score:.2f}")
