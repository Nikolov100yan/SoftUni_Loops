from sys import maxsize

input_data = ""
min_number = maxsize

while True:
    input_data = input()
    if input_data == "Stop":
        break
    else:
        input_data = int(input_data)
        min_number = min(min_number, input_data)

print(min_number)
