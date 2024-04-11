targeted_amount = int(input())
accumulated_amount = 0
price = 0
transactions_counter = 0
counter_cash_payments = 0
counter_card_payments = 0
amount_cash_payments = 0
amount_card_payments = 0
transaction_allowed = False

while accumulated_amount < targeted_amount:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        transactions_counter += 1
        price = int(command)
        if transactions_counter % 2 == 0:
            if price >= 10:
                counter_card_payments += 1
                amount_card_payments += price
                transaction_allowed = True
            else:
                transaction_allowed = False
        else:
            if price <= 100:
                counter_cash_payments += 1
                amount_cash_payments += price
                transaction_allowed = True
            else:
                transaction_allowed = False
        if transaction_allowed:
            accumulated_amount += price
            print("Product sold!")
        else:
            print("Error in transaction!")
else:
    average_amount_per_cash_payments = amount_cash_payments / counter_cash_payments
    average_amount_per_card_payments = amount_card_payments / counter_card_payments
    print(f"Average CS: {average_amount_per_cash_payments:.2f}")
    print(f"Average CC: {average_amount_per_card_payments:.2f}")
