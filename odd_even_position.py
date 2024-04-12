# The program reads n numbers entered by the user.
# It calculates the sum, min, and max of the numbers at even and odd positions (counting from 1).
# When there is no minimum/maximum element, print "No".
# Each number should be formatted to the second decimal place.

# Define how many numbers you would like to enter
n = int(input("How many numbers you would like to enter? "))

# Check for zero value of n
if n == 0:
    odd_sum = even_sum = "0.00"
    odd_min = odd_max = even_min = even_max = "No"

# Separate the numbers based on their odd and even positions
lis_odd_numbers = []
lis_even_numbers = []
for num_position in range(n):
    number = float(input())
    if (num_position + 1) % 2 == 0:
        lis_even_numbers.append(number)
    else:
        lis_odd_numbers.append(number)

# Check for missing odd values
if len(lis_odd_numbers) == 0:
    odd_sum = "0.00"
    odd_min = odd_max = "No"
else:
    odd_sum = "%.2f" % sum(lis_odd_numbers)
    odd_min = "%.2f" % min(lis_odd_numbers)
    odd_max = "%.2f" % max(lis_odd_numbers)

# Check for missing even values
if len(lis_even_numbers) == 0:
    even_sum = "0.00"
    even_min = even_max = "No"
else:
    even_sum = "%.2f" % sum(lis_even_numbers)
    even_min = "%.2f" % min(lis_even_numbers)
    even_max = "%.2f" % max(lis_even_numbers)

print(f"OddSum={odd_sum},\n"
      f"OddMin={odd_min},\n"
      f"OddMax={odd_max},\n"
      f"EvenSum={even_sum},\n"
      f"EvenMin={even_min},\n"
      f"EvenMax={even_max}")
