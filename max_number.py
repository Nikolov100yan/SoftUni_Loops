from sys import maxsize

input_data = ""
max_number = - maxsize

while True:
    input_data = input()
    if input_data == "Stop":
        break
    else:
        input_data = int(input_data)
        max_number = max(max_number, input_data)

print(max_number)
