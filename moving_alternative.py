wight = int(input())
length = int(input())
height = int(input())
free_space = wight * length * height
free_space_available = True
box_counter = 0
difference = 0

while free_space > 0:
    number_boxes = input()
    if number_boxes == "Done":
        break
    number_boxes = int(number_boxes)
    box_counter += number_boxes
    free_space -= number_boxes
else:
    free_space_available = False
    difference = abs(free_space)

if free_space_available:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {difference} Cubic meters more.")
