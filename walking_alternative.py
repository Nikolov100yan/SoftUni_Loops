target = 10000      # steps per day
steps_counter = 0

while steps_counter < target:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        steps_counter += last_steps
        break
    steps_per_day = int(command)
    steps_counter += steps_per_day
difference = abs(target - steps_counter)

if steps_counter >= target:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
