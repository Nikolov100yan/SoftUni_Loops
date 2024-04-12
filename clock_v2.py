# This program prints the hours of the day from 0:0:0 to 23:59:59, each on a separate line.
# The hours are displayed in the format "{hour} : {minutes} : {seconds}".

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(f"{hours} : {minutes} : {seconds}")
