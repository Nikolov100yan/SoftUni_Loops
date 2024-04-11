from math import floor

number_competitions = int(input())
start_points = int(input())
points_per_competition = 0
total_score = start_points   # at the initial moment
counter_number_wins = 0

for each_competition in range(number_competitions):
    stage_achieved = input()  # "W" - winner ; "F" - finalist ; "SF" - semi-finalist
    if stage_achieved == "W":
        points_per_competition = 2000
        counter_number_wins += 1
    elif stage_achieved == "F":
        points_per_competition = 1200
    elif stage_achieved == "SF":
        points_per_competition = 720
    total_score += points_per_competition
average_score = (total_score - start_points) / number_competitions   # average score per competition
percentage_wins = (counter_number_wins / number_competitions) * 100

print(f"Final points: {total_score}")
print(f"Average points: {floor(average_score)}")
print(f"{percentage_wins:.2f}%")
