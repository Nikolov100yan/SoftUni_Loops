target_not_achieved = True

while target_not_achieved:
    destination = input()
    if destination == "End":
        target_not_achieved = False
        break
    else:
        minimal_budget = float(input())
        total_saved_budget = 0
        while total_saved_budget < minimal_budget:
            saved_budget = float(input())
            total_saved_budget += saved_budget
        else:
            print(f"Going to {destination}!")
