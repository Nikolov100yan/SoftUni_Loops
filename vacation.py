budget_vacation = float(input())
available_budget = float(input())
days_counter = 0
days_spending = 0

while available_budget < budget_vacation:
    action = input()    # "spend" or "save"
    amount = float(input())
    days_counter += 1
    if action == "save":
        available_budget += amount
        days_spending = 0       # NB!!!!
    elif action == "spend":     # else
        if amount > available_budget:
            amount = available_budget
        available_budget -= amount
        days_spending += 1
        if days_spending == 5:
            print("You can't save the money.")
            print(f"{days_counter}")
            break
else:   # current_budget >= budget_vacation
    print(f"You saved the money for {days_counter} days.")
