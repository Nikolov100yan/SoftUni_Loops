wight = int(input())
length = int(input())
height = int(input())
free_space = wight * length * height
box_counter = 0
difference = 0

while free_space > 0:
    number_boxes = input()
    if number_boxes == "Done":
        print(f"{free_space} Cubic meters left.")
        break
    number_boxes = int(number_boxes)
    box_counter += number_boxes
    free_space -= number_boxes
else:
    difference = abs(free_space)
    print(f"No more free space! You need {difference} Cubic meters more.")
