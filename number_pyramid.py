n = int(input())
current_value = 1
current_value_bigger_than_n = False

for raw in range(1, n + 1):
    for column in range(1, raw + 1):
        if current_value > n:
            current_value_bigger_than_n = True
            break
        print(str(current_value) + " ", end="")
        current_value += 1
    if current_value_bigger_than_n:
        break
    print()
