number_turns = int(input())
score = 0
counter_scores_0_9 = 0
counter_scores_10_19 = 0
counter_scores_20_29 = 0
counter_scores_30_39 = 0
counter_scores_40_50 = 0
counter_scores_invalid = 0

for each_tern in range(number_turns):
    number = int(input())
    if number < 0 or number > 50:
        score /= 2
        counter_scores_invalid += 1
    elif number <= 9:
        score += number * 0.2
        counter_scores_0_9 += 1
    elif number <= 19:
        score += number * 0.3
        counter_scores_10_19 += 1
    elif number <= 29:
        score += number * 0.4
        counter_scores_20_29 += 1
    elif number <= 39:
        score += 50
        counter_scores_30_39 += 1
    elif number <= 50:
        score += 100
        counter_scores_40_50 += 1

percentage_scores_0_9 = counter_scores_0_9 / number_turns * 100
percentage_scores_10_19 = counter_scores_10_19 / number_turns * 100
percentage_scores_20_29 = counter_scores_20_29 / number_turns * 100
percentage_scores_30_39 = counter_scores_30_39 / number_turns * 100
percentage_scores_40_50 = counter_scores_40_50 / number_turns * 100
percentage_scores_invalid = counter_scores_invalid / number_turns * 100

print(f"{score:.2f}")
print(f"From 0 to 9: {percentage_scores_0_9:.2f}%")
print(f"From 10 to 19: {percentage_scores_10_19:.2f}%")
print(f"From 20 to 29: {percentage_scores_20_29:.2f}%")
print(f"From 30 to 39: {percentage_scores_30_39:.2f}%")
print(f"From 40 to 50: {percentage_scores_40_50:.2f}%")
print(f"Invalid numbers: {percentage_scores_invalid:.2f}%")
