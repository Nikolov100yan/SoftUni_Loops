name_actor = input()
academy_score_points = float(input())
number_jury_members = int(input())
jury_score_points = 0    # at the initial moment
total_score = academy_score_points  # at the initial moment
difference = 0

for i in range(number_jury_members):
    jury_member_name = input()
    jury_member_points = float(input())
    jury_score_points = (len(jury_member_name)) * jury_member_points / 2
    total_score += jury_score_points
    if total_score > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_score:.1f}!")
        break
if total_score <= 1250.5:
    difference = abs(1250.5 - total_score)
    print(f"Sorry, {name_actor} you need {difference:.1f} more!")
