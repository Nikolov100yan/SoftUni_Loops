total_sum = 0

while True:
    new_amount = input()
    if new_amount == "NoMoreMoney":
        break
    else:
        new_amount = float(new_amount)
        if new_amount < 0:
            print("Invalid operation!")
            break
        else:
            print(f"Increase: {new_amount:.2f}")
            total_sum += new_amount

print(f"Total: {total_sum:.2f}")
