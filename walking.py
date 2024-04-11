target = 10000      # steps per day
command = input()
steps_per_day = 0
steps_counter = 0
difference = 0

while True:
    if command != "Going home":
        steps_per_day = int(command)
        steps_counter += steps_per_day
        difference = abs(target - steps_counter)
        if steps_counter >= target:
            print("Goal reached! Good job!")
            print(f"{difference} steps over the goal!")
            break
        else:
            command = input()
    else:
        steps_per_day = int(input())
        steps_counter += steps_per_day
        difference = abs(target - steps_counter)
        if steps_counter < target:
            print(f"{difference} more steps to reach goal.")
            break
        else:
            print("Goal reached! Good job!")
            print(f"{difference} steps over the goal!")
            break
