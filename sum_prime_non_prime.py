command = input()
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
sum_prime_numbers = 0
sum_non_prime_numbers = 0

while command != "stop":
    if command[0] == "-":
        print("Number is negative.")
    else:
        current_number = int(command)
        if current_number in prime_numbers:
            sum_prime_numbers += current_number
        else:
            sum_non_prime_numbers += current_number
    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
