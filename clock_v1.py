# This program prints the hours of the day from 0:0 to 23:59, each on a separate line.
# The hours are displayed in the format "{hour} : {minutes}".

for hours in range(24):
    for minutes in range(60):
        print(f"{hours} : {minutes}")
