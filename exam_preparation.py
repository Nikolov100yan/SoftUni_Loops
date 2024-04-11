threshold_unsuccessful_tests = int(input())
tests_counter = 0
unsuccessful_tests_counter = 0
test_score = 0
total_score = 0
average_score = 0
test_name = ""
last_test_name = ""

while unsuccessful_tests_counter < threshold_unsuccessful_tests:
    last_test_name = test_name
    test_name = input()
    if test_name == "Enough":
        average_score = total_score / tests_counter
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {tests_counter}")
        print(f"Last problem: {last_test_name}")
        break
    test_score = int(input())
    if test_score <= 4:
        unsuccessful_tests_counter += 1
    tests_counter += 1
    total_score += test_score
else:
    print(f"You need a break, {unsuccessful_tests_counter} poor grades.")
