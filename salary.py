penalty_facebook = 150
penalty_instagram = 100
penalty_reddit = 50
total_penalty = 0

number_open_tabs = int(input())
amount_salary = int(input())
left_over = amount_salary

for i in range(number_open_tabs):
    website_name = input()
    if website_name == "Facebook":
        left_over -= penalty_facebook
    elif website_name == "Instagram":
        left_over -= penalty_instagram
    elif website_name == "Reddit":
        left_over -= penalty_reddit
    if left_over <= 0:
        print(f"You have lost your salary.")
        break
    else:
        continue
if left_over > 0:
    print(f"{left_over}")
